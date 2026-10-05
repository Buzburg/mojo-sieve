import unittest
from sieve import compact_text, score_line

class TestMojoSieve(unittest.TestCase):
    def test_noise_suppression(self):
        # 100 lines of noise + 1 compiler error
        noise_lines = ["test case passed: ok" for _ in range(100)]
        error_lines = [
            "error[E0425]: cannot find value `foo` in this scope",
            "  --> src/main.rs:14:5",
            "   |",
            "14 |     foo();",
            "   |     ^^^ not found in this scope"
        ]
        full_log = "\n".join(noise_lines + error_lines + noise_lines)

        res = compact_text(full_log, max_lines=30)
        self.assertGreater(res["compression_ratio_pct"], 75.0)
        self.assertIn("cannot find value `foo`", res["text"])
        self.assertIn("src/main.rs:14:5", res["text"])
        self.assertIn("truncated by mojo-sieve", res["text"])

    def test_short_log_passthrough(self):
        short = "Line 1\nLine 2\nLine 3"
        res = compact_text(short, max_lines=10)
        self.assertEqual(res["compacted_lines"], 3)
        self.assertEqual(res["compression_ratio_pct"], 0.0)

if __name__ == "__main__":
    unittest.main()
