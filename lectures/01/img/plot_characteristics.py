import numpy as np
import matplotlib.pyplot as plt

# For the transport equation u_t + u_x = 0,
# the characteristic lines are defined by:
# dt/ds = 1
# dx/ds = 1
# which gives: x - t = constant
# So characteristics are lines with slope 1 in the (x,t) plane

fig, ax = plt.subplots(figsize=(5, 4))

# Domain
x_min, x_max = 0, 2
t_min, t_max = 0, 2

# Plot characteristic lines: x - t = c
# Rearranging: x = t + c
constants = np.linspace(-4, 4, 17)

for c in constants:
    t_vals = np.linspace(t_min, t_max, 100)
    x_vals = t_vals + c
    
    # Only plot within domain
    ax.plot(t_vals, x_vals, 'b-', linewidth=1.5, alpha=0.7)

# Add arrows to show direction of propagation
for c in np.linspace(0, 2, 5):
    t_arrow = 1.
    x_arrow = t_arrow + c
    if x_min <= x_arrow <= x_max:
        ax.arrow(t_arrow - 0.1, x_arrow - 0.1, 0.15, 0.15, 
                head_width=0.15, head_length=0.1, fc='blue', ec='blue')

# Labels and formatting
ax.set_ylabel('Time (t)', fontsize=12)
ax.set_xlabel('Space (x)', fontsize=12)
ax.set_title('Characteristic Lines of Transport Equation', fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_xlim(t_min, t_max)
ax.set_ylim(x_min, x_max)
ax.set_aspect('equal')

# Add text annotation
ax.text(0.5, 0.5, r'$x - t = c$', fontsize=12, 
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('/home/accdavlo/Projects/Sapienza/teaching/calcolo-scientifico/transport_characteristics.png', 
            dpi=300, bbox_inches='tight')
plt.show()

print("Plot saved as transport_characteristics.png")
