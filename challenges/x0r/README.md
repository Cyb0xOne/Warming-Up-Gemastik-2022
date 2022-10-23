### Challenge Information


| Variable       | Value        |
| :------------- | :----------- |
| Challenge Name | x0r          |
| Category       | Cryptography |
| Points         | 200          |
| Difficulty     | Easy         |

### Description

Disajikan dua buah file, yaitu

* [x0r3d.py](x0r3d.py) sebagai encryptor
* [x0r3d_chiper.txt](x0r3d_chiper.txt) sebagai ciphertext

### Summary

[x0r3d.py](x0r3d.py) berisi kode dengan fungsi `encrypt(plain)`

```python
# /usr/bin/python3
from base64 import b64encode, b64decode


def encrypt(plain):
    key = "n0k3y"
    cipher = ""
    for c, i in enumerate(plain):
        cipher += chr(ord(i) ^ ord(key[c % 5]))

    print(b64encode(cipher.encode()))
```

### Solution

Dari kode di atas, dapat dilihat bahwa `key` yang digunakan adalah `n0k3y`.
Dengan demikian, dapat dilakukan dekripsi dengan cara melakukan operasi `xor` antara `cipher` dengan `key` yang diketahui.
Maka dapat diperoleh `plain text` yang merupakan flag. Berikut adalah kode untuk mendapatkan flag.

```python
from base64 import b64encode, b64decode

def decrypt(cipher):
    key = "n0k3y"
    plain = ""
    for c, i in enumerate(cipher):
        plain += chr(ord(i) ^ ord(key[c % 5]))

    return plain

with open("x0r3d_chiper.txt", "r") as f:
    cipher = b64decode(f.read()).decode()
    print(decrypt(cipher))
```

### Flag

Setelah mendapatkan `plain text`, maka dapat diperoleh flag.

```
Gemastik2022{yOu_d3crypt_m3}
```
