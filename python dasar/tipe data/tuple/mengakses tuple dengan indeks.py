# MENGAKSES TUPLE DENGAN INDEKS

import os
from colorama import Style, Fore, Back

# Contoh tuple
nama_buah = 'apel', 'pisang', 'mangga', 'jeruk'
jumlah_elemen = len(nama_buah)
                
# Cetak tuple
print(f"Ini adalah contoh tuple : {nama_buah}")

def confirm_lanjut():
    while True:
        try:
            confirm = input(Fore.CYAN + "\nMau mengakses data lagi? Tekan 'y' atau 'n' untuk melanjutkan atau keluar program.")
            confirm = confirm.lower()
            print(Style.RESET_ALL)
            if confirm.strip() == "":
                print("Confirm tidak boleh kosong!")
                continue
            
            if confirm in 'yn':
                return confirm
            else:
                print(Fore.RED + "Confirm tidak valid, tekan 'y' atau 'n'!")
                print(Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Confirm tidak valid! Tekan 'y' atau 'n'.")
            print(Style.RESET_ALL)
def bersih_layar():
     os.system('cls' if os.name == 'nt' else 'çlear')

# Mengakses tuple berdasar indeks
while True:
    try:
        bersih_layar()
        input_indeks = input("\nMasukkan indeks ke: - dalam angka bulat <= {jumlah_elemen}: ")
        
        # Jika indeks lebih besar dari jumlah elemen
        if not -jumlah_elemen <= int(input_indeks) < jumlah_elemen:
            print(Fore.RED + "Angka indeks tidak valid! Sesuaikan dengan jumlah elemen.")
            print(Style.RESET_ALL)
            continue
        else:    
            if input_indeks.strip():
                input_indeks = int(input_indeks)
                # Cetak indeks ke: ...
                isi_indeks = nama_buah[input_indeks]
                print(f"\nIsi elemen ke:{input_indeks} dari tuple 'nama_buah' adalah: {isi_indeks}")
                    

                confirm = confirm_lanjut()
                if confirm in 'n':
                    break
                
            else:
                print(Fore.RED + "Input indeks tidak boleh kosong.")
                print(Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Input indeks tidak valid!")
        print(Style.RESET_ALL)
        


