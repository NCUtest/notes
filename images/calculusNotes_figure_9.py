import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    ["0", 1, "", 1, "", 1, "", 1, "", 1],
    ["1/2", "", "", "", "", "", "", "", "", ""],
    ["1", 1, "", 2, "", 3, "", 4, "", 5],
    ["3/2", "", "", "", "", "", "", "", "", ""],
    ["2", 1, "", 3, "", 6, "", 10, "", 15],
    ["5/2", "", "", "", "", "", "", "", "", ""],
    ["3", 1, "", 4, "", 10, "", 20, "", 35],
    ["7/2", "", "", "", "", "", "", "", "", ""],
    ["4", 1, "", 5, "", 15, "", 35, "", 70]
]

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=["q \\ p", "0", "1/2", "1", "3/2", "2", "5/2", "3", "7/2", "4"])

# Plot the table
fig, ax = plt.subplots()
ax.axis('off')  # Turn off the axis
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Adjust the font size
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)

# Highlight the first row and first column
for key, cell in table.get_celld().items():
    if key[0] == 0 or key[1] == 0:
        cell.set_facecolor("lightblue")

# Save the plot as an SVG file
plt.savefig('calculusNotes_figure_9.svg', format='svg')

