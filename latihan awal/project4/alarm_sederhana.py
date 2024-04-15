# ALARM SEDERHANA
import datetime
import time
import pygame

print("\033[96m====================  ALARM SEDERHANA ====================\033[0m")
print(" ")

# validasi_jam = []
# for i in range(0, 24):
#     jam = '{:02d}'.format(i)
#     validasi_jam.append(jam)
validasi_jam = ['{:02d}'.format(i) for i in range(24)]
validasi_menit = ['{:02d}'.format(i) for i in range(60)]

while True:
    input_jam = input(" Silahkan masukkan Jam : ")
    if input_jam in validasi_jam:
        break
    else:
        print("Jam yag anda masukkan tidak valid!")

while True:
    input_menit = input(" Silahkan masukkan Menit : ")
    if input_menit in validasi_menit:
        break
    else:
        print("Menit yag anda masukkan tidak valid!")
def set_alarm():
    pygame.init()
    pygame.mixer.init()
    alarm_sound = pygame.mixer.Sound("alarmku.flac")
    try:
        played_alarm = 0
        while played_alarm < 2:
            while True:
                now = datetime.datetime.now()
                cur_jam   = now.hour
                cur_menit = now.minute

                if int(input_jam) == cur_jam and int(input_menit) == cur_menit:
                    print('bunyikan alarm')
                    for _ in range(3):  # Mengulang alarm 3 kali
                        alarm_sound.play()       
                        pygame.time.wait(int(alarm_sound.get_length() * 1000))   # Menunggu sampai alarm selesai diputar
                    played_alarm +=1
                    pygame.time.wait(1000)
    except pygame.error as e:
        print("error saat memainkan audio", str(e))    

if __name__ == "__main__":
    set_alarm()
