import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    ["0", 1, 0, 0, 0, 0, 0, r"$1$"],
    ["1/2", "", "", "", "", "", "", ""],
    ["1", 1, 1, "", "", "", r"$s$"],
    ["3/2", "", "", "", "", "", "", ""],
    ["2", 1, 2, 1, "", "", r"$\frac{s^2 + s}{2}$"],
    ["5/2", "", "", "", "", "", ""],
    ["3", 1, 3, 3, 1, "", "", r"$\frac{s^3 + 3s^2 + 2s}{6}$"],
    ["7/2", "", "", "", "", "", "", ""],
    ["4", 1, 4, 6, 4, 1, "", ""],
    ["9/2", "", "", "", "", "", "", ""],
    ["5", 1, 5, 10, 10, 5, 1, ""],
]

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=["r \\ n-term", r"$1$", r"$x$", r"$x^2$", r"$x^3$", r"$x^4$", r"$x^5$", "label"])

# Plot the table
fig, ax = plt.subplots()
ax.axis('off')  # Turn off the axis
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Adjust the font size
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.5, 1.5)

# Highlight the first row and first column
for key, cell in table.get_celld().items():
    if key[0] == 0 or key[1] == 0:
        cell.set_facecolor("lightblue")

# Adjust the last column's width
for i in range(len(df) + 1):
    cell = table.get_celld().get((i, len(df.columns) - 1))
    cell.set_text_props(ha='left')
    cell.set_facecolor('white')
    cell.set_edgecolor('white')  # Set all edges to white initially
    if i > 0:  # Skip the header row
        cell.visible_edges = 'L'  # Only show the left spine
        cell.set_edgecolor('black')
        cell.set_linewidth(1)
        cell.set_width(0.25)  # Increase the width of the last column

# Set the limits of the axis to include the labels
ax.set_xlim(0, 2)  # Adjust the x-axis limit to accommodate the wider column
ax.set_ylim(0, 1)

# Save the plot as an SVG file
plt.savefig('test.svg', format='svg', bbox_inches='tight')

