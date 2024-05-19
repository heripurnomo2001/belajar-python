# MODIFIKASI LIST

'''
Tantangan Modifikasi List:
Diberikan sebuah list dengan nama buah yang berisi nama-nama
buah seperti "apel", "jeruk", "pisang", "mangga", dan "anggur".
Modifikasilah list tersebut sehingga elemen kedua diganti menjadi
"melon" dan elemen kelima dihapus.
Tampilkan list buah setelah dimodifikasi.
'''

# List nama-nama buah
nama_buah = ["apel","jeruk","pisang","mangga","anggur"]

# Menampilkan List sebelum diubah dan dihapus elemennya
print("\nIni adalah List sebelum dimodifikasi : ", nama_buah)

# Modifikasi elemen ke [1] diganti "melon"
nama_buah[1] = "melon"

# Modifikasi lemen ke [5] dihapus
nama_buah.pop(4)

# Menampilkan List setelah diubah dan dihapus elemennya
print("\nIni adalah List setelah dimodifikasi : ", nama_buah)


