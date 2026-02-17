# Python Journey – Reproducible Notebooks & Tools (marimo + uv)

This repository documents my **Python learning path** with a focus on:

- **Reproducible environments** using **uv** (fast package + venv manager). [\[github.com\]](https://github.com/python/peps/blob/main/peps/pep-0723.rst)
- **Explorable notebooks** using **marimo** (Python‑native interactive notebooks). [\[pypi.org\]](https://pypi.org/project/pep723/)
- **Small, practical examples** → **thin, real projects** that support compliance, data quality, and light automation.

The structure mirrors my Rust and other language repos for consistency.

---

## marimo quickstart

- Edit notebooks: `uv run marimo edit notebooks/00_welcome.py` [\[pypi.org\]](https://pypi.org/project/pep723/)
- Run as app: `uv run marimo run notebooks/00_welcome.py` [\[pypi.org\]](https://pypi.org/project/pep723/)
- Convert Jupyter to marimo: `uv run marimo convert demo.ipynb -o notebooks/demo.py` [\[pypi.org\]](https://pypi.org/project/pep723/)

---

## Notebook dependencies (PEP 723)

marimo uses **uv** to manage **per‑notebook dependencies** using PEP 723 inline metadata—this lets **each notebook** declare its own environment. [\[pydevtools.com\]](https://pydevtools.com/handbook/how-to/how-to-write-a-self-contained-script/), [\[startdatae...eering.com\]](https://www.startdataengineering.com/post/python-notebook-best-practices-for-data-engineering/)

**Example:**

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo", "polars", "duckdb"]
# ///
```

---

## How marimo + uv + PEP 723 work (and why it matters)

---

```

Project mode                           Sandbox mode
-------------                          -----------------------------
 repo/                                  notebooks/y.py
 ├─ pyproject.toml  (shared deps)       ├─ PEP 723 header (deps here)
 └─ notebooks/x.py                      └─ code cells

 Launch:                                Launch:
   uv run marimo edit                     uvx marimo edit --sandbox
     notebooks/x.py                         notebooks/y.py

 Kernel env:                            Kernel env:
   project venv (shared)                  per-file venv (isolated)

```

**marimo** is a reactive notebook that stores notebooks as plain **`.py`** files instead of JSON, which makes them git‑friendly, script‑runnable, and easy to reuse. You edit with `marimo edit`, run as an app with `marimo run`, and convert from Jupyter with `marimo convert`. [\[marketplac...studio.com\]](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo), [\[pypi.org\]](https://pypi.org/project/pep723/), [\[docs.marimo.io\]](https://docs.marimo.io/guides/package_management/using_uv/)

**uv** is a modern, fast Python package & environment manager. marimo integrates tightly with uv in two workflows: (1) **project notebooks** that use the repo’s `pyproject.toml`; and (2) **sandboxed notebooks** that declare their own deps inline in the file. [\[pydevtools.com\]](https://pydevtools.com/handbook/how-to/how-to-write-a-self-contained-script/), [\[github.com\]](https://github.com/python/peps/blob/main/peps/pep-0723.rst)

**PEP 723** defines **inline script metadata**—a standardized way to put dependencies and Python version requirements _inside a single file_. Tools (like uv) read this metadata, create an isolated env, install exactly those deps, and run the file. This is what powers marimo’s **sandboxed notebooks**. [\[startdatae...eering.com\]](https://www.startdataengineering.com/post/python-notebook-best-practices-for-data-engineering/)

---

### File‑level dependencies with PEP 723

A marimo notebook can declare its own environment at the top of the file:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo", "polars", "duckdb"]
# ///
```

- **What this does:** When you launch with `uvx marimo edit --sandbox notebooks/00_welcome.py`, uv reads the block, builds an isolated env for this one file, installs those packages, and starts marimo. No global pollution, no guessing which `venv` to use. [\[pydevtools.com\]](https://pydevtools.com/handbook/how-to/how-to-write-a-self-contained-script/)
- **Why it’s new & important:** PEP 723 (created **Aug 4, 2023**; finalized **Jan 8, 2024**) standardized this inline format, so single‑file notebooks/scripts are portable and reproducible across tools. [\[startdatae...eering.com\]](https://www.startdataengineering.com/post/python-notebook-best-practices-for-data-engineering/)

---

### When do you need PEP 723?

- **Sandboxed notebooks (recommended for examples/tutorials):** **Yes.** Inline metadata makes each notebook self‑contained and shareable. [\[pydevtools.com\]](https://pydevtools.com/handbook/how-to/how-to-write-a-self-contained-script/)
- **Project notebooks (shared repo env):** **No.** Add marimo to your project (`uv add marimo`) and run `uv run marimo edit notebooks/x.py`; dependencies come from `pyproject.toml`. [\[github.com\]](https://github.com/python/peps/blob/main/peps/pep-0723.rst)

---

### SQL cells in marimo

If you use `mo.sql("…")` in a notebook, install marimo’s SQL extras (or include them in the PEP 723 block), e.g.:

```bash
# project mode
uv add "marimo[sql]"

# sandbox mode (adds to the notebook header)
uv add --script notebooks/00_welcome.py "marimo[sql]"
```

This pulls in the optional SQL stack (DuckDB backend + SQL parsing), enabling SQL cells to query DataFrames and databases directly from a notebook. [\[stackoverflow.com\]](https://stackoverflow.com/questions/46775346/what-do-square-brackets-mean-in-pip-install)

> Tip: For interactive tables / DataFrame outputs, install **Polars** (or Pandas). marimo’s SQL guide explains supported output types and backends. [\[stackoverflow.com\]](https://stackoverflow.com/questions/46775346/what-do-square-brackets-mean-in-pip-install)

---

## Why marimo instead of Jupyter?

marimo gives me:

- **Pure `.py` notebooks** → clean diffs, reusable modules, runnable as scripts. [\[marketplac...studio.com\]](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)
- **Reactive execution** → dependent cells auto‑update (no hidden state). [\[marketplac...studio.com\]](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)
- **Built‑in SQL + data tooling.** [\[stackoverflow.com\]](https://stackoverflow.com/questions/46775346/what-do-square-brackets-mean-in-pip-install)
- **PEP 723 environments via uv** → self‑contained, reproducible notebooks. [\[pydevtools.com\]](https://pydevtools.com/handbook/how-to/how-to-write-a-self-contained-script/), [\[startdatae...eering.com\]](https://www.startdataengineering.com/post/python-notebook-best-practices-for-data-engineering/)

---

## What to look at first

- **SUMMARY.md** – one‑page index of examples and projects
- **projects/** – portfolio‑style code with design notes
- **docs/architecture/** – decisions: why marimo + uv, notebooks vs scripts

---

## Tooling

- **Python:** 3.11+
- **uv:** creates virtual environments, resolves + installs deps, runs tools. [\[github.com\]](https://github.com/python/peps/blob/main/peps/pep-0723.rst)
- **marimo:** interactive notebooks in plain `.py` files. [\[marketplac...studio.com\]](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)

**Common commands:**

```bash
# Create and use a virtual environment
uv venv

# Install all dependencies (incl. dev extras)
uv sync --all-extras --dev

# Run marimo notebook editor (project mode)
uv run marimo edit notebooks/00_welcome.py

# Lint & tests
uv run ruff check .
uv run pytest -q
```

---

## Status Badges

<https://github.com/pmdenlinger/python-dev-journey/actions/workflows/ci.yml/badge.svg>  
<https://img.shields.io/badge/License-MIT-green.svg>

---

## Learning Philosophy

Progress from **small, focused examples** → **real projects**. Each step is documented with:

- Motivation
- Constraints & trade‑offs
- Tests and observability where it makes sense

---

## License

LICENSE

---

### References

- marimo docs: quickstart & CLI commands (`edit`, `run`, `convert`). [\[pypi.org\]](https://pypi.org/project/pep723/), [\[docs.marimo.io\]](https://docs.marimo.io/guides/package_management/using_uv/)
- marimo architecture & file format (plain `.py` notebooks). [\[marketplac...studio.com\]](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)
- marimo SQL guide and DuckDB integration. [\[stackoverflow.com\]](https://stackoverflow.com/questions/46775346/what-do-square-brackets-mean-in-pip-install), [\[stackoverflow.com\]](https://stackoverflow.com/questions/30239152/specify-extras-require-with-pip-install-e)
- uv + marimo integration, sandbox vs. project workflows. [\[pydevtools.com\]](https://pydevtools.com/handbook/how-to/how-to-write-a-self-contained-script/), [\[github.com\]](https://github.com/python/peps/blob/main/peps/pep-0723.rst)
- PEP 723 (inline script metadata): creation/finalization dates and spec. [\[startdatae...eering.com\]](https://www.startdataengineering.com/post/python-notebook-best-practices-for-data-engineering/)
