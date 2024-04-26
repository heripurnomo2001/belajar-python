import os
from mode_terminal import lebar_kolom 
from colorama import Fore, Back, Style, init
# aboutme.py


def bersih_layar():
     os.system('cls' if os.name == 'nt' else 'çlear')

def main():
    # Beri jarak beberapa baris kosong
    for i in range(1,8):
        print("\n")
    lbr_kolom = lebar_kolom()    
    bersih_layar()

    panjang_grs = lbr_kolom
    garis_dobel = '=' * panjang_grs
    garis_tunggal = '-' * panjang_grs

    #print("lebar kolom : ", lbr_kolom)
    redaksi = '''
Aplikasi ini dibuat untuk memudahkan Anda mendapatkan informasi penjualan dengan cepat dan efisien. Dirancang dengan antarmuka konsol yang sederhana namun powerful, sehingga Anda dapat mengakses data penjualan tanpa harus repot dengan tampilan yang rumit.

Aplikasi ini memungkinkan Anda untuk:

- Melihat data penjualan secara keseluruhan atau berdasarkan kategori tertentu dengan cepat dan mudah.
- Mengakses laporan penjualan harian, mingguan, bulanan, atau sesuai dengan rentang waktu yang Anda tentukan.
- Memeriksa informasi detail produk, termasuk jumlah stok, harga, dan informasi penting lainnya.
- Menganalisis tren penjualan dari waktu ke waktu untuk membantu Anda membuat keputusan yang lebih baik dalam strategi penjualan Anda.

Kami berkomitmen untuk terus meningkatkan aplikasi kami dengan fitur-fitur baru yang lebih bermanfaat dan inovatif. Dengan Info Penjualan Berbasis Konsol, Anda dapat mengoptimalkan pengelolaan penjualan Anda dengan mudah.

Jika Anda memiliki pertanyaan atau masukan, jangan ragu untuk menghubungi kami. Terima kasih telah memilih aplikasi kami untuk membantu membantu pekerjaan bisnis Anda!
        '''

    print(garis_dobel)
    print(Fore.WHITE + Back.RED + 'Selamat datang di APLIKASI INFO PENJUALAN Berbasis Konsol!')
    print(Style.RESET_ALL)
    print(garis_dobel)
    print(redaksi)
    print(garis_tunggal)
    print("devby: python")
    print(garis_tunggal, '\n')
           
if __name__ == "__main__":
    main()
