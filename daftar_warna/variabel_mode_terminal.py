import subprocess
#import csv

# Jalankan perintah 'mode' dan tangkap outputnya
result = subprocess.run('mode', capture_output=True, text=True, shell=True)
print(result.stdout)

# Memecah output menjadi baris-baris
output_lines = result.stdout.split('\n')

# Mencari baris yang mengandung informasi "Columns: 120"
for line in output_lines:
    if 'Columns:' in line:
        # Memisahkan baris menjadi kata-kata
        words = line.split()
        if len(words) >= 2:
            columns = words[1]
            break
else:
    columns = None  # Jika informasi tidak ditemukan, set nilai columns menjadi None

print("Nilai kolom:", columns)
