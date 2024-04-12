# MENGHITUNG KARAKTER UNIK


while True:
    try:
        # entry form
        kalimat = input("\nMasukkan kalimat ( ketik Quit utk keluar ) : ")
        jmlhuruf = len(kalimat)
        if kalimat.lower() == 'quit':
            print('\nTerima kasih sudah mencoba project ini.')
            break
        else:
            huruf_unik = []            
            for i in (kalimat):
                hithuruf = kalimat.count(i)
                if hithuruf == 1 and i != ' ':
                    #print(i, end=",")
                    huruf_unik.append(i)
            #print(huruf_unik)
            jmunik = len(huruf_unik)
            print(f"Penjelasan: Teks {kalimat} memiliki {jmunik} karakter unik yang muncul hanya sekali: ", end=" ")  
            for index, huruf in enumerate(huruf_unik):
                if index < len(huruf_unik)-1:
                    print(huruf, end=", ")
                else:
                    print(huruf)

    
    except ValueError:
        print("Kesalahan : input yang anda masukkan tidak valid!")
        
