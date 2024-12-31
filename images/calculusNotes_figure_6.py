import matplotlib.pyplot as plt
import numpy as np

# Define the function and parameters
k = 2
x = np.linspace(0, 10, 400)
y = x**k

# Create the plot
fig, ax = plt.subplots()

# Plot the function
ax.plot(x, y, label='$y=x^k$')

# Choose a point on the curve (e.g., x=4)
x_point = 9 
y_point = x_point**k

# Draw the rectangle to the x and y axes
ax.vlines(x=x_point, ymin=0, ymax=y_point, colors='red', linestyles='dotted', label='$x=4$')
ax.hlines(y=y_point, xmin=0, xmax=x_point, colors='red', linestyles='dotted')

# Draw the area under the curve up to the chosen point
ax.fill_between(x, y, where=(x <= x_point), color='skyblue', alpha=0.4)

# Labeling the chosen point on the curve
ax.plot(x_point, y_point, 'ro')  # Mark the point
#ax.text(x_point, y_point + 5, f'({x_point}, {y_point})', fontsize=12, va='bottom', ha='center')
#ax.text(7, 7**k + 10, r'$y=x^k$', fontsize=12, va='bottom', ha='center')

# Remove the top and right spines (the box edges)
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Move bottom and left spines to the center
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# Add arrows at the ends of the axes
ax.annotate('', xy=(10, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=1.5))
ax.annotate('', xy=(0, 100), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=1.5))

# Labeling the axes
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12, rotation=0)
ax.xaxis.set_label_coords(1.05, -0.05)
ax.yaxis.set_label_coords(-0.05, 1.05)

# Remove axis units (ticks)
ax.set_xticks([])
ax.set_yticks([])

# Set the x and y limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

# Save the plot as an SVG file
plt.savefig('calculusNotes_figure_6.svg', format='svg')

# plt.show() is not required since we're saving the file

