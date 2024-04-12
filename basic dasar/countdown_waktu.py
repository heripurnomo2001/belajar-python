# COUNTDOWN
# Menghitung mundur waktu tertentu hingga sekarang

from datetime import datetime, timedelta

while True:
    try:
        tg_string = input("Masukkan tanggal yang telah lalu (format:DD-MM-YYYY): ")
        slice1 = tg_string[0:2]
        slice2 = tg_string[3:5:1]
        slice3 = tg_string[-4:]
        tg_string = slice3+'-'+slice2+'-'+slice1
        tg_lalu = datetime.strptime(tg_string,'%Y-%m-%d')
        tg_sekarang = datetime.now()

        # jika tanggal yang diinput lebih besar atau sama dengan tanggal sekarang
        if tg_lalu >= tg_sekarang:
           raise ValueError("Tanggal yang anda input tidak boleh lebih besar atau sama dengan tanggal sekarang!")
        else:
           break
    except ValueError:
            print("Format tanggal yang anda masukkan tidak valid! Pastikan format:DD-MM-YYYY. ")


selisih = tg_sekarang - tg_lalu
format_tg_sekarang = tg_sekarang.strftime("%Y-%m-%d %H:%M:%S")
hari = selisih.days
formated_hari =  "{:,.0f}".format(hari)
jam,sisa_detik = divmod(selisih.seconds,3600)
menit, detik = divmod(sisa_detik,60)
print("Selisih waktu antara tangal:",tg_lalu," dan tanggal:",format_tg_sekarang," adalah: ",formated_hari,"hari, ",jam,"jam, ",menit,"menit, ",detik,"detik.")
print("\nSelesai\n")


        
