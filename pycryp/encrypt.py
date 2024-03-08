# Copyright (c) 2024 Suvan Banerjee <banerjeesuvan@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

'''
Imports
'''
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

def encrypt(message: bytes, password: str, salt: bytes = b'', iterations: int = 100000, length: int = 32, algorithm: hashes.HashAlgorithm = hashes.SHA256()) -> bytes:
    """
    Encrypts a message using a password and optional salt, iterations, length, and algorithm.

    Args:
        message (bytes): The message to encrypt.
        password (str): The password used for encryption.
        salt (bytes, optional): The salt used for key derivation. Defaults to b''.
        iterations (int, optional): The number of iterations for key derivation. Defaults to 100000.
        length (int, optional): The length of the derived key. Defaults to 32.
        algorithm (cryptography.hazmat.primitives.hashes.HashAlgorithm, optional): The hash algorithm used for key derivation. Defaults to hashes.SHA256().
    
    Returns:
        bytes: The encrypted message.
    """
    password = password.encode()

    #Key Derivation Function
    kdf = PBKDF2HMAC(
        algorithm,
        length=length,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    #Generating the key
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    
    return f.encrypt(message)