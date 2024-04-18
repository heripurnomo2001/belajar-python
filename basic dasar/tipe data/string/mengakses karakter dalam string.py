# MENGAKSES KARAKTER DALAM STRING

# entry form user
while True:
    try:
        kata = input("Masukkan sebuah kata (ketik 'quit' untuk keluar): ")
        if kata.isspace():  # bisa juga dengan : if kata.strip() == ""
            print("kata tidak boleh kosong.")
        elif kata.lower() == 'quit':
            break
        else:
            panjang_kata = len(kata.strip())
            print("Panjang kata adalah ", panjang_kata, "karakter")
            print("Catatan, spasi kanan dan kiri kata diabaikan.\n")
            n = input(f"Masukkan angka ke n untuk menampilkan karakter ke n. Angka >=0 dan <= {panjang_kata-1}: ")
            try:
                n = int(n)
            except ValueError as e:
                print("Data yang anda masukkan tidak valid: ", e)
                
            karakter_ke_n = kata[n]

            # cetak karakter ke n
            print("Karakter ke n adalah : ", karakter_ke_n)

            confirm_lanjut = input("Apakah anda ingin melanjutkan kata berikutnya? (y/n): ").lower()
            if confirm_lanjut == 'y':
                pass
            elif confirm_lanjut == 'n':
                print("\nTerima kasih sudah berlatih pemrograman python hari ini!")
                break
            else:
                print("input yang anda masukkan tidak valid!")
            
    except ValueError as e:
        print("Data yang anda masukkan tidak valid! Kesalahan : ", e)
