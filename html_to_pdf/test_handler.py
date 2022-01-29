import re
import unittest
import warnings

from src.handler import html_to_pdf


class TestHandler(unittest.TestCase):
    url = "www.google.com"

    def test_process(self):
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)

        return_msg, return_flag = html_to_pdf(self.url)
        print('\n', return_msg, return_flag)


if __name__ == '__main__':
    unittest.main()
