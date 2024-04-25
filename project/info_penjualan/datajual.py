def datajualharian():
    # Cek apakah saat ini berada pada waktu server sibuk ( sedang update data penjualan )
    cek_waktu, waktu_kini = batasan_waktu()

    if cek_waktu == 'y':      
        import pyodbc    
        from datetime import date, timedelta
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
            #tanggal = date.today() -  timedelta(days=1)
            tanggal = date.today() 

            # Eksekusi query
            query = f"SELECT b.cabang, SUM(a.total) AS total FROM invoice a INNER JOIN salesinvmap b ON a.nofak = b.invoiceid WHERE tglfak = ? AND type='SALES' GROUP BY b.cabang"    
            cursor = conn.cursor()
            print("PT. PENERBIT ERLANGGA")
            print("DATA PENJUALAN HARIAN")
            print(f"Tanggal: {tanggal} \n")
            
            
            try:
                # Menjalankan query    
                cursor.execute(query, tanggal) 
            except Exception as e:
                print("Terjadi kesalahan saat menjalankan perintah execute:")
                print(str(e))
            
            # Ambil semua baris hasil query
            rows = cursor.fetchall()
            
            # Header dengan tanggal penjualan
            header = f"Data Penjualan Hari ini: {tanggal.strftime('%d %B %Y')}"

            # Tambahkan garis pemisah
            panjang_garis = len(header)+8
            line = '-'* panjang_garis

            # Cetak garis pemisah dan header
            print(line)
            print(header)
            print(line)

            grand_total = 0
            width = 19
            for row in rows:
                cabang = row.cabang
                total = row.total
                grand_total += total
                formatted_number = "{:,}".format(int(total))
                
                # Tentukan lebar yang diinginkan untuk string            
                print(f"Cabang: {cabang}, Total: {formatted_number.rjust(width)}")
            formatted_gt_number = "{:,}".format(int(grand_total))    
            print(line)
            spasi = " " * 11
            print(f"Total Nasional: {spasi}{formatted_gt_number.rjust(width)}")
            print(line)
            # Tutup cursor dan koneksi
            cursor.close()
            conn.close()

        else:
            print("Koneksi gagal. Tidak dapat menampilkan data penjualan")
            

def batasan_waktu():
    from datetime import datetime
    
    # Mendapatkan waktu saat ini
    current_time = datetime.now()

    # Mendapatkan nilai menit dari waktu saat ini
    current_minute = current_time.minute

    
    
    # memeriksa apakah menit saat ini lebih dari 45 atau kurang dari 05
    if current_minute >= 45 or current_minute < 5:
        return 'n', current_time
    else:
        return 'y', current_time

def input_tanggal(tg):
    from datetime import datetime
    
    # Dapatkan tanggal 
    while True:
        try:
            tanggal_str = input(f"Masukkan {tg} (Format: DD/MM/YYYY): ")                
            tanggal = datetime.strptime(tanggal_str,'%d/%m/%Y').date()
            return tanggal
            break                
        except ValueError as e:
            print(f"Data tanggal yang anda masukkan tidak valid. Kesalahan: {e}" )

def datajual_periode():
    # Cek apakah saat ini berada pada waktu server sibuk ( sedang update data penjualan )
    cek_waktu, waktu_kini = batasan_waktu()

    if cek_waktu == 'y':                    
        import pyodbc
        import locale
        from datetime import date, timedelta, datetime  
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

            # Masukkan periode tanggal
            tanggal1 = input_tanggal('tanggal 1')
            tanggal2 = input_tanggal('tanggal 2')
                                                                                                           
            # Eksekusi query
            query = f"SELECT b.cabang, SUM(a.total) AS total FROM invoice a INNER JOIN salesinvmap b ON a.nofak = b.invoiceid WHERE a.tglfak BETWEEN ? AND ? AND type='SALES' GROUP BY b.cabang"    
            cursor = conn.cursor()
                             
            try:
                # Menampilkan pesan bahwa query sedang dieksekusi
                print("Sedang memproses query...")
                # Menjalankan query    
                cursor.execute(query, tanggal1, tanggal2)

                # Menampilkan pesan setelah query selesai
                print("Query selesai.")
            except Exception as e:
                print("Terjadi kesalahan saat menjalankan perintah execute:")
                print(str(e))
            
            # Ambil semua baris hasil query
            rows = cursor.fetchall()
            
            # Header dengan tanggal penjualan
            header = f"Data Penjualan Tanggal: {tanggal1.strftime('%d %B %Y')}"

            # Tambahkan garis pemisah
            panjang_garis = len(header)+8
            line = '-'* panjang_garis
            print("\n")
            print(line)
            print("PT. PENERBIT ERLANGGA")
            print("DATA PENJUALAN HARIAN")            
            print(f"Tanggal : {tanggal1:%d %B %Y} -s/d-")
            print(f"Tanggal : {tanggal2:%d %B %Y}")
            print(line)

            # Cetak garis pemisah dan header
            #print(line)
            #print(header)
            #print(line)

            grand_total = 0
            width = 19


            
            for row in rows:
                cabang = row.cabang
                total = row.total
                grand_total += total
                formatted_number = "{:,}".format(int(total))
                
                # Tentukan lebar yang diinginkan untuk string            
                print(f"Cabang: {cabang}, Total: {formatted_number.rjust(width)}")
            formatted_gt_number = "{:,}".format(int(grand_total))    
            print(line)
            spasi = " " * 11
            print(f"Total Nasional: {spasi}{formatted_gt_number.rjust(width)}")
            print(line)
            print('\n')
            # Tutup cursor dan koneksi
            cursor.close()
            conn.close()
            

        else:
            print("Koneksi gagal. Tidak dapat menampilkan data penjualan")

    else:
        print(f"Waktu saat ini adalah: {waktu_kini:%H:%M:%S}. Maaf proses belum bisa dilanjutkan, karena server sedang sibuk update data penjualan! Coba lagi di menit ke-6.")        
      
        
if __name__ == "__main__":
    main()
        
