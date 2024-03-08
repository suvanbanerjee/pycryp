import unittest
import string
from pycryp.passwords import generate_password

class PasswordsTest(unittest.TestCase):
    def test_generate_password_with_all_conditions(self):
        length = 12
        password = generate_password(length, upper=True, lower=True, digits=True, punctuation=True)

        self.assertEqual(len(password), length)
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))
        
    def test_generate_password_with_upper(self):
        length = 12
        password = generate_password(length, upper=True, lower=False, digits=False, punctuation=False)

        self.assertEqual(len(password), length)
        self.assertTrue(any(char.isupper() for char in password))
        self.assertFalse(any(char.islower() for char in password))
        self.assertFalse(any(char.isdigit() for char in password))
        self.assertFalse(any(char in string.punctuation for char in password))

    def test_generate_password_with_lower(self):
        length = 12
        password = generate_password(length, upper=False, lower=True, digits=False, punctuation=False)

        self.assertEqual(len(password), length)
        self.assertFalse(any(char.isupper() for char in password))
        self.assertTrue(any(char.islower() for char in password))
        self.assertFalse(any(char.isdigit() for char in password))
        self.assertFalse(any(char in string.punctuation for char in password))

    def test_generate_password_with_digits(self):
        length = 12
        password = generate_password(length, upper=False, lower=False, digits=True, punctuation=False)

        self.assertEqual(len(password), length)
        self.assertFalse(any(char.isupper() for char in password))
        self.assertFalse(any(char.islower() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertFalse(any(char in string.punctuation for char in password))

    def test_generate_password_with_punctuation(self):
        length = 12
        password = generate_password(length, upper=False, lower=False, digits=False, punctuation=True)

        self.assertEqual(len(password), length)
        self.assertFalse(any(char.isupper() for char in password))
        self.assertFalse(any(char.islower() for char in password))
        self.assertFalse(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

if __name__ == '__main__':
    unittest.main()