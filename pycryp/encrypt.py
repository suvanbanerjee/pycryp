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
    kdf = PBKDF2HMAC(
        algorithm,
        length=length,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    return f.encrypt(message)