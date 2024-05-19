# PALINDROM
# adalah string yang dibalik sama dengan string asli


while True:
    # entry form
    kata = input("Masukkan kata (Jika ingin keluar ketik 'Quit' : ")
    if kata.lower() == "quit":
        print("\nTerima kasih sudah mencoba project Palindrom ini.")
        break
    else:
    # iterasi
        jmlhuruf = len(kata)
        balik_kata = ''
        for i in range(jmlhuruf,0,-1):
            huruf = kata[i-1:i]
            balik_kata += huruf

        if balik_kata == kata:    
            print(f"Kata {kata} adalah Palindrom.")
        else:
            print(f"Kata {kata} adalah BUKAN Palindrom.")
            

    
