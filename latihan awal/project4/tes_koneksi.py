import mysql.connector
try:
    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='bidan')

    # Membuat objek cursor
    cursor = cnx.cursor()

    # Mengeksekusi perintah SQL untuk memeriksa koneksi
    cursor.execute("SELECT 1")

    # Mengambil hasil
    result = cursor.fetchone()

    # Menampilkan pesan jika koneksi berhasil
    if result:
        print("Koneksi berhasil!")


        query = ("SELECT nik,name FROM mstbidan ")    
        cursor.execute(query)

        for (nik, name) in cursor:
            print(nik, name)

    # Menutup kursor dan koneksi
    cursor.close()    

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    # Menutup koneksi
    try:
        cnx.close()
    except NameError:
        pass  # Jika koneksi belum terbuka, lewati saja


