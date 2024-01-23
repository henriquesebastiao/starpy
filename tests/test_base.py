import os
from unittest import TestCase

import requests
from typer.testing import CliRunner, Result

from skyport.cli import app, download_image, remaining_api


def check_result_error(result: Result):
    if result.exit_code == 1:
        assert 'Too many requests' in result.output


class CliUnitTest(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.runner = CliRunner()

    def setUp(self):
        os.environ['NASA_API_KEY'] = '0F0KeeYZ7axdckLa9VyRQZGTslLkkl6tmbdcapaj'

    def invoke(self, *flags: str) -> Result:
        """
        Simplify the invoke of the app for tests
        Args:
            *flags: Flags to be passed to the app

        Returns:
            Result of the invoke
        """
        return self.runner.invoke(app, [*flags])

    def test_cli_version(self):
        result = self.invoke('--version')
        assert result.exit_code == 0
        assert 'version' in result.output

    def test_cli_print_help_message_if_without_args(self):
        result = self.invoke()
        self.assertIn('USAGE', result.output)

    def test_remaining_requests(self):
        response = requests.get(
            'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
        )
        self.assertIn('More information', remaining_api(response))

    def test_if_remaining_requests_is_none(self):
        response = requests.get('https://httpbin.org/get')
        self.assertIn(
            'API limit information not found.', remaining_api(response)
        )

    def test_download_image(self):
        download_image('https://picsum.photos/200/300')
        self.assertTrue(os.path.exists('image.jpg'))
        os.remove('image.jpg')
