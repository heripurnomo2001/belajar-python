from colorama import Fore, Back, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Contoh penggunaan warna teks
print(Fore.RED + 'Teks merah')
print(Fore.GREEN + 'Teks hijau')
print(Fore.BLUE + 'Teks biru')

# Contoh penggunaan warna latar belakang (background)
print(Back.RED + 'Latar belakang merah')
print(Back.GREEN + 'Latar belakang hijau')
print(Back.BLUE + 'Latar belakang biru')

# Contoh kombinasi warna teks dan latar belakang
print(Fore.WHITE + Back.RED + 'Teks putih di latar belakang merah')
print(Fore.YELLOW + Back.GREEN + 'Teks kuning di latar belakang hijau')

# Menggunakan gaya teks (bold, underline, dan lainnya)
print(Style.BRIGHT + Fore.CYAN + 'Teks berwarna terang (bright cyan)')
print(Style.NORMAL + Fore.MAGENTA + 'Teks berwarna normal (normal magenta)')
print(Style.DIM + Fore.YELLOW + 'Teks dengan gaya dim (dim yellow)')
print(Style.RESET_ALL)  # Mengembalikan ke gaya default

# Menggunakan kombinasi gaya teks dan warna
print(Style.BRIGHT + Fore.RED + 'Teks merah terang dan berwarna terang')
print(Style.BRIGHT + Back.GREEN + 'Latar belakang hijau terang')


input("Tekan sembarang tombol untuk mengakhiri!")
