"""
Soal 2: Menggabungkan String dengan Operasi Concatenation
Berikan dua input string kepada pengguna melalui input.
Gabungkan dua string tersebut menjadi satu string baru menggunakan operator concatenation (+).
Cetak string hasil penggabungan.
"""

def input_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip(): # jika user_input tidak kosong setelah di-strip() 
            return user_input        
        else:
            print("Kata pertama tidak boleh kosong!")

while True:
    
    string1 = input_string("Masukkan kata pertama:")
    string2 = input_string("Masukkan kata ke-dua:")
    print("string1 + string2 : ", string1+string2)

    confirm_lanjut = input("Apakah lanjut {y/n): ")
    if confirm_lanjut == 'n':
        break
    elif confirm_lanjut == 'y':
        pass
    else:
        print("Confirm yang anda masukkan tidak valid, pilih y/n.")

        
