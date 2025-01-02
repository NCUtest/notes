import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Generate x values
x = np.linspace(0, 1, 400)

# Calculate corresponding y values
y = np.sqrt(1 - x**2)

# Create the plot
plt.fill_between(x, 0, y, color='blue', alpha=0.5)

# Set aspect ratio to 'equal' to ensure the circle appears as a circle
plt.gca().set_aspect('equal')

# Remove grid and axis
plt.axis('off')

# Set axis limits to start at (0,0)
plt.xlim(-0.1, 1.2)
plt.ylim(-0.1, 1.2)

# Remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Set axis ticks to empty
plt.xticks([])
plt.yticks([])

# Set axis arrow
ax = plt.gca()
ax.add_patch(patches.FancyArrowPatch((0, 0), (1.2, 0), arrowstyle='->', mutation_scale=20, lw=1))
ax.add_patch(patches.FancyArrowPatch((0, 0), (0, 1.2), arrowstyle='->', mutation_scale=20, lw=1))

# Draw a square line
plt.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color='black', lw=1)

# Save the plot as an SVG file
plt.savefig('calculusNotes_figure_8.svg', format='svg')

