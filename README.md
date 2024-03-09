# pycryp
This is a python library for encryption and decryption of messages. It is designed to be simple and easy to use.

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
#b'gAAAAABl6ym8taGz9n254R0nwIQ2nnMJ19LvgTMItPiTJeJYCeysfIarDwGXZRdyw39iOtPxi91QDRGtGIiLTBgZUEHk1_iTGQ=='
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
#gAAAAABl6yoPFjKhjCSJ1cOt68GuYNthZi3Ie9sc7QdMWa0BvaNHGb-mitXhxFNB2kom4vKBGmLcdlN7GCA_0UnGSWOJR_UEUA==
```

### Decryption
```python
import pycryp
encrypted_message = "b'gAAAAABl6ym8taGz9n254R0nwIQ2nnMJ19LvgTMItPiTJeJYCeysfIarDwGXZRdyw39iOtPxi91QDRGtGIiLTBgZUEHk1_iTGQ=='"
password = "password"
print(pycryp.decrypt(encrypted_message, password))
#b'Hello, World!'
```
It also has an optional parameters for salt, iterations and length of the key. The default values are salt = NULL, iterations = 100000, key_length = 32

Example:
```python
import pycryp
encrypted_message = "gAAAAABl6yoPFjKhjCSJ1cOt68GuYNthZi3Ie9sc7QdMWa0BvaNHGb-mitXhxFNB2kom4vKBGmLcdlN7GCA_0UnGSWOJR_UEUA=="
password = "password"
salt = b"someSALT" # Must be a byte string
iterations = 100000
key_length = 32
print(pycryp.decrypt(encrypted_message, password, salt, iterations, key_length))
#b'Hello, World!'
```

### Note:
 The salt, iterations and key_length must be the same for both encryption and decryption. If you change the values for encryption, you must also change the values for decryption.

 Message and password can be a string or a byte string. 

### Generating Password
```python
import pycryp
print(pycryp.generate_password())
#_=?Q.iaA#y$O
```
It also has an optional parameter for length, Upper case, Lower case, Digits and Special characters. The default values are length = 16, upper = True, lower = True, digits = True, special = True

Example:
```python
import pycryp
print(pycryp.generate_password(16, True, True, True, True))
#_=?Q.iaA#y$O
``` 

### Generating Salt
```python
import pycryp
print(pycryp.generate_salt())
#b'\xeeG\xea\x07\xe2\x01\xd58\xc2\x0f\xd8fK\xdb\xc0\x83'
```
It also has an optional parameter for length. The default value is length = 16

Example:
```python
import pycryp
print(pycryp.generate_salt(16))
#b'\xeeG\xea\x07\xe2\x01\xd58\xc2\x0f\xd8fK\xdb\xc0\x83'
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/suvanbanerjee/pycryp/blob/main/LICENSE) file for details