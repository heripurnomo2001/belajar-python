# Swap elements in String list

from colorama import Style, Fore 

# Redaksi asli soal
'''
Sometimes, while working with data records we can have a problem in which
we need to perform certain swap operation in which we need to change one
element with other over entire string list. This has application in
both day-day and data Science domain. Lets discuss certain ways in which
this task can be performed. 

Method #1 : Using replace() + list comprehension The combination of above
functionalities can be used to perform this task. In this, we iterate through
list using list comprehension and task of swapping is performed using
replace(). 
'''

# Terjemahan
'''
Tukar elemen dalam daftar String
Terakhir Diperbarui: 08 Mar, 2023
Terkadang, saat bekerja dengan catatan data kita dapat menghadapi masalah
di mana kita perlu melakukan operasi tukar tertentu di mana kita perlu
mengganti satu elemen dengan yang lain di seluruh daftar string. Hal ini
memiliki aplikasi di kedua domain sehari-hari dan ilmu data. Mari kita bahas
beberapa cara di mana tugas ini dapat dilakukan.
'''

# Pada metode pertama ini kita menggunakan :
# Using replace() + list comprehension
# list comprehension itu apa? googling atau chatgpt

# Menyiapkan contoh list
eksperimen_list = ['Andi', 'Joko', 'Bandi', 'Robi', 'Deri', 'Wiwid']


# Cetak list asli sebelum ditukar elemennya
print("Ini adalah list asli sebelum ditukar elemennya: ", eksperimen_list)

# Tukar elemen-elemen pada eksperimen list string di atas
res = [ sub.replace('A','E').replace('J','y').replace('a','e').replace('i','ee') for sub in eksperimen_list ]



# Cetak list setelah ditukar elemennya
print("Ini adalah list setelah ditukar elemennya: ", res)



input(Fore.CYAN + "\nTekan Enter untuk keluar...")
print(Style.RESET_ALL)





