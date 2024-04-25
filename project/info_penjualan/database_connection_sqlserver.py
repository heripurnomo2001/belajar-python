# Tes Koneksi SQL Server DB

import pyodbc

def test_connection(server, database, username, password):
    try:
        # Buat string koneksi
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"            
            f"UID={username};"
            f"PWD={password};"
        )

        # Buat objek koneksi
        conn = pyodbc.connect(conn_str)

        # Cetak status koneksi berhasil        
        # print("Koneksi berhasil!")

        # Tutup koneksi
        conn.close()

        # Kembalikan nilai True jika berhasil
        return True, conn_str

    except pyodbc.Error as e:
        # Tangani error saat koneksi gagal
        print(f"Koneksi gagal: {e}")

        # Kembalikan nilai False jika berhasil
        return False, conn_str
