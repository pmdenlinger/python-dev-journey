# Clydebank Coffee Simulator

_A progressively built simulation project following the Python QuickStart guide. This project grows feature‑by‑feature across commits to demonstrate design decisions, testing, and refactoring over time._

---

## Table of Contents

- \#project-overview
- \#goals--non-goals
- \#getting-started
- \#project-structure
- \#running-the-simulator
- \#notebooks-analysis--exploration
- \#configuration-if-applicable
- \#testing--quality
- \#milestones--progress-log
- \#design-decisions-adr-index
- \#roadmap--next-steps
- \#license

---

## Project Overview

**Clydebank Coffee** simulates a small coffee operation (menu, order flow, queues, timing, and costs).  
It begins as simple scripts and evolves into a modular design with clear separation of concerns:

- **Core domain**: menu items, pricing, order lifecycle
- **Simulation**: arrival rates, service times, queue behavior
- **Metrics**: throughput, wait time, revenue/cost summaries
- **(Optional) Visualization**: analysis notebooks with charts/tables

> **Portfolio value:** Commits show how requirements are translated into code, how refactors improve structure, and how tests/metrics validate the system.

---

## Goals & Non‑Goals

**Goals**

- Build the simulator iteratively, one concept at a time.
- Capture _clean commits_ that map to book chapters/sections.
- Practice testable design, small abstractions, and refactors.
- Produce analysis notebooks to interpret simulation outputs.

**Non‑Goals**

- Real‑time UI or production deployment.
- Full‑blown microservices or distributed design.
- Heavy frameworks—keep it lightweight and idiomatic.

---

## Getting Started

> **Project mode** (recommended): use the repo’s environment defined in `pyproject.toml`.

```bash
# from repo root
uv venv
uv sync --all-extras --dev
```

> If you prefer a one‑off sandboxed notebook later, you can still use PEP 723 inline metadata in a specific file. For the main simulator, stick with **project mode** for consistency.

---

## Project Structure

```

    projects/clydebank_coffee/
    ├─ src/                     # Python modules for the simulator
    │  ├─ __init__.py
    │  ├─ domain/               # menu, orders, pricing
    │  ├─ sim/                  # queue/arrival/service logic
    │  ├─ metrics/              # stats, summaries, reporting
    │  └─ cli.py                # optional CLI entrypoint
    ├─ notebooks/               # marimo notebooks for analysis (project mode)
    │  └─ analysis.py
    ├─ docs/                    # ADRs, diagrams, notes
    │  ├─ ADR-0001.md           # example: module layout decision
    │  └─ diagrams/             # optional architecture sketches
    └─ README.md                # this file
```

> Keep domain logic in `src/`. Use notebooks for exploration & reporting—not as the primary source of business logic.

---

## Running the Simulator

**Run as a plain Python program (project mode):**

```bash
uv run python projects/clydebank_coffee/src/cli.py --help
uv run python projects/clydebank_coffee/src/cli.py \
  --customers 250 --baristas 2 --seed 123
```

**Or run a specific module:**

```bash
uv run python -m projects.clydebank_coffee.src.cli --customers 250
```

_(Adjust CLI flags as they evolve—this file is a living guide.)_

---

## Notebooks (Analysis & Exploration)

**Open the analysis notebook with marimo (project mode):**

```bash
uv run marimo edit projects/clydebank_coffee/notebooks/analysis.py
```

Typical uses:

- Load simulation outputs (CSV/Parquet/JSON) and compute aggregates.
- Compare scenarios (e.g., 1 vs 2 baristas, new drink added).
- Plot wait times, throughput, and revenue.

> If you ever need a standalone/isolated notebook, you may add a PEP 723 header to _that notebook only_ and launch via sandbox mode. Keep the simulator itself in project mode.

---

## Configuration (If Applicable)

If/when configuration is introduced:

- `config/` folder or a `pyproject.toml`/`.env` entry
- Default parameters (arrival rate, service time distributions, menu prices)
- Override via CLI flags or environment variables

Example:

```bash
uv run python projects/clydebank_coffee/src/cli.py \
  --config projects/clydebank_coffee/config/dev.toml
```

---

## Testing & Quality

**Run tests & linting:**

```bash
uv run pytest -q
uv run ruff check .
uv run ruff format .
```

**Suggested structure:**

    projects/clydebank_coffee/
    ├─ tests/
    │  ├─ test_domain.py
    │  ├─ test_sim.py
    │  └─ test_metrics.py

Keep tests close to the code they validate. Add quick unit tests as features land.

---

## Milestones & Progress Log

> Update this list as you go. Each bullet should match a commit (or small set of commits).

- **M0 – Bootstrap**: create project folders, initial `cli.py` skeleton
- **M1 – Menu & Pricing**: domain models for drinks and prices
- **M2 – Order Lifecycle**: place order, prepare, complete
- **M3 – Queue Mechanics**: arrival/service distribution, barista capacity
- **M4 – Metrics**: wait time, throughput, revenue summary
- **M5 – Parameterization**: CLI flags/config toggles
- **M6 – Analysis Notebook**: scenario comparison & plots
- **M7 – Refactor/Docs**: tidy modules, add ADRs, improve tests

---

## Design Decisions (ADR Index)

Keep short **Architecture Decision Records** in `docs/`:

- **ADR‑0001**: Package/module layout for `domain/`, `sim/`, `metrics/`
- **ADR‑0002**: Randomness & reproducibility strategy (seeding)
- **ADR‑0003**: Data interchange format (CSV vs JSON vs Parquet)
- **ADR‑0004**: CLI parameters and defaults
- **ADR‑0005**: Performance considerations (profiling / batching)

_(Add/renumber as needed; link to files once created.)_

---

## Roadmap / Next Steps

- Add scenario presets (e.g., morning rush, weekend, promotions)
- Add inventory/cost modeling (beans, milk, cups) for margin analysis
- Support multiple queues vs single shared queue
- Sensitivity analysis: how does utilization affect wait time?
- (Optional) Visualization improvements in notebooks

---

## License

This project is from the book Python QuickStart Guide (Robert Oliver) and the Github repo is at https://github.com/clydebankmedia/python-quickstartguide and license is at https://github.com/clydebankmedia/python-quickstartguide?tab=License-1-ov-file.

---
