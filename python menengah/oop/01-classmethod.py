# Belajar class


class Manusia:
    jumlah_tangan = 2 # variable kelas

    def  __init__(self, nama):
        self.nama = nama # instance variabel


    @classmethod
    def pengertian(cls):
        print(f'Manusia memiliki {cls.jumlah_tangan} tangan')


print("Memanggil method langsung melalui kelas:")
Manusia.pengertian()

# Panggil via object
seseorang = Manusia('Tanpa Nama')
print("Memanggil method via object:")
seseorang.pengertian()


    
