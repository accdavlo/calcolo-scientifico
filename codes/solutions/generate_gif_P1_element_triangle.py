import numpy as np

# Reference triangle vertices:
# x0 = (0, 0), x1 = (1, 0), x2 = (0, 1)

def phi0(x, y):
    """P1 basis function associated with x0."""
    return (1.0 - x - y)*(x>=0)*(x>=0)*(1-x-y>=0)

def phi1(x, y):
    """P1 basis function associated with x1."""
    return x *(x>=0)*(x>=0)*(1-x-y>=0)

def phi2(x, y):
    """P1 basis function associated with x2."""
    return y*(x>=0)*(x>=0)*(1-x-y>=0)


def p1_basis(x, y):
    """Return all P1 basis functions [phi0, phi1, phi2] at (x, y)."""
    return np.array([phi0(x, y), phi1(x, y), phi2(x, y)])


# Constant gradients on the reference triangle
grad_phi0 = np.array([-1.0, -1.0])
grad_phi1 = np.array([1.0, 0.0])
grad_phi2 = np.array([0.0, 1.0])



# Plot with surf one basis function
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import imageio

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)

fig,axs = plt.subplots(1,3,figsize=(18, 6))

for i in range(3):
    if i == 0:
        Z = phi0(X, Y)
    elif i == 1:
        Z = phi1(X, Y)
    else:
        Z = phi2(X, Y)
    
    axs[i] = fig.add_subplot(1, 3, i+1, projection='3d')
    ax=axs[i]
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel(f'phi{i}')
    ax.set_title(f'P1 basis function phi{i} on the reference triangle')



# Rotate the visualization and save the gif of the animated rotation
filenames = []
for angle in range(0, 360, 5):
    for i in range(3):
        axs[i].view_init(30, angle)
    filename = f'frame_{angle}.png'
    plt.savefig(filename)
    filenames.append(filename)

# Create the GIF with time between frames = 200 ms
with imageio.get_writer(f'p1_basis_functions.gif', mode='I', duration=0.2) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Clean up the temporary files
import os
for filename in filenames:
    os.remove(filename)