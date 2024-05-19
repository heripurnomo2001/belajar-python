import os
import pyodbc    
from datetime import date, timedelta
from database_connection_sqlserver import test_connection
from colorama import Fore, Back, Style, init



def bersih_layar():
    # Membersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'çlear')
def init_database():
    server = '10.1.1.64'
    database = 'DataCollaboration'
    username = 'IT50'
    password = '64CollabPST'
    return server, database, username, password

def datajualharian():
    # Cek apakah saat ini berada pada waktu server sibuk ( sedang update data penjualan )
    cek_waktu, waktu_kini = batasan_waktu()

    if cek_waktu == 'y':      
        # Panggil fungsi untuk menginisialisasi nilai variabel database
        server, database, username, password = init_database()

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
            
            ## Header dengan tanggal penjualan
            #header = f"Data Penjualan Hari ini: {tanggal.strftime('%d %B %Y')}"

            #Header
            header = ['CABANG', 'KWANTUM']
            header_format = '{:<25}  {:<15}'.format(*header)

            # Tambahkan garis pemisah
            panjang_garis = 34
            line = '-'* panjang_garis
            

            # Cetak garis pemisah dan header
            print(line)
            print(header_format)
            print(line)
            grand_total = 0
            width = 19
            for row in rows:
                cabang = row.cabang
                total = row.total
                grand_total += total
                formatted_number = "{:,}".format(int(total))
                
                ## Tentukan lebar yang diinginkan untuk string            
                #print(f"Cabang: {cabang}, Total: {formatted_number.rjust(width)}")
                #formatted_gt_number = "{:,}".format(int(grand_total))
    
                # Tentukan lebar yang diinginkan untuk string            
                print(f"{cabang}     {formatted_number.rjust(width)}")
            formatted_gt_number = "{:,}".format(int(grand_total))       
            print(line)
            spasi = " " * 11
            #print(f"Total Nasional: {spasi}{formatted_gt_number.rjust(width)}")
            print(f"Total:         {formatted_gt_number.rjust(width)}")
            print(line)
            # Tutup cursor dan koneksi
            cursor.close()
            conn.close()

        else:
            print("Koneksi gagal. Tidak dapat menampilkan data penjualan")
    else:
        info_server = info_svr(waktu_kini) 
        print(info_server)
        
def batasan_waktu():
    from datetime import datetime
    
    # Mendapatkan waktu saat ini
    current_time = datetime.now()

    # Mendapatkan nilai menit dari waktu saat ini
    current_minute = current_time.minute

    
    
    # memeriksa apakah menit saat ini lebih dari 45 atau kurang dari 05
    if current_minute == 45 or current_minute == 15:
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
        
        # Panggil fungsi untuk menginisialisasi nilai variabel database
        server, database, username, password = init_database()

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

            bersih_layar() # Sebelum mencetak report layar dibersihkan

            # Tambahkan garis pemisah
            panjang_garis = 34
            line = '-'* panjang_garis
            print("\n")
            print("PT. PENERBIT ERLANGGA")
            print("DATA PENJUALAN ")            
            print(f"Tanggal : {tanggal1:%d %B %Y} -s/d-")
            print(f"Tanggal : {tanggal2:%d %B %Y}")


            #Header
            header = ['CABANG', 'KWANTUM']
            header_format = '{:<25}  {:<15}'.format(*header)

            grand_total = 0
            width = 19        

            print(line)
            print(header_format)
            print(line)
            
            for row in rows:
                cabang = row.cabang
                total = row.total
                grand_total += total
                formatted_number = "{:,}".format(int(total))
                
                # Tentukan lebar yang diinginkan untuk string            
                print(f"{cabang}     {formatted_number.rjust(width)}")
            formatted_gt_number = "{:,}".format(int(grand_total))    
            print(line)
            print(f"Total:         {formatted_gt_number.rjust(width)}")
            print(line)
            print('\n')
            # Tutup cursor dan koneksi
            cursor.close()
            conn.close()
            
        else:
            print("Koneksi gagal. Tidak dapat menampilkan data penjualan")

    else:
        info_server = info_svr(waktu_kini) 
        print(info_server) 
