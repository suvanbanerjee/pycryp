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