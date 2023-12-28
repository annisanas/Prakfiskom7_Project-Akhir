#No.3 by Annisa Nurlaili Aulia Safitri
#Plot Perbandingan Suhu Antara t(0) dan t(1.5)

import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 500  # Koefisien Difusivitas Termal [m^2/s]
panjang = 2.5  # Panjang plat [m]
waktu = 1.5  # Waktu simulasi [s]
node = 50  # Jumlah titik grid

dx = panjang / node  # Jarak antar titik grid [m]
dt = 0.5 * dx**2 / a  # Ukuran waktu simulasi [s]
t_n = int(waktu / dt)  # Jumlah iterasi simulasi
u = np.zeros(node) + 20  # Suhu awal plat [degC]

# Kondisi Batas
u[0] = 0  # Suhu ujung kiri plat [degC]
u[-1] = 100  # Suhu ujung kanan plat [degC]

# Simpan distribusi suhu pada t=0
u_t0 = u.copy()

# Visualisasi pada t=0
fig, ax = plt.subplots()
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh([u_t0], cmap=plt.cm.jet, vmin=0, vmax=100)  # Plot distribusi suhu pada t=0
plt.colorbar(pcm, ax=ax)
ax.set_ylim([-2, 3])  # Batas skala y
ax.set_title("Distribusi Suhu pada t: 0.0 s")

# Simulasi
counter = 0
while counter <= waktu:
    w = u.copy()  # Menyalin data suhu untuk perhitungan
    for i in range(1, node-1):  # Melooping setiap titik grid kecuali batas
        u[i] = (dt * a * (w[i-1] - 2*w[i] + w[i+1]) / dx**2) + w[i]  # Perhitungan suhu baru berdasarkan persamaan difusi panas

    # Memperbarui plot
    counter += dt  # Menambah waktu simulasi
    print("t: {:.3f} s, Suhu rata-rata: {:.2f} Celcius".format(counter, np.mean(u)))  # Menampilkan waktu dan suhu rata-rata
    pcm.set_array([u])
    ax.set_title("Distribusi Suhu pada t: {:.3f} s".format(counter))
    plt.pause(0.01)

# Bandingkan dengan plot pada t=0
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Plot distribusi suhu pada t=0
ax[0].set_xlabel("x (cm)")
pcm_t0 = ax[0].pcolormesh([u_t0], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm_t0, ax=ax[0])
ax[0].set_ylim([-2, 3])
ax[0].set_title("Distribusi Suhu pada t: 0.0 s")

# Plot distribusi suhu pada akhir waktu simulasi
ax[1].set_xlabel("x (cm)")
pcm_tn = ax[1].pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm_tn, ax=ax[1])
ax[1].set_ylim([-2, 3])
ax[1].set_title("Distribusi Suhu pada t: {:.3f} s".format(waktu))

plt.show()
