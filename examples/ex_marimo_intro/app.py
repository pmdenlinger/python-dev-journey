import marimo

__generated_with = "0.19.7"
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


if __name__ == "__main__":
    app.run()
