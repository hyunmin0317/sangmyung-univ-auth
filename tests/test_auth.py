import os
import unittest
from sangmyung_univ_auth import auth


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')

    def test_authenticator(self):
        res = auth(username=self.username, password=self.password)
        self.assertTrue(res.is_auth)
        res = auth(username='username', password='password')
        self.assertFalse(res.is_auth)


if __name__ == '__main__':
    unittest.main()
