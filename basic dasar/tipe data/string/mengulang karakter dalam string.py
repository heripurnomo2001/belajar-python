'''
Soal 3: Mengulang Karakter dalam String
Buatlah sebuah program Python yang meminta pengguna untuk memasukkan sebuah karakter dan bilangan bulat positif.
Buatlah string baru yang berisi karakter tersebut yang diulang sebanyak bilangan bulat yang dimasukkan.
Cetak string yang dihasilkan.
'''

while True:
    try:
        kata = input("Masukkan sebuah karakter dan sebuah bialangan bulat. Contoh: 'F6'. Ketik 'quit' untuk keluar: ")
        # validasi kosong
        if not kata.strip():
            print("Karakter tidak boleh kosong!")
        elif kata.lower() == 'quit':
            break
        else:
            # validasi jumlah karakter ( = 2)
            if len(kata.strip()) != 2:
                print("Jumlah karakter harus = 2.")
            else:
                karakter_ke_1 = kata[0:1]
                # validasi karakter ke 2 harus angka
                karakter_ke_2 = int(kata[1:2])
                if 0 < karakter_ke_2:
                    print(f"Karakter '{karakter_ke_1}' dicetak {karakter_ke_2} kali: ")
                    for i in range(karakter_ke_2):
                        print(f"{karakter_ke_1}", end=" ")
                    print("")
                else:
                    print("Karakter ke 2 harus angka >0 !")

        confirm_lanjut = input("Masih lanjut ? (y/n): ")
        if confirm_lanjut.lower() == 'n':
            break
        elif confirm_lanjut.lower() == 'y':
            pass
        else:
            print("karekter yang anda masukkan tidak valid")

                                                 
    except ValueError as e:
        print(f"Karakter yang anda masukkan tidak valid! Kesalahan: {e}")
