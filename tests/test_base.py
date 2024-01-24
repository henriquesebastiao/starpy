import os
from unittest import TestCase

import requests
from typer.testing import CliRunner, Result

from skyport.cli import __version__, app, download_image, remaining_api


class CliUnitTest(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.runner = CliRunner()

    def invoke(self, *flags: str) -> Result:
        """
        Simplify the invoke of the app for tests
        Args:
            *flags: Flags to be passed to the app

        Returns:
            Result of the invoke
        """
        return self.runner.invoke(app, [*flags])

    def test_cli_version_and_developer_name(self):
        result = self.invoke('--version')
        self.assertEqual(result.exit_code, 0)
        self.assertIn(f'Skyport version: {__version__}', result.stdout)
        self.assertIn('Developed by Henrique Sebastião', result.stdout)

    def test_cli_print_help_message_if_without_args(self):
        result = self.invoke()
        print(type(result.stdout))
        message = """USAGE: skyport [OPTIONS] COMMAND [OPTIONS]

There are 1 commands available:

- apod: Returns the image of the day from NASA's

Examples:
skyport apod (search for the image of the day)
skyport apod -d 2021-01-01 (search for the image of the day on the date)
skyport apod -s (download the image)

For more information: skyport --help
For more detailed information: repository
"""
        self.assertIn(message, result.stdout)

    def test_remaining_requests(self):
        response = requests.get(
            'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
        )
        result = remaining_api(response)
        self.assertIn(
            f'Remain {response.headers.get("X-RateLimit-Remaining")} requests',
            result,
        )
        self.assertIn('More information at: https://api.nasa.gov/', result)

    def test_if_remaining_requests_is_none(self):
        response = requests.get('https://httpbin.org/get')
        self.assertIn(
            'API limit information not found.', remaining_api(response)
        )

    def test_download_image(self):
        download_image('https://picsum.photos/200/300')
        self.assertTrue(os.path.exists('image.jpg'))
        os.remove('image.jpg')
