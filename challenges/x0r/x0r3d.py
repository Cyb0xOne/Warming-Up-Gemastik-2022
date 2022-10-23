# /usr/bin/python3
from base64 import b64encode, b64decode


def encrypt(plain):
    key = "n0k3y"
    cipher = ""
    for c, i in enumerate(plain):
        cipher += chr(ord(i) ^ ord(key[c % 5]))

    print(b64encode(cipher.encode()))


def decrypt(chiper: str):
    key = 'n0k3y'
    plaintext = ''
    for c, i in enumerate(b64decode(chiper).decode()):
        plaintext += chr(ord(i) ^ ord(key[c % 5]))
    return plaintext


def load_cipher():
    with open('x0r3d_chiper.txt') as f:
        return f.read()


if __name__ == "__main__":
    print(decrypt(load_cipher()))
