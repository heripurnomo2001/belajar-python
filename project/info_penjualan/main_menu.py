import subprocess
#import windows_curses
import curses

def show_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "==== Aplikasi Console Penjualan =====")
    stdscr.addstr(2, 0, "1. Tampilkan Data Penjualan")
    stdscr.addstr(3, 0, "2. Option 2")
    stdscr.addstr(4, 0, "3. Option 3")
    stdscr.addstr(5, 0, "0. Keluar")
    stdscr.refresh()

    return stdscr.getch()    

def process_option(option):
    if option == ord('1'):
        print("Menampilkan data penjualan...")
        try:
            subprocess.run(["python","data_penjualan.py"]) # Menjalankan data penjualan
        except FileNotFoundError:
            print("File data_penjualan.py tidak ditemukan.")
        return
    if option == ord('2'):
        print("Anda memilih Option 2")
        # Tambahkan logika untuk Option 2 di sini
    if option == ord('3'):
        print("Anda memilih Option 3")
        # Tambahkan logika untuk Option 3 di sini
    if option == ord('0'):
        print("Keluar dari aplikasi")
    else:
        print("Pilihan tidak valid.")


def main(stdscr):
    curses.curs_set(0) # Sembunyikan kursor
    stdscr.clear()
    
    while True:
        option = show_menu(stdscr)        
        if option == ord('0'):
            break # Keluar dari loop jika pengguna memilih keluar

        process_option(choice)

        stdscr.getch() # Tunggu input untuk melanjutkan

curses.wrapper(main)
        
