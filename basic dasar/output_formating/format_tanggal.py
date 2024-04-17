# FORMAT TANGGAL

def format_tanggal(tanggal):
    # ambil tahun, bulan, hari menggunakan slicing
    tahun = tanggal[:4]
    bulan = tanggal[5:7]
    hari  = tanggal[8:]
    

    # gabungkan kembali dalam format "DD/MM/YYYY"
    tanggal_format = f"{hari}/{bulan}/{tahun}"
    return tanggal_format

input_tanggal = input("Masukkan tanggal dengan format : YYYY-MM-DD : ")


# memanggail fungsi format_tanggal
hasil_format = format_tanggal(input_tanggal)

print(f"Hasil format {input_tanggal} adalah {hasil_format}")

