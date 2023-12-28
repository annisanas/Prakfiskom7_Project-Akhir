#No. 4 by Annisa Nurlaili Aulia Safitri
#Perbandingan suhu antara t(0) dan t(1.5)

import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 150  # Koefisien Difusivitas Termal
panjang = 0.5  # Panjang plat [mm]
waktu = 1.5  # Waktu simulasi [s]
node = 50  # Jumlah titik grid

dx = panjang / node  # Jarak antar titik grid pada x [mm]
dy = panjang / node  # Jarak antar titik grid pada y [mm]
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))  # Ukuran langkah waktu [s] (pilih yang lebih kecil agar stabil)
t_nodes = int(waktu / dt)  # Jumlah iterasi simulasi
u = np.zeros((node, node)) + 20  # Suhu awal plat [degC] (2 dimensi)

# Kondisi batas
u[0, :] = 0  # Suhu tepi kiri (variasi linear)
u[-1, :] = 100  # Suhu tepi kanan (variasi linear)
u[:, 0] = np.linspace(0, 100, node)  # Suhu tepi bawah (variasi linear)
u[:, -1] = np.linspace(0, 100, node)  # Suhu tepi atas (variasi linear)

# Visualisasi distribusi suhu awal
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].set_ylabel("y (cm)")
ax[0].set_xlabel("x (cm)")
pcm1 = ax[0].pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
ax[0].set_title("Distribusi Suhu Awal")
plt.colorbar(pcm1, ax=ax[0])

# Inisialisasi array untuk menyimpan suhu rata-rata pada setiap iterasi
t_mean_values = []

# Simulasi
counter = 0
while counter <= waktu:
    w = u.copy()  # Menyalin data suhu untuk perhitungan
    # Looping setiap titik grid kecuali batas
    for i in range(1, node-1):
        for j in range(1, node-1):
            # Menghitung perubahan suhu berdasarkan persamaan Laplace 2D(menggunakan tetangga terdekat)
            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j]) / dx**2
            dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1]) / dy**2
            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]  # Suhu baru dihitung dan ditambahkan ke suhu lama

    t_mean = np.mean(u)
    t_mean_values.append(t_mean)  # Menyimpan suhu rata-rata pada setiap iterasi
    counter += dt  # Menambah waktu simulasi

  # Visualisasi distribusi suhu setelah waktu tertentu
    ax[1].clear()
    ax[1].set_ylabel("y (cm)")
    ax[1].set_xlabel("x (cm)")
    pcm2 = ax[1].pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
    ax[1].set_title(f"Distribusi Suhu pada t: {counter:.3f} s")
    cbar = plt.colorbar(pcm2, ax=ax[1])

    plt.pause(0.01)

# Plot antara waktu (Sumbu X) dan suhu rata-rata (Sumbu Y)
plt.figure()
plt.plot(np.arange(0, waktu+dt, dt), t_mean_values, label='Suhu Rata-rata')
plt.title('Perubahan Suhu Rata-rata terhadap Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Suhu Rata-rata (Celcius)')
plt.legend()
plt.grid(True)
plt.show()
