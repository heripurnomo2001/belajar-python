# Akses Karakter 'o' dan 'r'
'''
Soal Kedua:
Buatlah sebuah string dengan nilai "Hello World!" dan lakukan hal berikut:
a. Cetak karakter "o" dalam string tersebut menggunakan indeks positif.
b. Cetak karakter "r" dalam string tersebut menggunakan indeks negatif.
'''

# Menyiapakan string
string1 = "Hello World!"
print(f"Akses Karakter 'o' dan 'r' pada String : '{string1}'\n")


# Cetak karakter 'o' dengan indeks positif
indeks1 = 4
indeks2 = 7
print(f"'{string1[indeks1]}' pada urutan ke: {indeks1}")
print(f"'{string1[indeks2]}' pada urutan ke: {indeks2}\n")

indeks3 = -4
# Cetak karakter 'r' dengan indeks positif
print(f"'{string1[indeks3]}' pada urutan ke: {indeks3}\n")

