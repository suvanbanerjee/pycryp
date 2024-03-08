import unittest
import pycryp

class EncryptTest(unittest.TestCase):
    def test_encrypt(self):
        message = b"Hello, World!"
        password = "mysecretpassword"
        salt = b"mysalt"
        iterations = 100000
        length = 32

        encrypted_message = pycryp.encrypt(message, password, salt, iterations, length)

        self.assertIsNotNone(encrypted_message)
        self.assertNotEqual(encrypted_message, message)

if __name__ == '__main__':
    unittest.main()