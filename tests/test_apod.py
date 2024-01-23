import os
from unittest.mock import Mock, patch

from .test_base import CliUnitTest


class ApodTest(CliUnitTest):
    def test_return_with_remaining_option_of_apod(self):
        result = self.invoke('apod', '--date', '2024-01-01', '-r')
        self.assertIn('Remain', result.output)

    def test_return_without_remaining_option_of_apod(self):
        result = self.invoke('apod', '--date', '2024-01-01')
        self.assertNotIn('Remain', result.output)

    def test_return_with_save_image_option_of_apod(self):
        result = self.invoke('apod', '-s', '--date', '2024-01-01')
        self.assertIn('Image saved', result.output)
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
        self.assertIn('Copyright', result.output)
        self.assertEqual(result.exit_code, 0)

    @patch('requests.get')
    def test_api_limit_exceeded(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 429
        mock_get.return_value = mock_response

        result = self.invoke('apod')
        self.assertIn('Too many requests', result.output)
        self.assertEqual(result.exit_code, 1)

    @patch('requests.get')
    def test_response_with_unknown_status_code(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        result = self.invoke('apod')
        self.assertIn('ATTENTION', result.output)
        self.assertEqual(result.exit_code, 1)
