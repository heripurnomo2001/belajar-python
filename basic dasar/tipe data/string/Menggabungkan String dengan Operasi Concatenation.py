"""
Soal 2: Menggabungkan String dengan Operasi Concatenation
Berikan dua input string kepada pengguna melalui input.
Gabungkan dua string tersebut menjadi satu string baru menggunakan operator concatenation (+).
Cetak string hasil penggabungan.
"""

def input_string1():
    while True:
        try:
            string1 = input("Masukkan kata pertama: ")
            if string1.strip() == "":
                print("Kata pertama tidak boleh kosong!")
            else:
                return string1
        except ValueError:
            print("Kata yang anda masukkan tidak valid!")

def input_string2():
    while True:
        try:
            string2 = input("Masukkan kata ke-dua: ")
            if string2.strip() == "":
                print("Kata ke-dua tidak boleh kosong!")
            else:
                return string2
        except ValueError:
            print("Kata yang anda masukkan tidak valid!")

while True:
    
    string1 = input_string1()
    string2 = input_string2()
    print("string1 + string2 : ", string1+string2)

    
    confirm_lanjut = input("Apakah lanjut {y/n): ")
    if confirm_lanjut == 'n':
        break
    elif confirm_lanjut == 'y':
        pass
    else:
        print("Confirm yang anda masukkan tidak valid, pilih y/n.")

        
