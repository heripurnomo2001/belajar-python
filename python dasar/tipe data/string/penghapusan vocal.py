# Penghapusan Vokal:
'''    
Buat program yang mengambil input sebuah kata atau kalimat dari pengguna,
lalu hapus semua huruf vokal dari kata atau kalimat tersebut.
'''

def input_str():
    while True:
        string1 = input("\nMasukkan kata atau kalimat: ")
        if string1.strip(): # Jika string tidak kosong
            return string1
        else:
            print("Input kata atau kalimat tidak boleh kosong!")


while True:
    string = input_str()
    vocal = 'aiueoAIUEO'
    print("Kata atau kalimat sebelun dihapus vocal: ", string)
    for huruf in vocal:
        # print(huruf, end=", ")
        string = string.replace(huruf,"")
    print("Katau atau kalimat setelah dihapus vocal: ", string)
    
        


        
        
        
    
