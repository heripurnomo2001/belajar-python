'''
Soal 3: Mengulang Karakter dalam String
Buatlah sebuah program Python yang meminta pengguna untuk memasukkan sebuah karakter dan bilangan bulat positif.
Buatlah string baru yang berisi karakter tersebut yang diulang sebanyak bilangan bulat yang dimasukkan.
Cetak string yang dihasilkan.
'''

while True:
    try:
        input_str = input("Masukkan sebuah karakter dan sebuah bialangan bulat. Contoh: 'F6'. Ketik 'quit' untuk keluar: ")

        # Validasi input tidak boleh kosong
        if not input_str.strip():
            print("Input tidak boleh kosong!")
            continue # Lanjut ke iterasi berikutnya dalam loop

        # Keluar jika input adalah 'quit'    
        if input_str.lower() == 'quit':
            continue # Lanjut ke iterasi berikutnya dalam loop
        
        # Validasi panjang input harus tepat 2 karakter
        if len(input_str) != 2:
            print("Input harus terdiri dari tepat 2 karakter.")
            continue # Lanjut ke iterasi berikutnya dalam loop

        karakter = input_str[0]
        jumlah_ulang = int(input_str[1])

        # Validasi jumlah ulang harus bilangan bulat positif
        if jumlah_ulang <= 0:
            print("Bilangan bulat harus lebih besar dari 0.")

        # Cetak karakter diulang sebanyak jumlah_ulang

        hasil = karakter * jumlah_ulang
        print(f"Karakter '{karakter}' dicetak {jumlah_ulang} kali: {hasil}\n")
                    

        confirm_lanjut = input("Masih lanjut ? (y/n): ")
        if confirm_lanjut.lower() == 'n':
            break
        elif confirm_lanjut.lower() == 'y':
            pass
                                                 
    except ValueError as e:
        print(f"Karakter yang anda masukkan tidak valid! Kesalahan: {e}")
