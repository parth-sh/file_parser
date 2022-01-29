import unittest
import warnings
from src.handler import decrypt_pdf

class TestHandler(unittest.TestCase):
    '''Test password protected file return in pdf format'''
    PDF_FILE_URL = 'https://tradecred-website-assets.s3.ap-south-1.amazonaws.com/encrypted-asset.pdf'
    PASSWORD = 'PART1998'
    FORMAT = 'pdf'
    
    def test_process(self):
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)

        return_msg, return_flag, return_service = decrypt_pdf(self.PDF_FILE_URL,self.PASSWORD,self.FORMAT)
        print('\n',return_msg, return_flag, return_service)

if __name__ == '__main__':
    unittest.main()
