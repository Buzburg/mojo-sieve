# Mojo Sieve 🔎

**Find the failure in the flood.**

Turn a noisy build log into error-focused context. Sieve keeps recognized errors, nearby lines, and the beginning and end of the output, inserting visible markers where it omits content.

## Try it

Requires Python 3.11+. No Python runtime dependencies or model download.

```sh
git clone https://github.com/Buzburg/mojo-sieve.git
cd mojo-sieve
python sieve.py /path/to/build.log
```

For Bash pipelines, capture stderr and preserve the command's failure status:

```bash
set -o pipefail
npm test 2>&1 | python /path/to/mojo-sieve/sieve.py
```

Use `--max-lines 60` to set the short-log passthrough threshold. It is **not a hard output cap**: every recognized error window is retained, so a failure-heavy log can exceed it. Statistics go to stderr; compacted text goes to stdout.

## Know what was omitted

Recognition is regex-based, not semantic debugging. Keep the original log when exact evidence matters. Unknown error formats and relevant context can be omitted. The CLI reads the complete input into memory; it is not a bounded-memory streaming processor.

The supported CLI is Python. `core.mojo` is a separate experimental kernel; the CLI does not load it, and kernel compilation does not establish native acceleration or parity.

## Verify

```sh
python -m unittest discover -v
# Optional native experiment, using Mojo 1.1.0:
mojo build core.mojo -o sieve-native
```

[Release verification](RELEASE_VERIFICATION.md). MIT licensed. Built by Buzburg.
