# MENCETAK BILANGAN PRIMA
# METODE IMPORT LIBRARY


# import library
import sympy 

# entry bilangan
bilangan = int(input("Masukkan batas bilangan : "))


# nested loop
print(f"Bilangan prima dari 2 sampai {bilangan} adalah : ")
for angka in range(2,bilangan+1):
    prime = True
    if not sympy.isprime(angka):
        prime = False
    else:
        prime = True
        print(angka, end=" ")
        
        


    
    
