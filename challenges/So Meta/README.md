### Challenge Information

| Variable       | Value     |
|----------------|-----------|
| Challenge Name | So Meta   |
| Category       | Forensics |
| Points         | 250       |
| Difficulty     | Easy      |

### Description
Disajikan sebuah file berekstensi `.png` yang berisi gambar berikut:

![](logo.png)

Resource file: [logo.png](logo.png)

### Solution
Ya, seperti nama _challenge_-nya mengandung kata `meta`, maka kita harus mencari informasi tambahan dari file tersebut. Dengan menggunakan perintah `exiftool` pada file tersebut, dapat diperoleh informasi tambahan sebagai berikut:
```
$ exiftool logo.png
ExifTool Version Number         : 12.42
File Name                       : logo.png
Directory                       : .
File Size                       : 34 kB
File Modification Date/Time     : 2022:10:22 20:13:47+07:00
File Access Date/Time           : 2022:10:24 08:19:10+07:00
File Inode Change Date/Time     : 2022:10:24 08:18:47+07:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 510
Image Height                    : 60
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Camera Serial Number            : Gemastik2022{n4s1_J4gO3nG}
Image Size                      : 510x60
Megapixels                      : 0.031
```

### Flag
Flag terdapat pada bagian `Camera Serial Number` yaitu `Gemastik2022{n4s1_J4gO3nG}`.