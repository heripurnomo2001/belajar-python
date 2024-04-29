# PENGGUNAAN extend()

'''
Berbeda dengan append() dan insert(),
extext() mengizinkan untuk menambahkan elemen lebih dari 2,
dengan mengirimkan isi / parameter lebih dari 2.
'''


# Contoh
list = [1,2,3,4]
print("List sebelum diextend(): ", list)

listnew = [1,7,8,"i", "love", "you", True]

# Menbambah elemen dengan banyak isi element lebih dari 2
list.extend(listnew)

print("List setelah diextend() dengan listnew: ", list)
      
