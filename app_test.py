import unittest
from app import Twitter
import requests

class classTwitter(unittest.TestCase):

    def setUp(self):
        self.Twitter = Twitter()

    def test_index(self):
        result = requests.get('http://localhost:5000/')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
