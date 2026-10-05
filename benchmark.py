import time
from sieve import compact_text

def run_benchmark():
    # Build a realistic 5,000-line test log
    lines = []
    for i in range(4990):
        lines.append(f"test test_suite_{i} ... ok (0.00{i%9}s)")
    lines.append("FAIL: test_critical_auth (auth.py:44)")
    lines.append("  AssertionError: Expected 200 OK, got 401 Unauthorized")
    lines.append("  Traceback (most recent call last):")
    lines.append("    File 'auth.py', line 44, in test_critical_auth")
    for i in range(5):
        lines.append(f"test cleanup_{i} ... ok")

    raw_text = "\n".join(lines)

    # Warmup
    for _ in range(5):
        compact_text(raw_text)

    iterations = 50
    start = time.perf_counter()
    for _ in range(iterations):
        res = compact_text(raw_text)
    total_time = time.perf_counter() - start

    avg_ms = (total_time / iterations) * 1000.0
    print(f"=== mojo-sieve Benchmark ===")
    print(f"Log size: 5,000 lines ({len(raw_text.encode('utf-8')) / 1024:.1f} KB)")
    print(f"Compacted to: {res['compacted_lines']} lines ({res['compression_ratio_pct']}% compressed)")
    print(f"Average compaction latency: {avg_ms:.2f} ms")
    print(f"Throughput: {iterations / total_time:.1f} full log compactions / sec")

if __name__ == "__main__":
    run_benchmark()
