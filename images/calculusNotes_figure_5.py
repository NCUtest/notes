import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

for i in range(1, 6):
    vertices = np.array([
        [0, 0, i-1],
        [i, 0, i-1],
        [i, i, i-1],
        [0, i, i-1],
        [0, 0, i],
        [i, 0, i],
        [i, i, i],
        [0, i, i]
    ])

    edges = np.array([
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0],
        [4, 5],
        [5, 6],
        [6, 7],
        [7, 4],
        [0, 4],
        [1, 5],
        [2, 6],
        [3, 7]
    ])

    for edge in edges:
        ax.plot(vertices[edge, 0], vertices[edge, 1], vertices[edge, 2], color='black')

ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)
ax.set_zlim(0, 6)

# set the unit length of x and y be the same
ax.set_aspect("equal")

# invert the z-axis
ax.invert_zaxis()

# turn off axis
ax.axis('off')


plt.savefig('/mnt/c/Users/user/Desktop/wujiaqi_personal_files/notes/images/calculusNotes_figure_5.svg', format='svg', bbox_inches='tight', pad_inches=0)
