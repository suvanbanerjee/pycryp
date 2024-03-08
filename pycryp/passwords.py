import random
import string

def generate_password(length: int = 12, upper: bool = True, lower: bool = True, digits: bool = True, punctuation: bool = True) -> str:
    """
    Generates a random password with the specified length and character types.

    Args:
        length (int): The length of the password (default is 12).
        upper (bool): Whether to include uppercase letters (default is True).
        lower (bool): Whether to include lowercase letters (default is True).
        digits (bool): Whether to include digits (default is True).
        punctuation (bool): Whether to include punctuation marks (default is True).

    Returns:
        str: The randomly generated password.
    """
    password = ''
    if upper:
        password += string.ascii_uppercase
    if lower:
        password += string.ascii_lowercase
    if digits:
        password += string.digits
    if punctuation:
        password += string.punctuation
    return ''.join(random.sample(password, length))