import unittest
import pycryp

class EncryptTest(unittest.TestCase):
    def test_decrypt(self):
        message = b"gAAAAABl6tKMHTOnvP2O0pGx1WutCqbg-4EeDi5YL2JvA64RK3DJgsyp4QTSzUy8igdt9x1HWiJXdmu5-fG_-obcJwDykXQLrQ=="
        password = "password"
        iterations = 100000
        salt = b''
        length = 32

        decrypted_message = pycryp.decrypt(message, password, salt, iterations, length)

        self.assertIsNotNone(decrypted_message)
        self.assertNotEqual(decrypted_message, message)

if __name__ == '__main__':
    unittest.main()