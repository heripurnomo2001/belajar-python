# Pisahkan Tanggal Dengan Split()

'''
Buatlah sebuah program yang meminta pengguna untuk memasukkan sebuah tanggal
dalam format "DD/MM/YYYY", lalu pisahkan tanggal, bulan, dan tahun menggunakan
fungsi split(). Kemudian, tampilkan tanggal, bulan, dan tahun secara terpisah.
'''

# Panggil module datetime
from datetime import datetime


def input_tgstring():
    while True:
        try:
            tgstring = input("\nMasukkan tanggal (Format: DD/MM/YYYY : Contoh: 19/04/2024): ")

            # Validasi input tanggal kosong
            if tgstring.strip() == "":
                print("Input tanggal tidak boleh kosong!")
                continue # Lanjutkan iterasi berikutnya dalam loop

            # Jika tanggal tidak kosong            
            tanggal = datetime.strptime(tgstring,'%d/%m/%Y').date()
            list_tgstring = tgstring.split('/')
            hari = list_tgstring[0]
            bulan = list_tgstring[1]
            tahun = list_tgstring[2]                               
           
            return hari, bulan, tahun
            
        except ValueError as e:
            print("Input tanggal tidak valid! Pastikan formatnya = DD/MM/YYYY. Kesalahan: ", e)

def confirm_lanjut():
    while True:
        confirm = input("\nMau melakukan split tanggal lagi? Masukkan 'y' atau 'n' untuk lanjut atau keluar: ").strip().lower()
        # Jika confirm valid
        if confirm in 'ny':
            return confirm

        # Jika confirm tidak valid
        print("Confirm cukup ketikkan 'y' atau 'n', lanjut atau keluar aplikasi.")
        

while True:
    # Input tanggal
    hari, bulan, tahun = input_tgstring()    
    print("Tanggal: ", hari)
    print("Bulan: ", bulan)
    print("Tahun: ", tahun)

    # Confirm lanjut atau keluar
    confirm = confirm_lanjut()
    if confirm == 'n':  # Jika memlilih keluar 
        print("Terima kasih, sampai jumpa.")
        break
        
