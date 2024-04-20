# Pemisahan dan Penggabungan Nama:

'''

Buat program yang meminta input nama lengkap dari pengguna
(misalnya, "John Doe") dan kemudian memisahkan nama depan dan belakang,
lalu gabungkan kembali dengan format nama belakang di depan dan nama depan
di belakang. Misalnya, "Doe John".
'''

# Fungsi input nama
def input_nama():
    while True:
        nama_lengkap = input("\nMasukkan nama: ")

        # Jika nama kosong
        if nama_lengkap.strip() == '':
            print("Nama tidak boleh kosong!")
            continue # Lanjutkan iterasi berikutnya dalam loop

        # Jika nama tidak kosong
        return nama_lengkap


while True:
    nama = input_nama()
    nama_split = nama.split()
    jumlah_elemen = len(nama_split)
    print(nama_split)

    print('Nama hasil balik: ', end="")
    for i in range(jumlah_elemen - 1, -1, -1):
        print(nama_split[i], end=" ")
    
    
