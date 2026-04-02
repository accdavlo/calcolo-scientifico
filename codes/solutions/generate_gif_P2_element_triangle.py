import numpy as np

# Reference triangle vertices:
# x0 = (0, 0), x1 = (1, 0), x2 = (0, 1) , other points in P2
# x3 = (0.5, 0), x4 = (0.5, 0.5), x5 = (0, 0.5)


# P2 (quadratic Lagrange) basis functions on the reference triangle
# using barycentric coordinates:
# l0 = 1 - x - y, l1 = x, l2 = y

def _tri_mask(x, y):
    return (x >= 0) * (y >= 0) * (1 - x - y >= 0)

def phi0_p2(x, y):
    l0 = 1.0 - x - y
    return l0 * (2.0 * l0 - 1.0) * _tri_mask(x, y)

def phi1_p2(x, y):
    l1 = x
    return l1 * (2.0 * l1 - 1.0) * _tri_mask(x, y)

def phi2_p2(x, y):
    l2 = y
    return l2 * (2.0 * l2 - 1.0) * _tri_mask(x, y)

def phi3_p2(x, y):
    l0 = 1.0 - x - y
    l1 = x
    return 4.0 * l0 * l1 * _tri_mask(x, y)

def phi4_p2(x, y):
    l1 = x
    l2 = y
    return 4.0 * l1 * l2 * _tri_mask(x, y)

def phi5_p2(x, y):
    l0 = 1.0 - x - y
    l2 = y
    return 4.0 * l2 * l0 * _tri_mask(x, y)

def p2_basis(x, y):
    """Return all P2 basis functions [phi0_p2, ..., phi5_p2] at (x, y)."""
    return np.array([
        phi0_p2(x, y), phi1_p2(x, y), phi2_p2(x, y),
        phi3_p2(x, y), phi4_p2(x, y), phi5_p2(x, y)
    ])



# Plot with surf one basis function
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import imageio

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)

fig,axs = plt.subplots(2, 3, figsize=(18, 12))

for i in range(6):
    ix = i // 3
    iy = i % 3
    if i == 0:
        Z = phi0_p2(X, Y)
    elif i == 1:
        Z = phi1_p2(X, Y)
    elif i == 2:
        Z = phi2_p2(X, Y)
    elif i == 3:
        Z = phi3_p2(X, Y)
    elif i == 4:
        Z = phi4_p2(X, Y)
    elif i == 5:
        Z = phi5_p2(X, Y)

    axs[ix,iy] = fig.add_subplot(2, 3, i+1, projection='3d')
    ax=axs[ix,iy]
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel(f'phi{i}')
    ax.set_title(f'P2 basis function phi{i} on the reference triangle')



# Rotate the visualization and save the gif of the animated rotation
filenames = []
for angle in range(0, 360, 5):
    for i in range(6):
        ix = i // 3
        iy = i % 3
        axs[ix,iy].view_init(30, angle)
    filename = f'frame_{angle}.png'
    plt.savefig(filename)
    filenames.append(filename)

# Create the GIF with time between frames = 200 ms
with imageio.get_writer(f'p2_basis_functions.gif', mode='I', duration=0.2) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Clean up the temporary files
import os
for filename in filenames:
    os.remove(filename)