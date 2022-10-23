#!usr/bin/python3

def encrypt(plaintext):
    plaintext = plaintext[::-1]
    ciphertext = ""
    for i in plaintext:
        copy = "X" * ((ord(i) ^ 0x50) + 9)
        copy += "-"
        ciphertext += copy
    return ciphertext


def decrypt(ciphertext):
    ciphertext = ciphertext.split("-")
    ciphertext.pop()
    plaintext = ""
    for i in ciphertext:
        plaintext += chr((len(i) - 9) ^ 0x50)
    return plaintext[::-1]


def load_cipher():
    with open('encrypted.txt') as f:
        return f.read()

print(decrypt(load_cipher()))