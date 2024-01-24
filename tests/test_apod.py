import os
from unittest.mock import Mock, patch

from .test_base import CliUnitTest


class ApodTest(CliUnitTest):
    def assert_messages_apod_2022_01_01_in_stdout(self, result):
        messages = [
            'The Full Moon of 2021',
            'Copyright: Soumyadeep Mukherjee',
            'Image link: https://apod.nasa.gov/apod/image/2201/MoonstripsAnnotatedIG.jpg',
        ]
        for message in messages:
            self.assertIn(message, result.stdout)

    def test_return_with_remaining_option_of_apod(self):
        result = self.invoke('apod', '--date', '2022-01-01', '-r')
        self.assert_messages_apod_2022_01_01_in_stdout(result)
        self.assertIn('Remain', result.stdout)
        self.assertIn('requests', result.stdout)
        self.assertIn(
            'More information at: https://api.nasa.gov/', result.stdout
        )

    def test_return_without_remaining_option_of_apod(self):
        result = self.invoke('apod', '--date', '2022-01-01')
        self.assert_messages_apod_2022_01_01_in_stdout(result)
        self.assertNotIn(
            'More information at: https://api.nasa.gov/', result.stdout
        )

    def test_return_with_save_image_option_of_apod(self):
        result = self.invoke('apod', '-s', '--date', '2022-01-01')
        self.assert_messages_apod_2022_01_01_in_stdout(result)
        self.assertIn('Image saved as image.jpg', result.stdout)
        os.remove('image.jpg')

    @patch('requests.get')
    def test_copyright(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'copyright': 'Copyright Information',
            'title': 'Test Title',
            'explanation': 'Test Explanation',
            'hdurl': 'Test URL',
        }
        mock_get.return_value = mock_response

        result = self.invoke('apod')
        self.assertIn('Copyright', result.stdout)
        self.assertEqual(result.exit_code, 0)

    @patch('requests.get')
    def test_api_limit_exceeded(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 429
        mock_get.return_value = mock_response

        result = self.invoke('apod')
        self.assertIn('Too many requests', result.stdout)
        self.assertEqual(result.exit_code, 1)

    @patch('requests.get')
    def test_response_with_unknown_status_code(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        result = self.invoke('apod')
        self.assertIn('ATTENTION', result.stdout)
        self.assertEqual(result.exit_code, 1)
