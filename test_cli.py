import subprocess
import sys
import unittest
from pathlib import Path

class CLITests(unittest.TestCase):
    def test_missing_file_fails(self):
        p = subprocess.run([sys.executable, str(Path(__file__).with_name('sieve.py')), 'missing-fixture.log'], input='', text=True, capture_output=True)
        self.assertNotEqual(p.returncode, 0)

    def test_negative_limit_fails(self):
        p = subprocess.run([sys.executable, str(Path(__file__).with_name('sieve.py')), '--max-lines', '-1'], input='test', text=True, capture_output=True)
        self.assertNotEqual(p.returncode, 0)
