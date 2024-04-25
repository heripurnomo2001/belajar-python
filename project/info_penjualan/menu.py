import os
import aboutme  # Import modul aboutme.py
import datajual
import subprocess
import time
from colorama import Fore, Back, Style

# Nilai default untuk lebar terminal jika tidak dapat diambil secara dinamis
terminal_width_default = 80

def main_menu():

    global terminal_width  # Mengakses variabel global
    
    try:
        # Mengambil lebar terminal saat ini (jika berhasil)
        terminal_width = os.get_terminal_size().columns
    except OSError:
        # Penanganan kesalahan jika os.get_terminal_size() tidak berhasil
        terminal_width = terminal_width_default # Menentukan lebar terminal tetap 
    

    # Menentukan teks menu
    menu_title = "=== Menu ==="
    option_1 = "1. About Me!"
    option_2 = "2. Data Penjualan Harian"
    option_3 = "3. Data Penjualan Periode"
    exit_option = "4. Keluar"
    
    # Menghitung posisi tengah teks menu
    title_centered = menu_title.center(terminal_width)
    option_1_centered = option_1.center(terminal_width)
    option_2_centered = option_2.center(terminal_width)
    option_3_centered = option_3.center(terminal_width)
    exit_option_centered = exit_option.center(terminal_width)

    # Membersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'çlear')

    beri_jarak_cetak()
    
    print(Fore.MAGENTA + Back.YELLOW + Style.DIM + title_centered)
    print(Style.RESET_ALL)  # Reset warna ke default
    print(option_1_centered)
    print(option_2_centered)
    print(option_3_centered)
    print(exit_option_centered)

def option1():
    bersih_layar()        
    aboutme.main()  # Memanggil fungsi main() dari helloworld.py
    input(Fore.RED + Back.YELLOW + Style.BRIGHT + "Tekan Enter untuk kembali ke menu utama...")  # Tunggu sampai pengguna menekan Enter
    print(Style.RESET_ALL)  # Reset warna ke default

def option2():
    bersih_layar()    
    for i in range(1,3):
        print("\n")
    datajual.datajualharian()  # Memanggil datajualharian() dari datajual.py
    input("Tekan Enter untuk kembali ke menu utama...")  # Tunggu sampai pengguna menekan Enter
    

def option3():
    
    bersih_layar()    
    for i in range(1,3):
        print("\n")
    datajual.datajual_periode()  # Memanggil datajual_periode() dari datajual.py
    input("Tekan Enter untuk kembali ke menu utama...")  # Tunggu sampai pengguna menekan Enter

def bersih_layar():
    # Membersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'çlear')
def beri_jarak_cetak():    
    for i in range(1,5):
        print("\n")

# Fungsi utama untuk menjalankan program
def run_program():
    while True:
        #os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar konsol
        main_menu()

        global terminal_width  # Mengakses variabel global

        
        text_choice ="Masukkan pilihan Anda (1/2/3/4): "
        panjang_text_choice = len(text_choice)
        spasi = int((terminal_width - panjang_text_choice)/2)

        text_choice = " " * spasi + text_choice
        print("\n" + text_choice, end="", flush=True)
        try:
            choice = input()

            if choice == '1':
                option1()
            elif choice == '2':
                option2()
            elif choice == '3':
                option3()
            elif choice == '4':
                bersih_layar()
                beri_jarak_cetak()
                text_salam = "Terima kasih telah menggunakan program. Sampai jumpa lagi!"
                panjang_text_salam = len(text_salam)
                spasi = int((terminal_width - panjang_text_salam)/2)
                text_salam = " " * spasi + text_salam
                print("\n" + text_salam, end="", flush=True)            
                time.sleep(2)
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan angka 1, 2, 3, atau 4.")
                input("Tekan sembarang tombol untuk kembali ke menu utama.")
        except ValueError:
            print("Pilihan tidak valid. Silakan masukkan angka 1, 2, 3, atau 4.")
            

# Panggil fungsi run_program() untuk memulai program
run_program()