def topproduk():
    
    # Cek apakah saat ini berada pada waktu server sibuk ( sedang update data penjualan )
    cek_waktu, waktu_kini = batasan_waktu()

    # Panggil fungsi untuk menginisialisasi nilai variabel database
    server, database, username, password = init_database()

    # Panggil fungsi untuk menguji koneksi
    test_result, connection_string = test_connection(server, database, username, password)

    if cek_waktu == 'y' and test_result:                                                
        try:
            # Buat objek koneksi
            conn = pyodbc.connect(connection_string) 

            # Eksekusi query
            query = f'''
                SELECT TOP 10 a.kodbuk, b.itemname, b.agr_itemlevel AS kelas, b.agr_gradename AS jenjang,
                SUM(a.kwantum) AS kwantum 
                FROM invoice a 
                INNER JOIN item b ON a.kodbuk = b.itemid
                WHERE thlap = 2024 AND type = 'SALES'
                GROUP BY a.kodbuk, b.itemname, b.agr_itemlevel, b.agr_gradename 
                ORDER BY kwantum DESC
                '''
            cursor = conn.cursor()
            # Menampilkan pesan bahwa query sedang dieksekusi
            print("Sedang memproses query...")
            # Menjalankan query    
            cursor.execute(query)

            # Menampilkan pesan setelah query selesai
            print("Query selesai.")
        except Exception as e:
            print("Terjadi kesalahan saat menjalankan perintah execute:")
            print(str(e))

        # Ambil semua baris hasil query
        rows = cursor.fetchall()

        bersih_layar() # Sebelum mencetak report layar dibersihkan
            
        # Header dengan tanggal penjualan
        header = f"10 Top Produk "

        # Tambahkan garis pemisah
        panjang_garis = 101
        line = '-'* panjang_garis
        print("\n")
    
        print("PT. PENERBIT ERLANGGA")
        print("10 Top Produk")            
        width = 19
            
        #Header
        header = ['KODE BUKU', 'JUDUL', 'KWANTUM']
        header_format = '{:<20} {:<72} {:<20}'.format(*header)
                
        #cetak header_format
        print(line)
        print(header_format)
        print(line)
        for row in rows:
            kodbuk = row.kodbuk
            itemname = row.itemname
            kwantum = row.kwantum
                
            formatted_number = "{:,}".format(int(kwantum))
                
            # Tentukan lebar yang diinginkan untuk string            
            print(f"{kodbuk} {itemname} {formatted_number.rjust(width)}")
               
        print(line)
        print('\n')
        #input("Tekan sembarang tombol untuk meninggalkan program.")
        # Tutup cursor dan koneksi
        cursor.close()
        conn.close()           

    else:
        info_server = info_svr(waktu_kini) 
        print(info_server) 

def info_svr(waktu_kini):
    pesan = f"Waktu saat ini adalah: {waktu_kini:%H:%M:%S}. Maaf proses belum bisa dilanjutkan, karena server sedang sibuk update data penjualan! Coba lagi di menit ke-6."
    info = Style.BRIGHT + Fore.RED + pesan
    return info

def topcustomer():
    # Cek apakah saat ini berada pada waktu server sibuk ( sedang update data penjualan )
    cek_waktu, waktu_kini = batasan_waktu()

    # Panggil fungsi untuk menginisialisasi nilai variabel database
    server, database, username, password = init_database()

    # Panggil fungsi untuk menguji koneksi
    test_result, connection_string = test_connection(server, database, username, password)

    if cek_waktu == 'y' and test_result:                                                
        try:
            # Buat objek koneksi
            conn = pyodbc.connect(connection_string) 

            # Eksekusi query
            query = f'''
            select top 10 c.cabang, a.kodlan, b.AGR_SCHOOLID as sekolah,b.agr_gradeid as jenjang,b.county as county,b.city, sum(a.kwantum) as kwantum 
            from invoice a 
            inner join customer b on a.kodlan = b.accountnum
            inner join salesinvmap c on a.nofak = c.invoiceid
            where thlap=2024 and type='SALES'
            group by c.cabang, a.kodlan,b.AGR_SCHOOLID,b.agr_gradeid,b.county,b.city order by kwantum desc
            '''        
            cursor = conn.cursor()
            # Menampilkan pesan bahwa query sedang dieksekusi
            print("Sedang memproses query...")
            # Menjalankan query    
            cursor.execute(query)

            # Menampilkan pesan setelah query selesai
            print("Query selesai.")
        except Exception as e:
            print("Terjadi kesalahan saat menjalankan perintah execute:")
            print(str(e))

        # Ambil semua baris hasil query
        rows = cursor.fetchall()

        bersih_layar() # Sebelum mencetak report layar dibersihkan
            
        # Header dengan tanggal penjualan
        header = f"10 Top Customer "

        # Tambahkan garis pemisah
        panjang_garis = 91
        line = '-'* panjang_garis
        print("\n")
    
        print("PT. PENERBIT ERLANGGA")
        print("10 Top Customer")            
        width = 19
            
        #Header
        header = ['KODLAN', 'NAMA PELANGGAN', 'CABANG', 'KWANTUM']
        header_format = '{:<15} {:<50} {:<16} {:<15}'.format(*header)
                
        #cetak header_format
        print(line)
        print(header_format)
        print(line)
        for row in rows:
            cabang = row.cabang[0:4]    
            kodlan = row.kodlan[0:15]
            sekolah = row.sekolah[0:50]
            kwantum = row.kwantum
                
            formatted_number = "{:,}".format(int(kwantum))
                
            # Tentukan lebar yang diinginkan untuk string            
            print(f"{kodlan} {sekolah} {cabang} {formatted_number.rjust(width)}")
               
        print(line)
        print('\n')
        #input("Tekan sembarang tombol untuk meninggalkan program.")
        # Tutup cursor dan koneksi
        cursor.close()
        conn.close()           

    else:
        info_server = info_svr(waktu_kini) 
        print(info_server)        

