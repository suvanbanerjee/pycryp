import os

def generate_salt(length: int = 16) -> bytes:
    """
    Generate a random salt of the specified length.
    
    Parameters:
    - length (int): The length of the salt in bytes. Default is 16.
    
    Returns:
    - bytes: The generated salt.
    """
    return os.urandom(length)