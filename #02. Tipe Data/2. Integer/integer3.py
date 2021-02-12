'''
lalu kalau di gabung?
'''
number = 2,4,6,8,10

print("di gabung dengan cara memakai format string, dan hasilnya malah di jumlah:")
a2 = number[0]
a3 = number[1]
print(a2 + a3)
print(30*"=")

'''
masalah nya adalah, kalau integer di gabung dengan cara yang sama seperti string memakai plus(+)
maka yang terjadi adalah angka kita akan otomatis di jumlah

lalu gimana dong?
gampang kok, kita hanya perlu ganti tanda plus(+) menjadi koma(,)
'''
print("di gabung dengan cara memakai format string, dan hasilnya tidak di jumlah:")
b1 = number[0]
b2 = number[1]
print(b1,b2)


'''
yah gak terlalu panjang sih kyk string, intinya kalau mau menggabungkan integer dan integer
harus menggunakan tanda koma(,)

digabung dan dijumlah beda loh yah.

kalau digabung itu kita ambil angka 2 dan angka 4 lalu kita gabungkan [dengan memakai koma(,)]
di dalam syntax yang sama atau berbeda
maka hasil nya adalah 2 4, contoh:

b1 = number[0]
b2 = number[1]
print(b1, b2)

Beda kalau djumlah, misal kita ambil angka 2 lalu angka 4 kita jumlah [dengan memakai plus(+)]
di dalam syntax yang sama atau berbeda
maka hasil nya adalah 6, contoh :

a2 = number[0]
a3 = number[1]
print(a2 + a3)
'''