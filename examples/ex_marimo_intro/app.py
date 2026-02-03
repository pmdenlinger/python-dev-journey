import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _(mo):
    name = mo.ui.text(label="Your name", value="Paul")
    name
    return (name,)


@app.cell
def _(mo, name):
    mo.md(f"""
    Hello, **{name.value}**! 👋
    """)
    return


@app.cell
def _():
    print("Hello world!")
    return


if __name__ == "__main__":
    app.run()
