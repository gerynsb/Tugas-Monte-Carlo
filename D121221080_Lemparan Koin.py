import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def lempar_koin():
    return random.choice(['kepala', 'ekor'])

def simulasi_lemparan_koin(n_lemparan):
    jumlah_kepala = 0
    hasil_probabilitas = []

    for i in range(1, n_lemparan + 1):
        hasil = lempar_koin()
        if hasil == 'kepala':
            jumlah_kepala += 1
        
        # Menyimpan hasil probabilitas setiap iterasi
        if i % 100 == 0: 
            probabilitas_kepala = jumlah_kepala / i
            hasil_probabilitas.append((i, probabilitas_kepala))

    return hasil_probabilitas

# Jumlah lemparan koin dalam simulasi
n_lemparan = 10000

# Melakukan simulasi
hasil_probabilitas = simulasi_lemparan_koin(n_lemparan)

# Memisahkan data untuk grafik
jumlah_lemparan, probabilitas = zip(*hasil_probabilitas)

# Membuat grafik
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot([], [], label='Probabilitas Kepala', color='green')
ax.axhline(y=0.5, color='orange', linestyle='--', label='Probabilitas Teoritis (0.5)')
ax.set_xlabel('Jumlah Lemparan')
ax.set_ylabel('Probabilitas Kepala')
ax.set_title('Simulasi Monte Carlo: Probabilitas Lemparan koin')
ax.legend(loc='lower right')
ax.grid(True)

def init():
    ax.set_xlim(0, n_lemparan)
    ax.set_ylim(0, 1)
    return line,

def update(frame):
    line.set_data(jumlah_lemparan[:frame], probabilitas[:frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(jumlah_lemparan), init_func=init, blit=True, interval=50, repeat=False)

plt.show()
