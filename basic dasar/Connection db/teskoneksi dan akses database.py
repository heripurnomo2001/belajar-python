# Tes koneksi database mysql

import mysql.connector

# Coba koneksi
try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='u9235928_mysys'
    )
    print("Koneksi Berhasil!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
        


# membuat cursor untuk eksekusi perintah SQL
mycursor = mydb.cursor()

try:
    # Menjalankan perintah SQL untuk memilik kolom accountnum, name, dan address dari tabel custtable
    mycursor.execute("SELECT accountnum, name, left(address,100) as address FROM custtable limit 0,10")

    # Mendapatkan nama kolom dari metadata cursor
    column_names = [desc[0] for desc in mycursor.description]    

    # Mendapatkan semua hasil dari perintah SQL
    results = mycursor.fetchall()

    # Menghitung lebar maksimum untuk setiap kolom
    max_lengths = [len(column) for column in column_names]
    for row in results:
        for i, value in enumerate(row):
            max_lengths[i] = max(max_lengths[i], len(str(value)))
            

    # Menampilkan header
    header = " | ".join(f"{column:{max_lengths[i]}}" for i, column in enumerate(column_names))
    print("-" * len(header)) # Garis pemisah untuk header
    print(header)
    print("-" * len(header)) # Garis pemisah untuk header


    # Menampilkan isi tabel
    for row in results:
        row_data = " | ".join(f"{str(value):{max_lengths[i]}}" for i, value in enumerate(row))
        print(row_data)
    
    print("-" * len(header)) # Cetak garis penutup tabel
        
                     
except mysql.connector.Error as err:
    print(f"Error: {err}")


