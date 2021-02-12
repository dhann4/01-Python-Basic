'''
ada lagi, yaitu cara mengambil masing - masing huruf
contoh:
'''
text = "pisang goreng"
a = text[0]
print(a)

'''
oke, format nya begini biar gk bingung

dari plus
| P | I | S | A | N | G |   | G | O | R | E  | N  | G  |
|   |   |   |   |   |   |   |   |   |   |    |    |    |
0   1   2   3   4   5   6   7   8   9   10   11   12   13

jika dari minus
| P |  I  |  S  |  A  |  N  |  G  |   | G | O | R | E | N | G |
|   |     |     |     |     |     |   |   |   |   |   |   |   |
0  -14  -13   -12    -11   -10   -9  -8  -7  -6  -5  -3  -2  -1


untuk mengambil masing - masing huruf kita hanya perlu menggunakan
a = text[0] untuk P
'''
# untuk plus
a1 = text[1] # untuk I
print(a1)
a2 = text[2] # untuk S
print(a2)

# untuk minus
b1 = text[-1] # untuk G
print(b1)
b2 = text[-2] # untuk N
print(b2)