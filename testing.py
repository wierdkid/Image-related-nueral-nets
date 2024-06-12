import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define the function to be plotted
def f(x):
    return np.sin(x)

# Define the range for x
x = np.linspace(0, 2 * np.pi, 1000)
y = f(x)

# Define the rectangle dimensions
rect_x = [0, 2 * np.pi]
rect_y = [0, 1]

# Calculate the areas
area_below = np.trapz(np.minimum(y, 1), x)
area_above = np.trapz(np.maximum(y - 1, 0), x)

# Create the plot
fig, ax = plt.subplots()

# Plot the function
ax.plot(x, y, label='f(x) = sin(x)')

# Plot the rectangle
rect = Rectangle((rect_x[0], rect_y[0]), rect_x[1] - rect_x[0], rect_y[1] - rect_y[0],
                 edgecolor='r', facecolor='none', linestyle='--', label='Rectangle')
ax.add_patch(rect)

# Fill the areas below and above the function
ax.fill_between(x, 0, np.minimum(y, 1), color='blue', alpha=0.3, label='Area below')
ax.fill_between(x, 1, y, where=(y > 1), color='orange', alpha=0.3, label='Area above')

# Add text for the areas
ax.text(1, 0.5, f'Area below: {area_below:.2f}', fontsize=12, color='blue')
ax.text(1, 1.5, f'Area above: {area_above:.2f}', fontsize=12, color='orange')

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Function and Rectangle with Areas')

# Add legend
ax.legend()

# Show the plot
plt.show()
