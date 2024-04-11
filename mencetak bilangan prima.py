# -----------------------#
# MENCETAK BILANGAN PRIMA
# metode operator '%'
# -----------------------#
print("MENCETAK BILANGAN PRIMA")

# form entry
bilangan = int(input("Masukkan batas bilangan : "))

print(f"\nBilangan prima antara 2 dan {bilangan} : ")
for angka in range(2,bilangan+1):
    prime = True
    
    for pembagi in range(2,angka):
        cekprime = angka % pembagi
        if cekprime == 0: #jika 0, berarti bukan bilangan prima
            prime = False
            break
        
    if prime:
        print(angka, end=" ")
        
            
        
                
            
    
    
