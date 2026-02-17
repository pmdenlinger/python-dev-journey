import marimo

__generated_with = "0.19.8"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    print("Hello, World!")
    return


if __name__ == "__main__":
    app.run()
