# MENGHAPUS DENGAN DEL


'''
'del' adalah perintah python
ini bisa digunakan untuk menghapus :
    - variabel list  -> del list  : maka variabel bernama list akan dihapus
    - dengan slicing ->
      list = [1,2,3,4,5,6,7]
      dele list[3:5] -> menghapus 4,5

      hasil : list = [1,2,3,6,7]
'''


list = [1,2,3,4,5,6,7,8,9,10]

print("Data list sebelum dihapus 'list = [1,2,3,4,5,6,7,8,9,10]':", list)

# Hapus elemen ke 2 sampai dengan 5
del list[2:6]

print("Data list setelah dihapus." , list)
