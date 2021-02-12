'''
baik, jika ada yang belum paham kita ganti contoh nya dengan kalimat.

oke sebelum itu, dalam boolean selain angka / integer
kita juga bisa memasukkan kalimat / string

contoh:
'''

hewan_karnivora = "harimau","singa","macan tutul","kucing"
hewan_herbivora = "sapi", "kerbau", "burung gereja", "monyet"

contoh1 = "harimau" in hewan_herbivora
print("Apakah di dalam hewan herbivora ada harimau?")
print("Jawab :",contoh1)

contoh2 = "singa" in hewan_karnivora
print("Apakah di dalam hewan karnivora ada singa?")
print("Jawab :",contoh2)

'''
sedikit penjelasan.

pasti beberapa ada yang sadar atau bahkan semuanya, karena ada huruf asing yaitu in
nah apa artinya in?
kita translatekan saja ke dalam bahasa indonesia:

bahasa inggris      = in
bahasa indonesia    = di

oke sudah paham kan arti dari in?.

Sekarang kita kembali lagi pada file boolean1 di baris ke 21
masih ingat dengan pertanyaan guru tadi kan?
kita ganti saja begini

guru bertanya: "Benar atau Salah, jika di dalam hewan herbivora ada harimau?"
jawaban kita: "Salah!"

Salah = False

'''