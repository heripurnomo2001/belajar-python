import pyodbc
import locale
from datetime import date 
from database_connection_sqlserver import test_connection

# Memberikan nilai untuk argumen-argumen yang diperlukan
server = '10.1.1.64'
database = 'DataCollaboration'
username = 'IT50'
password = '64CollabPST'

# Panggil fungsi untuk menguji koneksi
test_result, connection_string = test_connection(server, database, username, password)

if test_result:    
    # Buat objek koneksi
    conn = pyodbc.connect(connection_string)
    
    # Dapatkan tanggal hari ini
    tanggal = date.today()

    # Eksekusi query
    query = f"SELECT b.cabang, SUM(a.total) AS total FROM invoice a INNER JOIN salesinvmap b ON a.nofak = b.invoiceid WHERE tglfak = ? GROUP BY b.cabang"    
    cursor = conn.cursor()
    # print("Sedang mencoba menjalankan query: ")    
    try:
        cursor.execute(query, tanggal)
        print("Perintah execute berhasil dieksekusi.")
    except Exception as e:
        print("Terjadi kesalahan saat menjalankan perintah execute:")
        print(str(e))
    
    # Ambil semua baris hasil query
    rows = cursor.fetchall()
    
    # Header dengan tanggal penjualan
    header = f"Data Penjualan Tanggal: {tanggal.strftime('%d %B %Y')}"

    # Tambahkan garis pemisah
    panjang_garis = len(header)+5
    line = '-'* panjang_garis

    # Cetak garis pemisah dan header
    print(line)
    print(header)
    print(line)
    
    for row in rows:
        cabang = row.cabang
        total = row.total
        formatted_number = "{:,}".format(total)

        # Tentukan lebar yang diinginkan untuk string
        width = 15
        print(f"Cabang: {cabang}, Total: {formatted_number.rjust(width)}")

    # Tutup cursor dan koneksi
    cursor.close()
    conn.close()

else:
    print("Koneksi gagal. Tidak dapat menampilkan data penjualan")




    




