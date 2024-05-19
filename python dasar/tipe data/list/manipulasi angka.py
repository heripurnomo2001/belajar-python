# List Manipulasi Angka

'''
Tantangan List Manipulasi Angka:

Buatlah sebuah program Python yang melakukan manipulasi terhadap sebuah list angka. Program tersebut harus dapat melakukan hal berikut:

Menghapus semua angka genap dari list.
Menambahkan angka 10 pada akhir list.
Menggandakan setiap angka yang tersisa dalam list.
'''

# List angka awal
angka_list = [1, 2, 3, 4, 5]

# Fungsi manipulasi_list untuk melakukan manipulasi pada angka_list
def manipulasi_list(angka_list):
    # Menghapus angka genap dari list
    angka_list = [angka for angka in angka_list if angka % 2 != 0]
    # Menambahkan angka 10 pada akhir list
    angka_list.append(10)
    # Menggandakan setiap angka yang tersisa dalam list
    angka_list = [angka * 2 for angka in angka_list]
    return angka_list

# Memanggil fungsi manipulasi_list dan menampilkan hasilnya
hasil_manipulasi = manipulasi_list(angka_list)
print("Hasil manipulasi angka_list:", hasil_manipulasi)
