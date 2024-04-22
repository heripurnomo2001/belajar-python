# Basic Arithmetic Calculator
'''
Buatlah sebuah program Python yang menerima dua angka dari pengguna
dan menampilkan hasil dari operasi penjumlahan, pengurangan, perkalian,
dan pembagian dari kedua angka tersebut.
Pastikan program dapat menangani input angka desimal.
'''

def input_angka(text):
    while True:
        try:
            angka = input(f"Masukkan angka {text}. Batasan angka antara 0 dan 20: ")
            if angka.strip() == '':
                print("Angka tidak boleh kosong atau negatif!")
                continue

            angka = float(angka)
            if 0 <= angka <= 20:    
                return angka
            else:
                print("Angka yang anda masukkan tidak valid, Masukkan angka antaran 0 sampai 20.")
                
        except ValueError as e:
            print("Input angka anda tidak valid! Kesalahan: ", e)

def confirm_lanjut():
    while True:
        confirm = input("\nMau mencoba lagi? Tekan 'y' dan 'n' untuk lanjut atau keluar.\n").lower()
        if confirm.strip() == '':
            print("Confirm tidak boleh kosong!")
            continue
        if confirm in 'yn':
            return confirm
        else:
            print("Confirm yang anda masukkan tidak valid! Masukkan 'y' atau 'n'.")
            

while True:
    angka_pertama = input_angka("pertama")
    angka_kedua = input_angka("kedua")
 
    # Hasil perhitungan
    penjumlahan = angka_pertama + angka_kedua
    pengurangan = angka_pertama - angka_kedua
    perkalian = angka_pertama * angka_kedua
    pembagian = angka_pertama / angka_kedua
        
    print("Hasil penjumlahan : %5.1f" % penjumlahan) 
    print("Hasil pengurangan : %5.1f" % pengurangan)
    print("Hasil perkalian   : %5.1f" % perkalian)
    print("Hasil pembagian   : %5.2f" % pembagian)
    
            
    confirm = confirm_lanjut()
    if confirm == 'y':
        continue
    # Jika confirn 'n'
    print("\nTerima kasih, selamat tinggal.")
    break
    
        

    
        
