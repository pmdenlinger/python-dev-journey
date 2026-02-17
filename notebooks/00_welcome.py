# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo","polars","duckdb"]
# ///

import marimo

__generated_with = "0.19.11"
app = marimo.App()


@app.cell
def _():
    import polars as pl
    df = pl.DataFrame({"repo": ["python-dev-journey"], "hello": ["world"]})
    df
    return


@app.cell
def _():
    import marimo as mo
    # SQL against a local dataframe (requires duckdb)
    result = mo.sql(f"SELECT repo, hello FROM df")
    result
    return


if __name__ == "__main__":
    app.run()
