# Penerapan OOP
# Object : Inventaris Rumah Tangga

# Contoh: Buku

class barang_rmh_tangga():
    nama = None
    kategori = None
    jumlah = 0
    lokasi = None

    def info(self):
        print('Info barang: ')
        print(f'Nama barang: {self.nama}')
        print(f'Kategori: {self.kategori}')
        print(f'Jumlah: {self.jumlah}')
        print(f'Lokasi: {self.lokasi}')
        print('\n')

    def tambah_barang(self, jumlah_baru):
        self.jumlah += jumlah_baru

    def kurang_barang(self, jumlah_pengurang):
        self.jumlah -= jumlah_pengurang

# Instansiasi
riyadus_shalihin = barang_rmh_tangga()
riyadus_shalihin.nama = 'riyadus_shalihin'
riyadus_shalihin.kategori = 'BUKU'
riyadus_shalihin.jumlah = 1
riyadus_shalihin.lokasi = 'Lemari buku ruang tamu rak no.3'
riyadus_shalihin.info()    

obeng1 = barang_rmh_tangga()
obeng1.nama = 'obeng kembang X'
obeng1.kategori = 'KUNCI'
obeng1.jumlah = 5
obeng1.lokasi = 'Lemari gudang '

# Object Obeng awal
print("Ini Obeng1 awal:")
obeng1.info()

# Obeng1 setelah dikurangi
obeng1.kurang_barang(1)
print("Ini Obeng1 setelah dikurang 1:")
obeng1.info()

# Menambah jumlah barang riyadus_shalilih sebanyak 2
riyadus_shalihin.tambah_barang(2)
print(riyadus_shalihin.info())

