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
        Ini adalah aplikasi python berbasis console. Hanya untuk testing query sql melalui BigQuery API. 
        '''

    print(garis_dobel)
    print(Fore.WHITE + Back.RED + 'TEST INFO PENJUALAN DENGAN MEMANFAATKAN BIGQUERY GOOGLE')
    print(Style.RESET_ALL)
    print(garis_dobel)
    print(redaksi)
    print(garis_tunggal)
    print("disclaimer: just trial")
    print(garis_tunggal, '\n')
           
if __name__ == "__main__":
    main()
