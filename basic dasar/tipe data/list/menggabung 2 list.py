# MENGGABUNG 2 LIST

'''
Tantangan Gabung List:
Buatlah dua list, list1 dan list2, yang berisi beberapa bilangan bulat.
Gabung kedua list tersebut menjadi satu list baru dengan nama list_gabungan.
Urutkan list_gabungan dari nilai terkecil ke terbesar, lalu tampilkan isi
dari list_gabungan.
'''

list1 = [0,3,4,5,6,10,30]
list2 = [1,9,2,7,11,20,25]

list_gabungan = list1 + list2

list_gabungan.sort()

print("List gabungan setelah diurutkan: ", list_gabungan)
