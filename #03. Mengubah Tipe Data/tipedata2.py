'''
Contoh No.1
merubah tipe data string menjadi integer, float, dan boolean

Perhatian!!
jika ingin mengubah tipe data string menjadi integer dan menjadi float
maka string harus tipe string yang angka bukan yang kalimat
karena jika kalimat akan error seperti ini

contoh = "satu"
print(int(contoh))
ValueError: invalid literal for int() with base 10: 'satu'

yang benar :
'''
contoh = str("10")
integer = int(contoh) + int(contoh)
float_ = float(contoh) + float(2.2)
boolean = bool(contoh)

print("ini adalah string    :",contoh)
print("ini adalah integer   :",integer)
print("ini adalah float     :",float_)
print("ini adalah boolean   :",boolean)