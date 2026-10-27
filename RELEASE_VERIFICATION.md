# Release verification — mojo-sieve v0.1.1

Verified locally on October 27, 2026, Linux x86-64. Toolchains: Python 3.14.8, Rust 1.98.1, Node.js 26.8.1, Go 1.27.1 and Mojo 1.1.0, as applicable. CI covers additional versions/platforms where configured; consult the workflow run for the release commit rather than an older green run.

## Checks

```sh
python -m unittest discover -v
mojo build core.mojo -o sieve-native
```

**Local result: PASS.** 4 Python tests; piped-log CLI acceptance preserves the fixture error and reduces noise; separate Mojo 1.1.0 kernel compiles and its executable starts.

The Python build command requires the `build` package; Unity checks also require `mypy` and `ruff`. Native Mojo experiments are optional and require Mojo 1.1.0. CLI acceptance used disposable fixtures and no real customer data.

## Release changes

Reject missing files and invalid thresholds instead of silently succeeding.

The README and repository summary now explain the supported behavior, installation, and limits without unverified speed or security promises.

## Limits

Python is the supported CLI; native acceleration/parity is not claimed. Whole input is read into memory. max-lines is a passthrough threshold, not a hard cap.

Git history was checked for common credential/key patterns. Matches in Envghost were synthetic scanner fixtures; no live credentials were identified by that scan. This is a limited pattern check, not a comprehensive security certification.
