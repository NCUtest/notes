import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    ["0", 1, 1, 1, 1, 1, 1, 1, 1, 1, r"$1$"],
    ["1/2", 1, "", r"$\frac{3}{2}$", "", r"$\frac{3 \cdot 5}{2 \cdot 4}$", "", r"$\frac{3 \cdot 5 \cdot 7}{2 \cdot 4 \cdot 6}$", "", r"$\frac{3 \cdot 5 \cdot 7 \cdot 9}{2 \cdot 4 \cdot 6 \cdot 8}$", ""],
    ["1", 1, r"$\frac{3}{2}$", 2, r"$\frac{5}{2}$", 3, r"$\frac{7}{2}$", 4, r"$\frac{9}{2}$", 5, r"$s$"],
    ["3/2", 1, "", r"$\frac{5}{2}$", "", r"$\frac{5 \cdot 7}{2 \cdot 4}$", "", r"$\frac{5 \cdot 7 \cdot 9}{2 \cdot 4 \cdot 6}$", "", r"$\frac{5 \cdot 7 \cdot 9 \cdot 11}{2 \cdot 4 \cdot 6 \cdot 8}$", ""],
    ["2", 1, r"$\frac{15}{8}$", 3, r"$\frac{35}{8}$", 6, r"$\frac{63}{8}$", 10, r"$\frac{99}{8}$", 15, r"$\frac{s^2 + s}{2}$"],
    ["5/2", 1, "", r"$\frac{7}{2}$", "", r"$\frac{7 \cdot 9}{2 \cdot 4}$", "", r"$\frac{7 \cdot 9 \cdot 11}{2 \cdot 4 \cdot 6}$", "", r"$\frac{7 \cdot 9 \cdot 11 \cdot 13}{2 \cdot 4 \cdot 6 \cdot 8}$", ""],
    ["3", 1, r"$\frac{105}{48}$", 4, r"$\frac{315}{48}$", 10, r"$\frac{693}{48}$", 20, r"$\frac{1287}{48}$", 35, r"$\frac{s^3 + 3s^2 + 2s}{6}$"],
    ["7/2", 1, "", r"$\frac{9}{2}$", "", r"$\frac{9 \cdot 11}{2 \cdot 4}$", "", r"$\frac{9 \cdot 11 \cdot 13}{2 \cdot 4 \cdot 6}$", "", r"$\frac{9 \cdot 11 \cdot 13 \cdot 15}{2 \cdot 4 \cdot 6 \cdot 8}$", ""],
    ["4", 1, r"$\frac{945}{384}$", 5, r"$\frac{3465}{384}$", 15, r"$\frac{9009}{384}$", 35, r"$\frac{19305}{384}$", 70, r"$\frac{s^4 + 6s^3 + 11s^2 + 6s}{24}$"]
]

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=["q \\ p", "0", "1/2", "1", "3/2", "2", "5/2", "3", "7/2", "4", ""])

# Plot the table
fig, ax = plt.subplots()
ax.axis('off')  # Turn off the axis
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Adjust the font size
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(2.0, 2.5)

# Highlight the first row and first column
for key, cell in table.get_celld().items():
    if key[0] == 0 or key[1] == 0:
        cell.set_facecolor("lightblue")

# Adjust the last column's width
for i in range(len(df)+1):
    cell = table.get_celld().get((i, len(df.columns)-1))
    cell.set_text_props(ha='left')
    cell.set_facecolor('white')
    cell.set_edgecolor('white')  # Set all edges to white initially
    cell.visible_edges = 'L'  # Only show the left spine
    cell.set_edgecolor('black')
    cell.set_linewidth(1)
    cell.set_width(0.25)  # Increase the width of the last column

# Set the limits of the axis to include the labels
ax.set_xlim(0, 1.5)  # Adjust the x-axis limit to accommodate the wider column
ax.set_ylim(0, 1)

# Save the plot as an SVG file
plt.savefig('calculusNotes_figure_11.svg', format='svg', bbox_inches='tight')


