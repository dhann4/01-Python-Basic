'''
-> bagaimana jika hari jum'at?, masalahnya kan hari jum'at ada tanda kutip atas nya dan untuk bahasa inggris juga
terdapat banyak tanda kutip nya seperti :
don't, doesn't, isn't dan lain sebagainya

-> sedangkan untuk string harus menggunakan tanda kutip untuk mengatasi agar syntax nya tidak error.
Jika tanda kutip nya seperti

contoh1 = tutorial string
print(contoh1)

yang muncul di terminal bukan tutorial string tapi

    contoh1 = tutorial string
                          ^
SyntaxError: invalid syntax

akan error, karena tidak boleh ada identasi nya.

-> lalu kalau tidak boleh ada identasi nya apakah dengan begini bisa?
contoh:

contoh2 = tutorialstring
print(contoh2)

tetap tidak bisa. yang muncul di terminal adalah

    contoh2 = tutorialstring
NameError: name 'tutorialstring' is not defined

-> ohh kalau begitu bagaimana jika begini?

contoh3 = 'jalan - jalan di hari jum'at'
print(contoh3)

yap, sayang sekali masih tidak bisa juga akan ada error jika di jalankan di terminal hasil nya adalah

    contoh3 = 'jalan - jalan di hari jum'at'
                                         ^
SyntaxError: invalid syntax

-> karena at itu tidak ada tipe data nya sedangkan yang di baca hanya 'jalan - jalan di hari jum'
sedangkan untuk 'at' nya tidak di baca.

-> hadeuh... caranya gimana dong?
simpel doang kok kita hanya perlu mengganti yang awal nya tanda kutip satu(')
kita ganti jadi tanda double kutip (") atau kita bisa menggunakan slash (\).

contoh nya:

text2 = "jalan - jalan di hari jum'at"
print(text2)

text3 = 'jalan - jalan di hari jum\'at'
print(text3)

hasil dari kedua trik tersebut adalah
jalan - jalan di hari jum'at
'''
text2 = "jalan - jalan di hari jum'at"
print(text2)
text3 = 'jalan - jalan di hari jum\'at'
print(text3)