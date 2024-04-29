# PROGRAM KECIL : DAFTAR TEMAN

from colorama import Fore, Back, Style

'''
Tantangan:
Buatlah program yang meminta pengguna untuk memasukkan daftar nama
teman-teman mereka. Setelah itu, program harus melakukan hal berikut:

Menampilkan jumlah teman dalam daftar.
Menampilkan daftar teman-teman secara terurut secara alfabetis.
Meminta pengguna untuk memasukkan nama seorang teman dan program
harus menampilkan apakah teman tersebut ada di dalam daftar atau tidak.
Anda dapat menggunakan metode dan perintah yang telah kita bahas
sebelumnya untuk menyelesaikan tantangan ini. Selamat mencoba! Jika Anda
memiliki pertanyaan, jangan ragu untuk bertanya.
'''

def input_teman():
    nama_teman = input("Masukkan nama temanmu: ")
    if nama_teman.strip(): # nama teman tidak kosong
        temans.append(nama_teman)
    else:
        print("Input nama teman tidak boleh kosong!")
        

def cari_temans():
    cari_teman = input("Mencari nama temanmu, masukkan nama: ")
    if cari_teman.strip(): # jima nama teman tidak kosong
        if cari_teman in temans:
            berita = f"Nama teman anda: {cari_teman} ADA dalam daftar list."
        else:
            berita = f"Nama teman anda: {cari_teman} TIDAK ADA dalam daftar list."
        return berita
    else:
        print("Input nama teman tidak boleh kosong!")

def confirm_lanjut(isi_confirm):
    while True:
        confirm = input(Fore.CYAN + isi_confirm)
        print(Style.RESET_ALL)
        
        if confirm.lower() in 'yn':
            return confirm.lower()
        else:
            print(Fore.RED + "\nConfirm yang anda masukkan tidak valid. Tekah 'y' atau 'n', lanjut atau keluar aplikasi.")
            
temans = []
while True:

    # Input temans
    input_teman()

    # Confirm lanjut input atau keluar
    isi_confirm = "\nApakah ingin memasukkan data teman lagi? Tekan 'y' atau 'n' untuk lanjut atau keluar aplikasi."
    confirm = confirm_lanjut(isi_confirm)
    if confirm == 'n':
        break


jumlah_teman = len(temans)
print("Jumlah temanmu adalah: ", jumlah_teman)
print("Berikut ini nama-nama teman-temanmu sesuai urutan abjad: ")
temans = temans.sort()
for teman in (temans):
    print(teman)


while True:
    berita = cari_temans()
    print (berita)
    input("\nTekan Enter untuk melanjutkan...")

    # Confirm lanjut input atau keluar
    isi_confirm = "\nApakah ingin mencari nama teman lagi? Tekan 'y' atau 'n' untuk lanjut atau keluar aplikasi."
    confirm = confirm_lanjut(isi_confirm)
    if confirm == 'n':
        break
    
    
