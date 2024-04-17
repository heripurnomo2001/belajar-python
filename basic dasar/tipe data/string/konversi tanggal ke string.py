# KONVERSI DATE KE STRING


# gunakan module datetime
from datetime import datetime

# form pengguna

while True:
    try:
        tg_string = input("Masukkan tanggal (ketik 'quit' untuk keluar) dengan format (YYYY-MM-DD): ")
        tahun = tg_string[:4]
        bulan = tg_string[5:7]
        hari  = tg_string[8:]
        if tg_string.lower() == 'quit':
            break
        else:
            tanggal = datetime.strptime(tg_string,'%Y-%m-%d').date()
            hasil = (f"Konversi tanggal dengan format string {tg_string} ke tanggal format date adalah : {tanggal.strftime('%d %B %Y')}")
            print(hasil)
            
        
    except ValueError as e:
        print("Tanggal yang anda masukkan tidak valid! Kesalahan: ", e)


'''
    strftime() : berfungsi untuk mengkonversi oject datetime menjadi string dengan format tertentu.
    strptime() : berfungsi untuk mengkonversi string menjadi object datetime
'''
