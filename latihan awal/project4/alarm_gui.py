# import modul tk
import tkinter as tk
from tkinter import ttk
import datetime
import pygame


# validasi
validasi_jam = ['{:02d}'.format(i) for i in range(24)]
validasi_menit = ['{:02d}'.format(i) for i in range(60)]

window = tk.Tk()
window.configure(bg='white')
window.title("Alarm Sederhana")
window.geometry('600x400')

# input frame
input_frame = ttk.Frame(window)
# penempatan Grid, Pad dan Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)


def show_notification(message):
    popup = tk.Toplevel()
    popup.title("Notifikasi")
    label = tk.Label(popup, text = message)
    label.pack(padx=20, pady=10)
    close_button = tk.Button(popup, text="Close", command = popup.destroy)
    close_button.pack(padx=5)


def validate_jam(event):
    INPUT_JAM_VALUE = INPUT_JAM.get()
    if INPUT_JAM_VALUE not in validasi_jam:
        show_notification("Jam yang anda input tidak valid!")


def validate_menit(event):
    INPUT_MENIT_VALUE = INPUT_MENIT.get()
    if INPUT_MENIT_VALUE not in validasi_menit:
        show_notification("Menit yang anda input tidak valid!")
   

#label jam 
input_jam_label = ttk.Label(input_frame,text="Masukkan Jam : ")
input_jam_label.pack(padx=10, fill="x",expand=True)

#entri jam
INPUT_JAM = tk.StringVar()
input_jam_entry = ttk.Entry(input_frame, textvariable=INPUT_JAM)
input_jam_entry.pack(padx=10, fill='x', expand=True)
input_jam_entry.bind("<FocusOut>", lambda event: validate_jam(event))  # Binding event FocusOut ke fungsi validate_jam


#label  menit
input_menit_label = ttk.Label(input_frame,text="Masukkan Menit : ")
input_menit_label.pack(padx=10, fill="x",expand=True)

#entri menit
INPUT_MENIT = tk.StringVar()
input_menit_entry = ttk.Entry(input_frame, textvariable=INPUT_MENIT)
input_menit_entry.pack(padx=10, fill='x', expand=True)
input_menit_entry.bind("<FocusOut>", lambda event: validate_menit(event))  # Binding event FocusOut ke fungsi validate_menit

played_alarm = 0  # Pindahkan inisialisasi ini ke luar fungsi set_alarm
def set_alarm():
    global played_alarm  # Tambahkan ini untuk mengakses variabel played_alarm yang ada di luar fungsi
    pygame.init()
    pygame.mixer.init()
    alarm_sound = pygame.mixer.Sound("alarmku.flac")
    try:                
        INPUT_JAM_VALUE = 0  # Inisialisasi nilai default
        INPUT_MENIT_VALUE = 0  # Inisialisasi nilai default
                
        now = datetime.datetime.now()
        cur_jam = now.hour
        cur_menit = now.minute
        
        if INPUT_JAM_VALUE != '' and INPUT_MENIT_VALUE != '':  # Memastikan input tidak kosong
            # show_notification("data input tidak kosong")
            INPUT_JAM_VALUE = int(INPUT_JAM.get())    # Ambil nilai jam dari input
            INPUT_MENIT_VALUE = int(INPUT_MENIT.get())  # Ambil nilai menit dari input
            if INPUT_JAM_VALUE == cur_jam and INPUT_MENIT_VALUE == cur_menit:                                         
                alarm_sound.play()       
                pygame.time.wait(int(alarm_sound.get_length() * 1000))   # Menunggu sampai alarm selesai diputar
                played_alarm += 1
                show_notification("bunyi alaram ke " +str(played_alarm)+" kali")
                pygame.time.wait(1000)
            else:                
                # Jadwalkan pemanggilan set_alarm setelah 1 detik lagi
                window.after(1000, set_alarm)
        else:
            show_notification("data input kosong")

    except pygame.error as e:
        show_notification("error saat memainkan audio", str(e))    

    if played_alarm < 3:
        window.after(1000, set_alarm)
    else:
        submit_button.config(state="disabled")  
        played_alarm = 0   

#button untuk memanggil function check_input

submit_button = ttk.Button(input_frame, text="Submit", command=set_alarm)
submit_button.pack()

if __name__ == "__main__":
    window.mainloop()
   
