# aboutme.py

def main():
    # Beri jarak beberapa baris kosong
    for i in range(1,8):
        print("\n")
        
    panjang_grs = 50
    garis_dobel = '=' * panjang_grs
    garis_tunggal = '-' * panjang_grs
    print(garis_dobel)
    print("INFO PENJUALAN")
    print(garis_dobel)    
    print("Salam kenal.")
    print("Ini adalah ujicoba aplikasi Info Penjualan")
    print("berbasis konsol. ")
    print("Program ini dibuat untuk tujuan praktis, yaitu ")
    print("mengakses data penjualan dengan simple dan cepat.")
    print(garis_tunggal)
    print("devby:python")
    print(garis_tunggal, '\n')
           
if __name__ == "__main__":
    main()
