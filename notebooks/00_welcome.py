# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo","polars","duckdb"]
# ///
import marimo as mo

app = mo.App()

@app.cell
def _():
    import polars as pl
    df = pl.DataFrame({"repo": ["python-dev-journey"], "hello": ["world"]})
    df
    return df

@app.cell
def _(df):
    import marimo as mo
    # SQL against a local dataframe (requires duckdb)
    result = mo.sql(f"SELECT repo, hello FROM df")
    result
    return result

if __name__ == "__main__":
    app.run()