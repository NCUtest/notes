import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

for i in range(1, 6):
    ax.add_patch(patches.Rectangle((0, 5-i), i, 1, edgecolor='black', facecolor='none'))

ax.set_xlim(-1, 6)
ax.set_ylim(0, 6)

ax.axis('off')

plt.savefig('/mnt/c/Users/user/Desktop/wujiaqi_personal_files/notes/images/calculusNotes_figure_4.svg', format='svg', bbox_inches='tight', pad_inches=0)
