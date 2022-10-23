### Challenge Information

| Variable       | Value           |
|----------------|-----------------|
| Challenge Name | Encoder-Decoder |
| Category       | Cryptography    |
| Points         | 200             |
| Difficulty     | Easy            |

### Description
Disajikan dua buah berkas, yaitu
* [jatim-enc.py](jatim-enc.py) sebagai encryptor
* [encrypted.txt](encrypted.txt) sebagai ciphertext

### Summary
[jatim-enc.py](jatim-enc.py) berisi kode dengan fungsi `encrypt(plain)`
```python
#!usr/bin/python3

def encrypt(plaintext):
    plaintext = plaintext[::-1]
    ciphertext = ""
    for i in plaintext:
        copy = "X" * ((ord(i) ^ 0x50) + 9)
        copy += "-"
        ciphertext += copy
    return ciphertext
```
Penjelasan kode di atas:
* `plaintext = plaintext[::-1]` merupakan operasi `reverse` pada `plaintext`
* `ciphertext = ""` merupakan variabel yang akan menyimpan hasil enkripsi
* `for i in plaintext:` merupakan perulangan untuk setiap karakter pada `plaintext`
* `copy = "X" * ((ord(i) ^ 0x50) + 9)` merupakan operasi `xor` antara karakter pada `plaintext` dengan hexadesimal `0x50` kemudian ditambah `9` dan diulangi sebanyak hasil operasi tersebut. Yang nantinya karakter `X` akan diulang sebanyak hasil operasi tersebut.
* Misal, jika hasil operasi `xor` adalah 41. Maka karakter `X` akan dikalikan sebanyak (41 + 9). Sampai sini pahamkan? Okay lanjut!
* `copy += "-"` merupakan operasi penambahan `-` pada setiap karakter pada `ciphertext`, nantinya karakter `-` akan dijadikan sebagai pemisah antara jumlah karakter `X` yang sudah dikalikan dengan (_N_ + 9), dimana _N_ adalah hasil operasi `xor`
* `ciphertext += copy` merupakan operasi penambahan `copy` pada `ciphertext`
* `return ciphertext` merupakan operasi pengembalian nilai `ciphertext`

### Solution 
Dari kode di atas, kita bisa mengetahui algoritma yang digunakan untuk melakukan enkripsi. Pada algoritma tersebut, terdapat operasi `reverse` pada `plaintext`, kemudian dilakukan operasi `xor` antara karakter pada `plaintext` dengan hexadesimal `0x50`. Setelah itu, karakter `X` akan diulang sebanyak hasil operasi `xor` tersebut. Kemudian, karakter `-` akan dijadikan sebagai pemisah antara jumlah karakter `X` yang sudah dikalikan dengan (_N_ + 9), dimana _N_ adalah hasil operasi `xor`.

Dengan demikian, dapat dilakukan dekripsi dengan cara melakukan operasi `xor` antara `cipher` dengan hexadesimal `0x50` kemudian melakukan operasi `reverse` pada hasil dekripsi. Maka dapat diperoleh `plain text` yang merupakan flag. Berikut adalah kode untuk mendapatkan flag.
```python
#!usr/bin/python3

def decrypt(ciphertext):
    ciphertext = ciphertext.split("-")
    ciphertext = ciphertext[:-1]
    plaintext = ""
    for i in ciphertext:
        plaintext = chr((len(i) - 9) ^ 0x50)
    plaintext = plaintext[::-1]
    return plaintext
```
Penjelasan kode di atas:
* `ciphertext = ciphertext.split("-")` merupakan operasi pemisahan antara karakter `-` pada `ciphertext`
* `plaintext = ""` merupakan variabel yang akan menyimpan hasil dekripsi
* `for i in ciphertext:` merupakan perulangan untuk setiap karakter pada `ciphertext`
* `plaintext = chr((len(i) - 9) ^ 0x50)` merupakan operasi `xor` antara jumlah karakter pada `ciphertext` dengan hexadesimal `0x50` kemudian dikurangi `9`
* `plaintext = plaintext[::-1]` merupakan operasi `reverse` pada `plaintext`
* `return plaintext` merupakan operasi pengembalian nilai `plaintext`

### Flag
Setelah membuat kode untuk mendekripsi ciphertext, lakukan dekripsi pada [encrypted.txt](encrypted.txt) dan dapatkan flag.
```python
#!usr/bin/python3

def decrypt(ciphertext):
    ciphertext = ciphertext.split("-")
    ciphertext = ciphertext[:-1]
    plaintext = ""
    for i in ciphertext:
        plaintext += chr((len(i) - 9) ^ 0x50)
    plaintext = plaintext[::-1]
    return plaintext

with open("encrypted.txt", "r") as f:
    ciphertext = f.read()
    print(decrypt(ciphertext))
```
Maka akan diperoleh flag sebagai berikut.
```
Gemastik2022{tHanKs_f0r_f1nd1ng_m3}
```