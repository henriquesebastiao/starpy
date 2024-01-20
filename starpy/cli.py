import typer
from rich.console import Console

app = typer.Typer()
console = Console()
__version__ = '0.1.0'


def version(value: bool):
    if value:
        console.print(
            f'[bold blue]StarPy[/bold] version: [green]{__version__}[/green]'
        )
        raise typer.Exit()


@app.command()
def main():
    ...
