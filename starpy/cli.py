import os
from datetime import datetime

import requests
import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing_extensions import Annotated, Optional

# Settings of CLI
__version__ = '0.1.0'
WARNING = (
    '[bold red]ATTENTION: something wrong seems to have happened![/bold red]'
)

# Settings for consuming Nasa API
HOST = 'https://api.nasa.gov/'
NASA_API_KEY = os.getenv('NASA_API_KEY', 'DEMO_KEY')
date_now = datetime.now().date().isoformat()

app = typer.Typer(help='StarPy is a cli for obtaining information from astronomical objects.')
console = Console()


def get_version(value: bool):
    if value:
        console.print(
            f'[bold blue]StarPy[/bold blue] version: [green]{__version__}[/green]',
        )
        console.print('Developed by [bold]Henrique Sebastião[/bold]')
        raise typer.Exit()


def remaining_api(response: requests.Response):
    limit = response.headers.get('X-RateLimit-Remaining', None)
    if limit is None:
        return '\nAPI limit information not found.'
    return f"""\nRemain {limit} requests\nMore information at: https://api.nasa.gov/"""


def download_image(url: str):
    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        transient=True,
    ) as progress:
        progress.add_task(description='Downloading image...', total=None)
        response = requests.get(url, stream=True)

    with open('image.jpg', 'wb') as file:
        file.write(response.content)
    console.print('[bold green]Image saved as image.jpg[/bold green]')


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Annotated[  # noqa: F841
        Optional[bool],
        typer.Option(
            '--version',
            '-v',
            callback=get_version,
            help='Returns the version of StarPy',
        ),
    ] = None,
):
    message = """USAGE: starpy [OPTIONS] COMMAND [OPTIONS]

There are 1 commands available:

- [bold]apod[/bold]: Returns the image of the day from NASA's

[bold]Examples:[/bold]
[italic yellow]starpy apod[/italic yellow] (search for the image of the day)
[italic yellow]starpy apod -d 2021-01-01[/italic yellow] (search for the image of the day on the date)
[italic yellow]starpy apod -s[/italic yellow] (download the image)

[bold]For more information:[/bold] [italic cyan]starpy --help[/italic cyan]
[bold]For more detailed information:[/bold] [cyan][link=https://github.com/henriquesebastiao/starpy]repository[/cyan]
"""
    if ctx.invoked_subcommand:
        return
    console.print(message)


@app.command()
def apod(
    date: Annotated[
        str,
        typer.Option(
            '--date', '-d', help='Date to search for the image of the day'
        ),
    ] = date_now,
    save_image: Annotated[
        bool, typer.Option('--save-image', '-s', help='Download the image')
    ] = False,
    remaining: Annotated[
        bool,
        typer.Option(
            '--remaining',
            '-r',
            help='Tells how many requests remain for the API',
        ),
    ] = False,
):
    url = HOST + 'planetary/apod'

    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        transient=True,
    ) as progress:
        progress.add_task(description='Searching...', total=None)
        response = requests.get(
            url, params={'api_key': NASA_API_KEY, 'date': date}
        )

    if response.status_code == 200:
        info: dict = response.json()
        console.print(f'[bold]{info["title"]}[/bold]')
        if info.__contains__('copyright'):
            console.print(f'Copyright: {info["copyright"]}')
        console.print('\n' + info['explanation'] + '\n')
        console.print(f'[bold]Image link:[/bold] {info["hdurl"]}')

        if save_image:
            download_image(info['hdurl'])

        if remaining:
            console.print(remaining_api(response))
    elif response.status_code == 429:
        console.print(
            '[bold red]Error [bold blue]429[/bold blue]: Too many requests, '
            'you have exceeded the request limit for your API key.[/bold red]'
        )
        raise typer.Exit(code=1)
    else:
        console.print(WARNING)
