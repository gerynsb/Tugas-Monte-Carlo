import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Total jumlah titik
n_points = 1000

# Titik di dalam lingkaran
inside_circle = 0

# Daftar untuk menyimpan titik
x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Membuat plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Menambahkan lingkaran pada plot
circle = plt.Circle((0, 0), 1, color='blue', fill=False)
ax.add_patch(circle)

# Menambahkan titik dalam dan luar lingkaran
inside_points, = ax.plot([], [], 'go', label='Titik di dalam lingkaran')  # Titik hijau untuk di dalam lingkaran
outside_points, = ax.plot([], [], 'ro', label='Titik di luar lingkaran')  # Titik merah untuk di luar lingkaran

# Menambahkan legend dan judul pada plot
ax.legend(bbox_to_anchor=(0.5, -0.05), loc='upper center', ncol=2)
ax.set_title('Monte Carlo Simulation: Estimasi Area')

# Fungsi untuk memperbarui plot
def update(i):
    global inside_circle
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    
    if x**2 + y**2 <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)
    
    inside_points.set_data(x_inside, y_inside)
    outside_points.set_data(x_outside, y_outside)
    
    if i > 0:
        # Memperbarui judul dengan hasil estimasi π
        estimation = 4 * inside_circle / (i + 1)
        ax.set_title(f'Monte Carlo Simulation: Estimasi Area ≈ {estimation:.4f}')
    
    return inside_points, outside_points

# Membuat animasi
ani = animation.FuncAnimation(fig, update, frames=n_points, interval=10, blit=True, repeat=False)
plt.show()
