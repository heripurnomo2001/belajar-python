# SELISIH WAKTU

from datetime import datetime

while True:
    try:
        tg_string1 = input('Masukkan tanggal1 dengan format "YYYY-MM-DD" : ')
        tg1 = datetime.strptime(tg_string1,'%Y-%m-%d')
        break
    except ValueError:
        print("Format tanggal yang anda masukkan salah atau tidak valid! Masukkan format yang benar : 'YYYY-MM-DD' ")

while True:
    try:
        tg_string2 = input("Masukkan tanggal2 dengan format 'YYYY-MM-DD' : ")
        tg2 = datetime.strptime(tg_string2,'%Y-%m-%d')
        break
    except ValueError:
        print("Format tanggal yang anda masukkan salah atau tidak valid! Masukkan format yang benar : 'YYYY-MM-DD' ")

selisih = tg1 - tg2 
print(f"Selisih ", abs(selisih.days), ' hari\n')

print("selesai!")
