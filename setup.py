from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'package to encrypt and decrypt messages using AES '

setup(
    name="pycryp",
    version=VERSION,
    author="Suvan Banerjee",
    author_email="<banerjeesuvan@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['cryptography'],
    keywords=['python', 'aes', 'encryption', 'decryption', 'aes-256-cbc'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python 3",
        "License ::  MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)