def topsalesman():
    # Cek apakah saat ini berada pada waktu server sibuk ( sedang update data penjualan )
    cek_waktu, waktu_kini = batasan_waktu()

    # Panggil fungsi untuk menginisialisasi nilai variabel database
    server, database, username, password = init_database()

    # Panggil fungsi untuk menguji koneksi
    test_result, connection_string = test_connection(server, database, username, password)

    if cek_waktu == 'y' and test_result:                                                
        try:
            # Buat objek koneksi
            conn = pyodbc.connect(connection_string) 

            # Eksekusi query
            query = f'''
                select top 10 c.cabang, a.kodsal,d.name, sum(a.kwantum) as kwantum 
                from invoice a 
                inner join employee b on a.kodsal = b.emplid
                inner join dirparty d on b.partyid = d.partyid
                inner join salesinvmap c on a.nofak = c.invoiceid
                where thlap=2024 and type='SALES'
                group by c.cabang, a.kodsal,d.name order by kwantum desc
            '''        
            cursor = conn.cursor()
            # Menampilkan pesan bahwa query sedang dieksekusi
            print("Sedang memproses query...")
            # Menjalankan query    
            cursor.execute(query)

            # Menampilkan pesan setelah query selesai
            print("Query selesai.")
        except Exception as e:
            print("Terjadi kesalahan saat menjalankan perintah execute:")
            print(str(e))

        # Ambil semua baris hasil query
        rows = cursor.fetchall()

        bersih_layar() # Sebelum mencetak report layar dibersihkan
            
        # Header dengan tanggal penjualan
        header = f"10 Top Customer "

        # Tambahkan garis pemisah
        panjang_garis = 75
        line = '-'* panjang_garis
        print("\n")
    
        print("PT. PENERBIT ERLANGGA")
        print("10 Top Salesman")            
        width = 19
            
        #Header
        header = ['KODSAL', 'NAMA', 'CABANG', 'KWANTUM']
        header_format = '{:<10} {:<30} {:<16} {:<15}'.format(*header)
                
        #cetak header_format
        print(line)
        print(header_format)
        print(line)
        for row in rows:
            cabang = row.cabang[0:4]    
            kodsal = row.kodsal[0:10]
            salesman = row.name[:30]
            if len(salesman) < 30:
                kr_spasi = 30 - len(salesman)
                spasi = " " *kr_spasi 
                salesman = salesman + spasi
            kwantum = row.kwantum
                
            formatted_number = "{:,}".format(int(kwantum))
                
            # Tentukan lebar yang diinginkan untuk string            
            print(f"{kodsal} {salesman} {cabang} {formatted_number.rjust(width)}")
               
        print(line)
        print('\n')
        #input("Tekan sembarang tombol untuk meninggalkan program.")
        # Tutup cursor dan koneksi
        cursor.close()
        conn.close()           

    else:
        info_server = info_svr(waktu_kini) 
        print(info_server)        


if __name__ == "__main__":
    main()
        
