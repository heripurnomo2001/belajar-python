# MENGGABUNGKAN NAMA DEPAN DAN BELAKANG

# form entry
nama_depan = input("Nama depan : ")
nama_belakang = input("Nama belakang : ")

nama = "Nama anda adalah %s %s " % (nama_depan, nama_belakang)

print(nama)
print(nama_depan + ' ' +nama_belakang)
print("{} {}" .format(nama_depan, nama_belakang))
print(nama_depan, end=" ")
print(nama_belakang )
