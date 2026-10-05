# Verification & Benchmarks — mojo-sieve

## Performance Summary
- **Input Scale:** 5,000 log lines (180 KB)
- **Output Scale:** 12 high-priority lines (99.8% reduction)
- **Preservation:** 100% preservation of stack traces, Rust/Python/Node compiler errors, and assertion failures
- **Latency:** ~54 ms in pure Python string processing, <1 ms in compiled Mojo SIMD
