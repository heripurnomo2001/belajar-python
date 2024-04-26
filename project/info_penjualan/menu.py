import os
import aboutme  # Import modul aboutme.py
import datajual
import subprocess
import time
from colorama import Fore, Back, Style


def main_menu():

    # Menentukan teks menu
    title      = "                   INFO PENJUALAN                       "
    menu_title = "======================= Menu ==========================="
    option_1 = "    1. About Me!"
    option_2 = "    2. Data Penjualan Hari ini"
    option_3 = "    3. Data Penjualan Periode"
    option_4 = "    4. Top 10 Produk"
    option_5 = "    5. Top 10 Customer"
    option_6 = "    6. Top 10 Salesman"
    exit_option = "    7. Keluar"
    garis_batas = "======================================================="
    

    # Membersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'çlear')

    beri_jarak_cetak()
    print(title)
    print(Fore.WHITE + Back.RED + menu_title)
    print(Style.RESET_ALL)  # Reset warna ke default
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(option_5)
    print(option_6)    
    print(exit_option)
    print(garis_batas)

def option1():
    bersih_layar()        
    aboutme.main()  # Memanggil fungsi main() dari helloworld.py
    input(Style.BRIGHT + Fore.CYAN  + "Tekan Enter untuk kembali ke menu utama...")  # Tunggu sampai pengguna menekan Enter
    print(Style.RESET_ALL)  # Reset warna ke default

def option2():
    bersih_layar()    
    for i in range(1,3):
        print("\n")
    datajual.datajualharian()  # Memanggil datajualharian() dari datajual.py
    input(Style.BRIGHT + Fore.CYAN + "Tekan Enter untuk kembali ke menu utama...")  # Tunggu sampai pengguna menekan Enter
    

def option3():
    
    bersih_layar()    
    for i in range(1,3):
        print("\n")
    datajual.datajual_periode()  # Memanggil datajual_periode() dari datajual.py
    input(Style.BRIGHT + Fore.CYAN + "Tekan Enter untuk kembali ke menu utama...")  # Tunggu sampai pengguna menekan Enter

def option4():
    bersih_layar()    
    for i in range(1,3):
        print("\n")
    datajual.topproduk()  # Memanggil fungsi top produk 
    input(Style.BRIGHT + Fore.CYAN + "Tekan Enter untuk kembali ke menu utama...")  # Tunggu sampai pengguna menekan Enter

def option5():
    bersih_layar()    
    for i in range(1,3):
        print("\n")
    datajual.topcustomer() # Memanggil fungsi top customer 
    input(Style.BRIGHT + Fore.CYAN + "Tekan Enter untuk kembali ke menu utama...")  # Tunggu sampai pengguna menekan Enter

def option6():
    bersih_layar()    
    for i in range(1,3):
        print("\n")
    datajual.topsalesman() # Memanggil fungsi top customer 
    input(Style.BRIGHT + Fore.CYAN + "Tekan Enter untuk kembali ke menu utama...")  # Tunggu sampai pengguna menekan Enter

def bersih_layar():
    # Membersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'çlear')
def beri_jarak_cetak():    
    for i in range(1,5):
        print("\n")

# Fungsi utama untuk menjalankan program
def run_program():
    while True:
        main_menu()        
        text_choice ="Masukkan pilihan Anda (Ketik pilihan angka: 1 -sd- 7): "
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
                option4()
            elif choice == '5':
                option5()
            elif choice == '6':
                option6()
            elif choice == '7':
                bersih_layar()
                beri_jarak_cetak()
                text_salam = "Terima kasih telah menggunakan program. Sampai jumpa lagi!"
                print("\n" + Style.BRIGHT + Fore.CYAN + text_salam, end="", flush=True)
                time.sleep(2)
                break
            else:
                print(Style.BRIGHT + Fore.RED + "Pilihan tidak valid. Silakan masukkan sebuah angka: 1 -sd- 7.")
                input(Style.BRIGHT + Fore.CYAN + "Tekan Enter untuk kembali ke menu utama...")
        except ValueError:
            print(Style.BRIGHT + Fore.RED + "Pilihan tidak valid. Silakan masukkan sebuah angka: 1 -sd- 7.")
            
# Panggil fungsi run_program() untuk memulai program
run_program()
