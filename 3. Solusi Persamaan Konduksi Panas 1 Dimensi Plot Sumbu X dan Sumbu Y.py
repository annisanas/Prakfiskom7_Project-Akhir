#No.3 by Annisa Nurlaili Aulia Safitri
#Plot sumbu X dan sumbu Y

import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 500 # Koefisien Difusivitas Termal [m^2/s]
panjang = 2.5 # Panjang plat [m]
waktu = 1.5 # Waktu simulasi [s]
node = 50 # Jumlah titik grid

dx = panjang / node # Jarak antar titik grid [m]
dt = 0.5 * dx**2 / a # Ukuran waktu simulasi [s]
t_n = int(waktu / dt) # Jumlah iterasi simulasi
u = np.zeros(node) + 20 # Suhu awal plat [degC]

# Kondisi Batas
u[0] = 0 # Suhu ujung kiri plat [degC]
u[-1] = 100 # Suhu ujung kanan plat [degC]

# Inisialisasi list untuk menyimpan nilai waktu dan suhu rata-rata
time_list = []
mean_temperature_list = []

# Simulasi
counter = 0
while counter <= waktu:
    w = u.copy()  # Menyalin data suhu untuk perhitungan
    for i in range(1, node-1):  # Melooping setiap titik grid kecuali batas
        u[i] = (dt * a * (w[i-1] - 2*w[i] + w[i+1]) / dx**2) + w[i]  # Perhitungan suhu baru berdasarkan persamaan difusi panas

    # Menambah nilai waktu dan suhu rata-rata ke dalam list
    time_list.append(counter)
    mean_temperature_list.append(np.mean(u))

    counter += dt  # Menambah waktu simulasi

# Membuat plot waktu vs suhu rata-rata
plt.plot(time_list, mean_temperature_list, label='Suhu Rata-rata')
plt.xlabel('Waktu (s)')
plt.ylabel('Suhu Rata-rata (°C)')
plt.title('Perubahan Suhu Rata-rata dari Waktu')
plt.legend()
plt.show()
