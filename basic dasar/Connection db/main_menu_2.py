import sys
import os
import subprocess
import colorama
from colorama import init, Fore

# Dapatkan direktori saat ini (direktori tempat main_menu_2.py berada)
# current_directory = os.path.dirname(os.path.abspath(__file__))
current_directory = sys.argv[0]

def run_datajual():
    try:
        #subprocess.run([os.path.join(current_directory, 'dist', 'main_menu_2.exe')])
        #subprocess.run(['python', 'data_penjualan.py'], check=True)
        subprocess.run(['python', os.path.join(current_directory, '..', 'data_penjualan.py')], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def main():
    init()

    while True:
        print("Menu:")
        print("1. Data Penjualan")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")

        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            print("Menampilkan data penjualan...")
            run_datajual()
    
        elif choice == '2':
            print("Anda memilih Option 2")
            # Tambahkan logika untuk menu Option 2 di sini

        elif choice == '3':
            print("Anda memilih Option 3")
            # Tambahkan logika untuk menu Option 3 di sini

        elif choice == '4':
            print("Program berakhir.")
            break

        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan pilih kembali." + Fore.RESET)

if __name__ == '__main__':
    main()
