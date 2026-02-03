# Python Journey – Reproducible Notebooks & Tools (marimo + uv)

This repository documents my **Python learning path** with a focus on:

- **Reproducible environments** using **uv** (fast package + venv manager)
- **Explorable notebooks** using **marimo** (Python-native interactive notebooks)
- **Small, practical examples** → **thin, real projects** that support compliance, data quality,
  and light automation

The structure mirrors my Rust and other language repos for consistency.

---

## What to look at first
- **[SUMMARY.md](SUMMARY.md)** – one-page index of examples and projects
- **[projects/](projects/)** – portfolio-style code with design notes
- **[docs/architecture](docs/architecture/)** – decisions: why marimo + uv, notebooks vs scripts

## Tooling
- **Python**: 3.11+
- **uv**: creates virtual environments, resolves + installs deps, runs tools
- **marimo**: interactive notebooks in plain `.py` files

Common commands:

```bash
# Create and use a virtual environment
uv venv

# Install all dependencies (incl. dev extras)
uv sync --all-extras --dev

# Run marimo notebook editor
uv run marimo edit examples/ex_marimo_intro/app.py

# Lint & tests
uv run ruff check .
uv run pytest -q
```

## Status Badges
![CI](https://github.com/pmdenlinger/python-dev-journey/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## Learning Philosophy
Progress from **small, focused examples** → **real projects**. Each step is documented with:
- Motivation
- Constraints & trade-offs
- Tests and observability where it makes sense

---

## License
[MIT](LICENSE)
