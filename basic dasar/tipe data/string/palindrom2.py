# PALINDROM
# definisi : kata yang pengucapannya sama apabila dibalik


# buat fungsi membalik kata
def membalik_kata(kata):
    return kata[::-1]

while True:
    try:
        kata = input("Masukkan kata (Ketik 'quit' untuk keluar : ")
        if kata.isspace() or not kata:
            print("Kata yang anda masukkan kosong!")
        elif kata.lower() == "quit":
            break
        else:
            hasil = membalik_kata(kata)
            if hasil == kata:
                print(f"{kata} adalah PALINDROM.")
            else:
                print(f"{kata} adalah BUKAN PALINDROM.")
                
    except ValueError as e:
        print("Kata yang anda masukkan tidak valid! Kesalahan: ", e)
