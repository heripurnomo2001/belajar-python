# JADWAL KEGIATAN HARIAN

#import library
import os
from datetime import datetime, time


#siapkan data dictionary kosong
kegiatan = []


#function validasi
def validate_nama_kegiatan(namakegiatan):
    if not namakegiatan.strip():
        print("Nama kegiatan tidak boleh kosong")
        return False
    return True

def validate_tanggal(tanggal):
    try:
        datetime.strptime(tanggal, '%d-%m-%Y')
        return True
    except ValueError:
        print("Format tanggal tidak valid. Mohon masukkan tanggal dengan format DD-MM-YYYY.")
        return False

def validate_mulai_jam(mulai_jam):
    try:
        datetime.strptime(mulai_jam, '%H:%M:%S')                     
        return True
    except ValueError:
        print("Format jam dimulai tidak valid. Mohon masukkan jam dimulai dengan format HH:MM:SS.")
        return False

def validate_selesai_jam(selesai_jam):
    try:
        datetime.strptime(selesai_jam, '%H:%M:%S')                     
        return True
    except ValueError:
        print("Format jam selesai tidak valid. Mohon masukkan jam selesai dengan format HH:MM:SS.")
        return False

def validate_waktu(mulai_jam, selesai_jam):
    try:
        mulai_obj = datetime.strptime(mulai_jam, '%H:%M:%S')
        selesai_obj = datetime.strptime(selesai_jam, '%H:%M:%S')
        if selesai_obj <= mulai_obj:
            print("Waktu selesai harus lebih besar dari waktu mulai.")
            return False
        return True
    except ValueError:
        print("Format waktu tidak valid. Mohon masukkan waktu dengan format HH:MM:SS.")
        return False


def get_user_input():
    namakegiatan = input("Masukkan nama kegiatan: ")
    tanggal = input("Masukkan tanggal (format: DD-MM-YYYY): ")
    mulai_jam = input("Masukkan jam dimulai (format: HH-MM-SS): ")
    selesai_jam = input("Masukkan jam selesai (format: HH-MM-SS): ")

    while not validate_nama_kegiatan(namakegiatan):
        namakegiatan = input("Masukkan nama kegiatan: ")

    while not validate_tanggal(tanggal):
        tanggal = input("Masukkan tanggal (format: DD-MM-YYYY): ")

    while not validate_mulai_jam(mulai_jam):
        mulai_jam = input("Masukkan jam dimulai (format: HH:MM:SS): ")

    while not validate_selesai_jam(selesai_jam):
        selesai_jam = input("Masukkan jam selesai (format: HH:MM:SS): ")

    while not validate_waktu(mulai_jam, selesai_jam):
        mulai_jam = input("Masukkan jam dimulai (format: HH:MM:SS): ")
        selesai_jam = input("Masukkan jam selesai (format: HH:MM:SS): ")
    #print("Validasi berhasil.")
        
    return namakegiatan, tanggal, mulai_jam, selesai_jam

# Fungsi untuk mendapatkan input dari pengguna dan menyimpannya dalam list
def tambah_kegiatan():
    try:
        namakegiatan, tanggal, mulai_jam, selesai_jam = get_user_input()   
        kegiatan.append({'namakegiatan': namakegiatan, 'tanggal': tanggal, 'mulai_jam': mulai_jam, 'selesai_jam': selesai_jam})
        lanjut = input("Apakah anda masih mau memasukkan data lagi? Tekan 'ya' jika lanjut, 'tidak' untuk keluar!" )
        if lanjut.lower() == 'tidak':
            return False
        elif lanjut.lower() != 'ya':
            print("Konfirmasi anda tidak valid! Jawab 'ya' atau 'tidak'. ")
            return tambah_kegiatan()  # Panggil kembali fungsi tambah_kegiatan() untuk mengulangi konfirmasi
        return True
    
    except ValueError as e:
        print(f"Terjadi kesalahan: {e}")
        

#input: nama kegiatan, tanggal, waktu mulai dan selesai
while tambah_kegiatan():
    pass
    
    
            
print("DAFTAR KEGIATAN\n")
jmdata=len(kegiatan)
print("\nJumlah data = ",jmdata,'\n')

# Headers dengan redaksi berbeda dari nama key
header = ['NAMA KEGIATAN', 'TANGGAL', 'MULAI JAM', 'SELESAI JAM']
header_format = '{:<15} {:<10} {:<10} {:<10}'.format(*header)


# Menampilkan header dengan redaksi yang berbeda
# print('\t'.join(header))
print(header_format)

for item in kegiatan:
    data_format = '{:<15} {:<10} {:<10} {:<10}'.format(item['namakegiatan'], item['tanggal'], item['mulai_jam'], item['selesai_jam'])
    print(data_format)
    
print("\nSelesai!")





