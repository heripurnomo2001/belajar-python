import matplotlib.pyplot as plt

# Data penjualan
tanggal = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei']
penjualan = [100, 120, 90, 110, 130]

# Plot grafik garis
plt.plot(tanggal, penjualan)

# Tambahkan label dan judul
plt.xlabel('Bulan')
plt.ylabel('Penjualan')
plt.title('Grafik Penjualan Bulanan')

# Tampilkan grafik di konsol
plt.show()
