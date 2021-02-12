'''
operasi matematika format:

tambah                          : +
kurang                          : -
kali                            : *
bagi                            : /
bilangan bulat                  : //
modulus(sisa dari pembagian)    : %
pangkat                         : **
kurang dari                     : <
lebih dari                      : >
kurang dari sama dengan         : <=
lebih dari sama dengan          : >=
sama dengan dari                : ==
tidak sama dengan dari          : !=
'''

# tambah
tambah = 3+3
# bisa memakai float
tambah_float = 3+3.0

# kurang
kurang = 9-3
# bisa memakai float
kurang_float = 9-3.0

# kali
kali = 3*3
# bisa memakai float
kali_float = 3*3.0

# pembagian float
bagi_float = 3/3
# hasil nya akan tetap float

# pembagian bulat
bagi_bulat = 3//3
# hasil nya menjadi bilangan bulat

# modulus = sisa dari pembagian
modulus = 10%3
# bisa memakai float
modulus_float = 10%3.0

# penggunaan kurung
salah = 3+2*4
'''
yang duluan di eksekusi adalah 3+2
perlu di ingat karena berbahaya jika memprogram aplikasi lalu menggunakan ini dan hasil nya berbeda
'''
benar = (3+2)*4
'''
yang seperti ini benar, karena semuanya di eksekusi.

Berlaku untuk semuanya, dari tambah, kurang, kali, dan bagi
'''

# pangkat dengan menggunakan double stars(**)
pangkat = 3**3
# bisa memakai float
pangkat_float = 3**3.0

#===================================================================================================================
'''
Assigment
'''
a = 5
b = 3
c = 4.0

# penjumlahan
d = a + b
# pengurangan
e = a - b
# perkalian
f = a * b
# pembagian
g = a / b

# contoh untuk hasil eksekusi tambah dan kali
h = (a+b)*c
print(h)