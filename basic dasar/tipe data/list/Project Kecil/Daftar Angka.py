# LIST ANGKA

# Import Modul / Library
from colorama import Style, Fore, Back 

'''
Buatlah program yang meminta pengguna untuk memasukkan daftar
angka bulat. Setelah itu, program harus melakukan hal berikut:

Menampilkan jumlah angka dalam daftar.
Menampilkan angka terkecil dan angka terbesar dalam daftar.
Menghitung jumlah total dari semua angka dalam daftar.
Menampilkan daftar angka yang hanya terdiri dari angka genap.
Menampilkan daftar angka yang hanya terdiri dari angka ganjil.

Anda dapat menggunakan metode dan perintah yang telah kita
bahas sebelumnya, seperti penggunaan loop, kondisional, dan
metode list, untuk menyelesaikan tantangan ini. Selamat mencoba!
Jika Anda memiliki pertanyaan, jangan ragu untuk bertanya.
'''


def input_angka():
    bilangan = input("Masukkan bilangan bulat: ")
    if bilangan.strip():
        try:
            bilangan = int(bilangan)
            
            # Tambahkan list bilangans dengan bilangan
            bilangans.append(bilangan)
            
        except ValueError:
            print(Fore.RED + "Input harus berupa bilangan bulat!")
    else:
        print(Fore.RED + "Input angka tidak boleh kosong!")

def confirm_lanjut():
    confirm = input(Fore.CYAN + "\nMau menambahkan bilangan ke dalam list bilangans lagi? Tekan 'y' atau 'n' untuk lanjut atau keluar program.")
    print(Style.RESET_ALL)
    if confirm in 'yn':
        return confirm
    else:
        print(Fore.RED + "\nConfirm yang ada masukkan tidak valid! Tekan 'y' atau 'n', untuk lanjut atau keluar program.")
        

bilangans = []


while True:

    input_angka()

    # Confirm lanjut
    confirm = confirm_lanjut()
    if confirm == 'n':
        break

    
# Menghitung jumlah, min dan max
jumlah_bilangan = len(bilangans)
bilangan_max = max(bilangans)
bilangan_min = min(bilangans)
jumlah_total = sum(bilangans)


# Buat List bilangan genap dan list bilangan ganjil
bil_genap = []
bil_ganjil = []
for bilangan in bilangans:
    if bilangan % 2 == 0:
        bil_genap.append(bilangan)
    else:
        bil_ganjil.append(bilangan)

# Tampilkan hasil
print("Jumlah bilangan adalah: ", jumlah_bilangan)
print("Bilangan terbesar adalah: ", bilangan_max)
print("Bilangan terkecil adalah: ", bilangan_min)
print("Jumlah_total bilangan adalah: ", jumlah_total)
print("List bilangan genap: ", bil_genap)
print("List bilangan ganjil: ", bil_ganjil)


# Tunda sebelum keluar program
input("Tekan Enter untuk keluar program...")

    
    
