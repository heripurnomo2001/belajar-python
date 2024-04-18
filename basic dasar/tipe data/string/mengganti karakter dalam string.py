'''
Soal 4: Mengganti Karakter dalam String
Buatlah sebuah program Python yang meminta pengguna untuk memasukkan sebuah string.
Mintalah pengguna untuk memasukkan indeks dari karakter yang ingin diganti (antara 0 hingga panjang string dikurangi 1).
Mintalah pengguna untuk memasukkan karakter pengganti.
Gantilah karakter pada indeks yang dimasukkan dengan karakter pengganti.
Cetak string yang telah dimodifikasi.
'''

def input_str():
    while True:
        try:
            input_str = input("Masukkan sebuah kata. (ketik 'quit') jika ingin keluar): ").strip().lower()
            if input_str == 'quit':
                return None
            
            if input_str.strip(): # Jika input_str tidak kosong setelah dihilangkan spasi kanan dan kiri
                return input_str

            if input_str == "":
                print("Input anda kosong. Masukkan sebuah kata.")
                continue # Melanjutkan iterasi berikutnya dalam loop

        except ValueError as e:
            print(f"Input anda tidak valid! Kesalahan: {e}")

def confirm_lanjut():
    while True:
        try:
            confirm_lanjut = input("Masih lanjut (y/n) ?: ")
            if confirm_lanjut == 'n':
                return 'n'
            if confirm_lanjut == 'y':
                return 'y'
            if confirm_lanjut != 'y':
                print("Pilihan hanya 'y' (lanjut) atau 'n' (tidak lanjut).")
                
        except ValueError as e:
            print(f"Confirm anda tidak valid. Kesalahan: {e}")

def index_ttn(jumlah_karakter):
    while True:
        try:
            index_ttn = int(input(f"Masukkan nomor karakter yang ingin anda ganti, antara 0 sampai {jumlah_karakter-1}: "))
            if 0 <= index_ttn < jumlah_karakter:
                return index_ttn
            else:
                print(f"Index harus berada di antara 0 dan {jumlah_karakter-1}.")
        
        except ValueError:
            print("Input nomor anda tidak valid!")

def karakter_pgt():
    while True:
        try:
            karakter_pgt = input("Masukkan sebuah karakter pengganti: ").strip()

            # Validasi karakter pengganti harus tepat 1 karakter
            if len(karakter_pgt) != 1:
                print("Jumlah karakter pengganti harus tepat 1 karakter!")
                continue # Melanjutkan iterasi berikutnya dalam loop

            # Mengembalikan nilai, jika kondisi memenuhi syarat
            return karakter_pgt

        except ValueError as e:
            print(f"Input anda tidak valid! Kesalahan: {e}")

while True:
    string = input_str()
    if string == None:
        print("Terima kasih. Selamat tinggal.")
        break
    
    jumlah_karakter = len(string)
    print(f"String yang anda input adalah '{string}' ")

    index_tertentu = index_ttn(jumlah_karakter)
    print("Nomor yang akan anda ganti adalah: ", index_tertentu)

    karakter_pengganti = karakter_pgt()
    print(f"Karakter pengganti adalah '{karakter_pengganti}'")

    string_baru = string[:index_tertentu]+karakter_pengganti+string[index_tertentu+1:]
    print("Kata yang baru adalah : ", string_baru)
    print("\n")

    confirm = confirm_lanjut()
    if confirm == 'n':
        print("Terima kasih. Selamat tinggal.")
        break 

    
