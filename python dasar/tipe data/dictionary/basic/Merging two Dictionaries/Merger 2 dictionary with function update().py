# Menggabung dua dictionary dengan fungsi update()


# Buat Fungsi
def returnMerge(dict1, dict2):
    dict2.update(dict1)
    return dict2

# Driver Code
dict1 = {'a': 2, 'b': 5, 'e': 10, 'z':67}
dict2 = {'f': 20, 'h': 55, 'r': 23}

# Menampilkan dictionary 
print("Dict 1: ", dict1)
print("Dict 2: ", dict2)

# Memanggil fungsi
gabDict = returnMerge(dict1, dict2)

# Menampilkan penggabungan
print("\nPenggabungan Dict 1 dan Dict 2: ", gabDict)
