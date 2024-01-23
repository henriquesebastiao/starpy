import os
from os import getenv

from .test_base import CliUnitTest, check_result_error


class ApodTest(CliUnitTest):
    def test_return_with_remaining_option_of_apod(self):
        print('\n' + '>>>>> ' + getenv('NASA_API_KEY', 'DEMO_KEY'))
        result = self.invoke('apod', '-r')
        if result.exit_code == 0:
            self.assertIn('Remain', result.output)
        check_result_error(result)

    def test_return_without_remaining_option_of_apod(self):
        result = self.invoke('apod')
        if result.exit_code == 0:
            self.assertNotIn('Remain', result.output)
        check_result_error(result)

    def test_return_with_save_image_option_of_apod(self):
        result = self.invoke('apod', '-s')
        if result.exit_code == 0:
            self.assertIn('Image saved', result.output)
            os.remove('image.jpg')
        check_result_error(result)
