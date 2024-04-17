import time

# Menulis output tanpa menggunakan flush
print("Memulai proses...", end='')
time.sleep(2)  # Menunggu 2 detik
print("Selesai.")

# Menulis output dengan menggunakan flush
print("Memulai proses...", end='', flush=True)
time.sleep(2)  # Menunggu 2 detik
print("Selesai.")
