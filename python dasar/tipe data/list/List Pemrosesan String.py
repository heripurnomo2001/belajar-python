# List Pemrosesan String

'''
Tantangan List Pemrosesan String:

Buatlah sebuah program Python yang mengandung sebuah list dengan
nama kata_kalimat yang berisi beberapa kata atau kalimat. Buatlah
fungsi gabung_kata yang menerima list tersebut sebagai argumen dan
mengembalikan sebuah string yang merupakan hasil gabungan dari
semua kata atau kalimat dalam list tersebut, dipisahkan oleh spasi.
'''

# Input list kata_kalimat
kata_kalimat = ["Saya", "sedang", "belajar", "Python"]

# Fungsi gabung_kata untuk menggabungkan kata_kalimat
def gabung_kata(kata_list):
    return ' '.join(kata_list)

# Memanggil fungsi gabung_kata dan menampilkan hasilnya
hasil_gabung = gabung_kata(kata_kalimat)
print("Hasil gabungan kata_kalimat:", hasil_gabung)
