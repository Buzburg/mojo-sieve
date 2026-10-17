# mojo-sieve ⚡

**Release status: experimental.** The Python CLI runs its own reference implementation; it does not load `core.mojo`. The separate native kernel compiles with Mojo 1.1.0. Python tests and native compilation do not establish end-to-end native speed, model accuracy, or production safety. Historical timing and savings figures below are not release guarantees. See [launch review](LAUNCH_READINESS.md).

> [!NOTE]
> **In Plain English:** When an AI coding agent runs test suites or compilers, the terminal often outputs thousands of lines of logs. Dumping all of that into context burns tokens and causes the agent to lose focus. `mojo-sieve` streams through multi-thousand-line logs in under 2 milliseconds, extracting the critical stack traces, failure assertions, and compiler errors while pruning 95%+ of repetitive passing tests and noise.

---

## ⚡ Features

- **Microsecond Log Compaction:** Compresses 5,000+ line terminal outputs in <2 ms.
- **Adaptive Windowing:** Preserves root-cause error lines plus 2 surrounding context lines for accurate debugging.
- **Noise Suppression:** Automatically suppresses repetitive unit test checkmarks, spinners, and downloading progress bars.
- **Pipelined CLI:** Drop-in pipe support for any command: `npm test | python sieve.py`.

---

## 🚀 Quickstart

```bash
# Pipe any command through mojo-sieve
cargo test | python sieve.py

# Or compact an existing log file
python sieve.py build_failure.log
```

---

## 🧪 Testing

```bash
python -m unittest test_sieve.py
```

---

## 📄 License

[MIT](LICENSE) © 2026 Buzburg AI
