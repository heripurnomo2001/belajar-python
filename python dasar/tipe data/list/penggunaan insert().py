# PENGGUNAAN FUNGSI insert()

'''
Selain append() , fungsi untuk menambah data ada insert().
Tapi berbeda dengan append(), insert() memiliki 2 argument,
insert(a,b) artinya, masukkan data ke-a dengan isi elemen b
'''

# Contoh

list = [1,2,3,4]
print("list sebelum diinsert", list)

list.insert(2,"Hallo")
print("list setelah insert(2, 'Hallo') adalah: ", list)
