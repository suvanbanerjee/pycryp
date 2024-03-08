import unittest
from pycryp.salt import generate_salt

class SaltTest(unittest.TestCase):
    def test_generate_salt(self):
        length = 16
        salt = generate_salt(length)

        self.assertEqual(len(salt), length)

if __name__ == '__main__':
    unittest.main()