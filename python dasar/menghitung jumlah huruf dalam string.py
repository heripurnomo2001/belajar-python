# MENGHITUNG JUMLAH HURUF DALAM SEBUAH KATA

mydic = {}

#entry form
kata = input("Masukkan string: " )

# nested loop
for huruf in kata:
    jumlah = kata.count(huruf)
    mydic[huruf] = jumlah

print("Output : ")
for key, value in mydic.items():
    print(f"{key}: {value}")

          
