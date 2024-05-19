# Dictionary and counter in Python to find winner of election

'''
Instruksi ini meminta untuk menganalisis sebuah array yang berisi
nama-nama kandidat dalam sebuah pemilihan. Setiap nama kandidat
dalam array ini merepresentasikan suara yang diberikan kepada
kandidat tersebut. Tugasnya adalah mencetak nama kandidat yang
mendapatkan suara maksimal. Jika terjadi hasil imbang, maka cetak
nama kandidat yang leksikografis lebih kecil.

Misalnya, jika kita memiliki array ["Alice", "Bob", "Charlie",
"Bob", "Alice", "Alice"], kita harus mencetak "Alice" karena dia
adalah kandidat yang menerima suara terbanyak. Jika ada imbang,
misalnya ["Alice", "Bob", "Charlie", "Bob", "Alice", "Charlie"],
kita harus mencetak "Alice" karena meskipun dia mendapatkan jumlah
suara yang sama dengan "Charlie," namun "Alice" lebih kecil secara
leksikografis daripada "Charlie."

Apakah ini yang kamu perlukan, atau ada yang perlu ditambahkan?
'''

# Pendekatan

'''

Pendekatannya sangat sederhana,

1. Konversi daftar suara yang diberikan menjadi kamus menggunakan metode
Counter(iterator). Kita akan memiliki kamus yang memiliki nama-nama
kandidat sebagai Kunci dan frekuensi mereka (jumlah) sebagai Nilai.

2. Karena lebih dari 1 kandidat dapat mendapatkan jumlah suara yang
sama dan dalam situasi ini kita perlu mencetak nama yang lebih kecil
secara leksikografis, maka sekarang kita akan membuat kamus lain
dengan menjelajahi kamus yang dibuat sebelumnya, jumlah suara akan
menjadi Kunci dan nama-nama kandidat akan menjadi Nilai.

3. Sekarang cari nilai suara maksimum yang diberikan untuk seorang kandidat
dan dapatkan daftar kandidat yang dipetakan pada nilai tersebut.

4. Sortir daftar kandidat yang memiliki jumlah suara maksimum yang
sama dan cetak elemen pertama dari daftar yang diurutkan untuk
mencetak nama yang lebih kecil secara leksikografis.
'''

# Panggil library collections
from collections import Counter

# Membuat fungsi menenetukan pemenang berdasarkan jumlah vote
def winner(input):
    votes = Counter(input)

    # create another dictionary and it's key will 
    # be count of votes values will be name of 
    # candidates
    dict = {}
    for value in votes.values():
        # initialize empty list to each key to 
        # insert candidate names having same 
        # number of votes
        dict[value] = [] 

    for (key, value) in votes.items():
        dict[value].append(key)

    # Mengurutkan dengan urutan besar-kecil (DESC)
    # untuk mendapatkan vote terbesar
    pemenang = sorted(dict.keys(),reverse=True)[0] 
    return votes, dict, pemenang

# Driver program
if __name__ == "__main__":
    input = ["Azis", "Sardi", "Azis", "Ahmad", "Azis", "Azis", "Azis",
             "Ahmad", "Azis", "Ahmad", "Azis", "Azis", "Azis", "Ahmad"]

    votes, dict, pemenang = winner(input)

    nama_pemenang = dict[pemenang]

    print("Votes: ", votes)
    print("Dict: ", dict)
    print(f"Pemenangnya adalah: {nama_pemenang} dengan jumlah vote: {pemenang}")
