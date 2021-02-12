'''
nah jadi bisa bikin yang seperti ini
'''
text = "PISANG GORENG"
c1 = text[0:5]
print("saat belum paham:")
print(c1)

'''
"loh kok hasil nya PISAN sih ?"
pasti ada yang kyk gini.

kalian masih ingat dengan format nya kan ?

| P | I | S | A | N | G |   | G | O | R | E  | N  | G  |
|   |   |   |   |   |   |   |   |   |   |    |    |    |
0   1   2   3   4   5   6   7   8   9   10   11   12   13

kalau kita asumsikan
| P | I | S | A | N | G |   | G | O | R | E  | N  | G  |
|   |   |   |   |   |   |   |   |   |   |    |    |    |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

lah kok kayak gitu, padahal asumsi nya benar loh bahwa G itu sama dengan 5
tapi kok hanya muncul cuma PISAN sih :'(

oke, mari berfikir sejenak . . .

setelah kalian berfikir lama
lalu dalam benak kalian akan berkata seperti ini saat menemukan solusinya

" wah, saya tau!! kenapa hanya muncul PISAN saat saya ambil format 0:5...
ternyata asumsi saya salah, seharus nya kalau di lihat dari format aslinya
yang harus saya ambil adalah angka 6 bukan 5, karena sebelum angka 6 itu adalah G.
Jadi dengan begini saya sudah bisa membuat kalimat PISANG dengan sempurna"

jika ada yang berfikir begitu, yap kalian pintar.. 
sebenarnya asumsi di atas itu benar tidak salah sama sekali
hanya saja kita masih belum mengerti cara menggunakan nya.

oke, jadi kita bisa nih buat kalimat pisang nya dengan cara
'''
c2 = text[0:6]
print("\nsaat sudah paham:")
print(c2)

'''
atau kita bisa menggunakan cara ini yang lebih mudah lagi dari yang di atas
'''
print("\ntrik mudah:")
c3 = text[:6]
print(c3)

c4 = text[7:]
print(c4)

'''
artinya kita akan mengambil kalimat sebelum 6 yaitu PISANG.
atau kita bisa mengambil kalimat sesudah 7 yaitu GORENG

nah pasti ada yg protes nih
"gimana sih, ini padahal mudah banget loh, kok sampai harus jelaskan yang di atas sih
susah - susah ngetik nya ternyata ada yang lebih enak"

aduh jangan lah di protes :'(
kasian aku:'v

untuk contoh di atas saya jelaskan karena biar gk bingung format nya bagaimana
lalu, kok 0 = P dan 5 = G saat di ambil 0:5 jadi nya malah PISAN, kenapa? padahal format nya benar
sedangkan saat di ambil cuma 0 doang hasil nya P, dan saat di ambil cuma 5 doang hasil nya G
waktu di satukan hasil nya malah jadi PISAN.

nah bingung kan?, inilah guna nya saya menjelaskan panjang lebar di atas untuk mengatasi kebingungan kalian.


Yang terakhir, kita bisa bermain - main seperti ini
'''
print("\ndi gunakan untuk mengambil huruf tertentu:")
c5 = text[0]
c6 = text[2]
print(c5 + c6)

print("\nmenambahkan text:")
d1 = text[0]
d2 = text[2]
print("hadeuh pengen beli " + d1 + d2 + "5, tapi gaji kurang :'(")

print("\nmenambah jumlah text dengan cara memakai *:")
d2 = text[8]
print(d2*3 + " aza ya kan")

'''
berkreasilah dengan imajinasi kalian masing - masing
'''