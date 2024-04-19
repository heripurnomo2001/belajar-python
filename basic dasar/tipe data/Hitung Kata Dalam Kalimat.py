# Hitung Kata Dalam Kalimat

'''
Buatlah sebuah program yang meminta pengguna untuk memasukkan sebuah kalimat,
lalu pisahkan kata-kata dalam kalimat tersebut menggunakan fungsi split().
Setelah itu, tampilkan jumlah kata dalam kalimat tersebut.
'''

def input_kalimat():
    while True:
        kalimat = input("Masukkan sebuah kalimat: ")
        if kalimat.strip(): # Jika kalimat tidak kosong
            return kalimat

        # Jika kalimat kosong setelah distrip
        print("Kalimat tidak boleh kosong!")


def confirm_lanjut():
    while True:
        confirm = input("Mau mencoba lagi? (y/n):").strip().lower()
        if confirm in 'ny':
            print("\n")
            return confirm

        if confirm != 'y':
            print("Masukkan hanya 'y' atau 'n' untuk melanjutkan atau keluar!")
                        
while True:
    kalimat = input_kalimat()
    list_kalimat = kalimat.split()
    jumlah_kata = len(list_kalimat)

    # Cetak jumlah kata
    print("Jumlah kata dalam kalimat: ", jumlah_kata, "\n")

    # Confirm akan keluar aplikasi
    confirm = confirm_lanjut()
    if confirm == 'n':
        print("Terima kasih, sampai jumpa.")
        break
    

    

          
    
