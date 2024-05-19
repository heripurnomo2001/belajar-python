# find the sum of all items in a dictionary

'''
Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.

Examples: 

Input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600

Input : {‘x’: 25, ‘y’:18, ‘z’:45}
Output : 88
'''

# Membuat function penjumlahan
def returnSum(mydict):
    list = []
    for i in mydict:
        list.append(mydict[i])
    hasil_penjumlahan = sum(list)
    return hasil_penjumlahan

# Contoh dictionary
mydict = {'a':100, 'b': 200, 'c': 300}

# Memanggil fungsi penjumlahan
resultSum = returnSum(mydict)

# menampilkan dictionary dan hasil penjumlahan
print('Dictionary mydict: ', mydict)
print('Hasil Penjumlahan: ', resultSum)
