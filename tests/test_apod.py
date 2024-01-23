import os

from .test_base import CliUnitTest, check_result_error


class ApodTest(CliUnitTest):
    def test_return_with_remaining_option_of_apod(self):
        result = self.invoke('apod', '--date 2024-01-01', '-r')
        if result.exit_code == 0:
            print('\n' + result.output)
            self.assertIn('Remain', result.output)
        check_result_error(result)

    def test_return_without_remaining_option_of_apod(self):
        result = self.invoke('apod', '--date 2024-01-01')
        if result.exit_code == 0:
            self.assertNotIn('Remain', result.output)
        check_result_error(result)

    def test_return_with_save_image_option_of_apod(self):
        result = self.invoke('apod', '-s', '--date 2024-01-01')
        if result.exit_code == 0:
            self.assertIn('Image saved', result.output)
            os.remove('image.jpg')
        check_result_error(result)
