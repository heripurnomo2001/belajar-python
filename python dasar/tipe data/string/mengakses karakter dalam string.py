
# MENGAKSES KARAKTER DALAM STRING

'''
Soal 1: Mengakses Karakter dalam String
Buatlah sebuah program Python yang meminta pengguna untuk memasukkan sebuah string.
Tampilkan panjang dari string tersebut.
Mintalah pengguna untuk memasukkan sebuah indeks (bilangan bulat) antara 0 hingga panjang string dikurangi 1.
Cetak karakter yang berada pada indeks yang dimasukkan pengguna.
'''

# function
def input_kata():
    while True:
        try:
            kata = input("Masukkan sebuah kata (ketik 'quit' untuk keluar): ")
            if kata.strip() == "":
                print("kata tidak boleh kosong.")
            elif kata.lower() == 'quit':
                return None
            else:
                return kata
        except ValueError:
            print("Kata yang anda masukkan tidak valid!")

def input_indeks(panjang_kata):
    while True:
        try:
            n = int(input(f"Masukkan angka ke n untuk menampilkan karakter ke n. Angka >=0 dan <= {panjang_kata-1}: "))            
            if 0 <= n < panjang_kata:
                return n # mengembalikan indeks yang valid
            else:
                print(f"Angka yang dimasukkan harus di antara 0 dan {panjang_kata-1}.")

        except ValueError:
            print("Masukkan angka yang valid!")

# entry form user
while True:
    kata = input_kata()
    if kata == None:
        break
    
    panjang_kata = len(kata)        
    print("Panjang kata adalah ", panjang_kata, "karakter")


    n = input_indeks(panjang_kata)                
    karakter_ke_n = kata[n]

    # cetak karakter ke n
    print(f"Karakter ke {n} adalah : {karakter_ke_n}")

    confirm_lanjut = input("Apakah anda ingin melanjutkan kata berikutnya? (y/n): ").lower()
    if confirm_lanjut == 'y':  
        pass
    elif confirm_lanjut == 'n':
        print("\nTerima kasih sudah berlatih pemrograman python hari ini!")
        break
    else:
        print("Pilihan hanya 'y' atau 'n'!")
            
