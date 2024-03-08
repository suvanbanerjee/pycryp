# pycryp
This is a simple python library for encryption and decryption of messages using the AES algorithm. It is designed to be simple and easy to use.

## Installation
```
pip install pycryp
```

## Usage

### Encryption
```python
import pycryp
message = "Hello, World!"
password = "password"
print(pycryp.encrypt(message, password))
```
It also has an optional parameters for salt, iterations and length of the key. The default values are salt = NULL, iterations = 100000, key_length = 32

Example:
```python
import pycryp
message = "Hello, World!"
password = "password"
salt = b"someSALT" # Must be a byte string
iterations = 100000
key_length = 32
print(pycryp.encrypt(message, password, salt, iterations, key_length))
```

### Decryption
```python
import pycryp
encrypted_message = "WhatevrEncryptedMessage"
password = "password"
print(pycryp.decrypt(encrypted_message, password))
```
It also has an optional parameters for salt, iterations and length of the key. The default values are salt = NULL, iterations = 100000, key_length = 32

Example:
```python
import pycryp
encrypted_message = "WhatevrEncryptedMessage"
password = "password"
salt = b"someSALT" # Must be a byte string
iterations = 100000
key_length = 32
print(pycryp.decrypt(encrypted_message, password, salt, iterations, key_length))
```

### Note:
 The salt, iterations and key_length must be the same for both encryption and decryption. If you change the values for encryption, you must also change the values for decryption.

### Generating Password
```python
import pycryp
print(pycryp.generate_password())
```
It also has an optional parameter for length, Upper case, Lower case, Digits and Special characters. The default values are length = 16, upper = True, lower = True, digits = True, special = True

Example:
```python
import pycryp
print(pycryp.generate_password(16, True, True, True, True))
``` 

### Generating Salt
```python
import pycryp
print(pycryp.generate_salt())
```
It also has an optional parameter for length. The default value is length = 16

Example:
```python
import pycryp
print(pycryp.generate_salt(16))
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details