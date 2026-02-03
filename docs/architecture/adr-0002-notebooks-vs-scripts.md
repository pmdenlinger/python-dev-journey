# ADR-0002: Notebooks vs Scripts
- **Status**: Accepted
- **Date**: 2026-02-03

## Context
Some tasks are better as reproducible notebooks, others as plain scripts/CLIs. We need a simple
rule so the repo stays coherent.

## Decision
- Use **marimo notebooks** for exploration, tutorials, and report-like artifacts.
- Use **scripts/CLIs** (plain `.py` with Typer) when the goal is automation or reuse.

## Consequences
- Examples can start as notebooks, then graduate into scripts as they stabilize.
- Tests focus on scriptable parts; notebooks kept small and intentional.
