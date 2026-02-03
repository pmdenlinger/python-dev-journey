# ADR-0001: Use uv for environments and marimo for notebooks
- **Status**: Accepted
- **Date**: 2026-02-03

## Context
This repo needs fast, reproducible Python environments and notebooks that are version-control
friendly and easy to run locally and in CI.

## Decision
- Use **uv** for dependency resolution, virtualenv management, and command running.
- Use **marimo** for interactive notebooks in plain `.py` files, avoiding heavy `.ipynb` JSON.

## Alternatives Considered
- `pip` + `venv`: lightweight but slower installs and no single entrypoint for commands.
- Conda/mamba: powerful but heavier than necessary for this repo.
- Jupyter notebooks: ubiquitous, but `.ipynb` is noisy in diffs and awkward in reviews.

## Consequences
- Faster cold/warm installs; simpler CI.
- Cleaner diffs and better code review for notebooks.
- Contributors need `uv` installed; add quick-start to README.
