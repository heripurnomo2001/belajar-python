# MEMBALIK KATA-KATA DALAM SEBUAH KALIMAT


# loop until quit
while True:
    try:
        kalimat = input("Masukkan kalimat ( ketik 'quit' jika ingin keluar ) : ")
        if kalimat.isspace():
            print("Input kalimat jangan diisi kosong!")
        elif kalimat == 'quit':
            break
        else:
            kata_kata = kalimat.split()
            jumlah_kata = len(kata_kata)
            print("Jumlah kata : ", jumlah_kata)
            kata_balik = ''
            for i in range(jumlah_kata):
                kata_balik += ' '+ kata_kata[i][::-1]

            print(f'Hasil membalikkan kata dalam kalimat \'{kalimat}\' adalah \'{kata_balik}\' ')
                
    except ValueError:
        print("Kalimat yang anda masukkan tidak valid!")
