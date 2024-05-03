# Count occurrences of an element in a list
# ( Menghitung berapa kali suatu elemen muncul dalam sebuah list )

# Metode : menggunakan sebuah LOOP

# Fungsi menghitung element
def HitungX(list, x):
    hslhitung = 0
    for element in list:
        if element == x:
            hslhitung += 1
    return hslhitung


# Driver Code ( Menguji sebuah fungsi atau code )
list = [ 1, 9, 2, 20, 30, 40,1, 2, 9, 30, 3, 100, 20, 40, 20, 20, 20 ]
x = 20

# Tampilkan list
print("List yang diuji adalah: ", list)
print("{} ada di dalam List sebanyak {} kali".format(x, HitungX(list, x)))
print("\nTekan Enter untuk keluar...")




