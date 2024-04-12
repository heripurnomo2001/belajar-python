# MEMBALIKKAN KATA
# menggunakan slicing

# entry form
kata = input("Masukkan kata : ")

# iterasi
jmlhuruf = len(kata)
for i in range(jmlhuruf,0,-1):
    huruf = kata[i-1:i]
    print(huruf, end="")
    #print(i,end=" ")    
