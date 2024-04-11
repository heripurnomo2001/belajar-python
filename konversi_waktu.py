# KONVERSI TANGGAL
from datetime import datetime

while True:
    try:
        tg_string = input("Masukkan tanggal (format: DD-MM-YYYY): ")
        slice1 = tg_string[0:2]
        slice2 = tg_string[3:5:1]
        slice3 = tg_string[-4:]
        tg_string = slice3+'-'+slice2+'-'+slice1
        tanggal = datetime.strptime(tg_string,'%Y-%m-%d').date()
        break
    except ValueError:
        print("Tanggal yang anda masukkan tidak valid! Format: DD-MM-YYYY.")

print("Tanggal telah dikonversi menjadi : ",tanggal)
print('\nProgram selesai.')

    
