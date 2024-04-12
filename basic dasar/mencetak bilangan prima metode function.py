# MENCETAK BILANGAN PRIMA
# metode function

# buat function
def is_prime(bilangan):
    for angka in range(2,bilangan):
        prime = True
        for pembagi in range(2,angka):
            cek_prime = angka % pembagi # jika cek_prime == 0, maka bukan bil prima
            if cek_prime == 0:
                prime = False
                break
        if prime:
            print(angka,end=" ")
        
# form entry
bilangan = int(input("Masukkan batas bilangan : "))
is_prime(bilangan)

