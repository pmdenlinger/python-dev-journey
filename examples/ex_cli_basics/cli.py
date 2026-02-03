import typer

app = typer.Typer(help="Tiny greeting CLI")

@app.command()
def hello(name: str = "world"):
    """Print a friendly greeting."""
    typer.echo(f"Hello, {name}!")

if __name__ == "__main__":
    app()
