# BELAJAR CRUD
# TAMBAH PELANGGAN

import validators
import re


#siapkan data kosong
pelanggan = []


#function validasi
def validate_kode_pelanggan(kode_pelanggan):
    try:
        if not kode_pelanggan.strip():
            print("Kode pelanggan tidak boleh kosong")
            return False
        elif len(kode_pelanggan) != 10:
            print("Kode Pelanggan minimal 10 character!")
            return False
        else:
            return True
    
    except ValueError as e:
        print("Terjadi kesalahan {e}")
        
def validate_nama(nama):
    if not nama.strip():
        print("Nama Pelanggan tidak boleh kosong")
        return False
    return True

def validate_email(email):
    # Cek format umum email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Format email tidak valid.")
        return False
    
    elif not validators.email(email):
        print("Domain email tidak valid.")
        return False
    
    # Validasi berhasil jika melewati semua cek
    return True

#function enty data
def get_user_input():
    while True:
        kode_pelanggan = input("Masukkan kode pelanggan : ")
        if validate_kode_pelanggan(kode_pelanggan):
            break
        
    nama = input("Masukkan nama pelanggan : ")
    alamat = input("Masukkan alamat : ")
    nomor_hp = input("Masukkan nomor HP : ")

    while True:
        email = input("Masukkan email : ")
        if validate_email(email):
            break
        
    while not validate_kode_pelanggan(kode_pelanggan):
        kode_pelanggan = input("Masukkan kode pelanggan : ")

    while not validate_nama(nama):
        nama = input("Masukkan Nama Pelanggan : ")

    while not validate_email(email):
        email = input("Masukkan Email : ")

    return kode_pelanggan, nama, email


def tambah_pelanggan():
    try:
        #panggil function entry
        kode_pelanggan, nama, email = get_user_input()

        #insert data
        pelanggan.append({'kode_pelanggan': kode_pelanggan, 'nama': nama, 'email': email})
        #konfirm lanjut input data lagi
        lanjut = input("Apakah mau lanjut input data lagi? 'ya' untuk lanjut, 'tidak' untuk keluar : ")

        if lanjut.lower() == 'tidak':
            return False
        elif lanjut.lower() != 'ya':
            print("Anda memasukkan konfirmasi yang tidak valid! ")
            return tambah_pelanggan() # Panggil kembali fungsi tambah_kegiatan() untuk mengulangi konfirmasi
        return True
    
    except ValueError as e:
        print(f"Kesalahan : {e}")


#LOOPING PROGRAM
while tambah_pelanggan():
    pass


#Print daftar Pelanggan

#Header
header = ['KODE PELANGGAN', 'NAMA', 'EMAIL']
header_format = '{:<20} {:<40} {:<40}'.format(*header)
        
#cetak header_format
print(header_format)

for item in pelanggan:
    data_format = '{:<20} {:<40}  {:<40}'.format(item['kode_pelanggan'], item['nama'], item['email'])
    print(data_format)

input("Tekan sembarang tombol untuk meninggalkan program ini ..")
    

