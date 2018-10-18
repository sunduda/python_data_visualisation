import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#import time

from random_walk import RandomWalk

rw = RandomWalk(5000)

plt.ion()

fig, ax = plt.subplots()
cmap = mpl.cm.get_cmap("Blues")
sc = ax.scatter(rw.x_values, rw.y_values, c = [1], cmap = cmap, s = 10)
# c = list(range(len(rw.x_values))), cmap = plt.cm.Blues, edgecolor = 'none', s = 10

plt.xlim(-1, 1)
plt.ylim(-1, 1)

plt.draw()

while len(rw.x_values) < rw.num_points:
    if rw.fill_walk():
        sc.set_offsets(np.c_[rw.x_values, rw.y_values])

        # Using Normalize to make a normalised colour list based on the relevant data, 
        # mapping it to a ScalarMappable, and using that to set the face colour and 
        # c limits on each frame of the animation.
        n = mpl.colors.Normalize(vmin = 1, vmax = len(rw.x_values))
        m = mpl.cm.ScalarMappable(norm=n, cmap=cmap)
        sc.set_facecolor(m.to_rgba(list(range(1, len(rw.x_values) + 1))))

        plt.xlim(min(rw.x_values)-5, max(rw.x_values)+5)
        plt.ylim(min(rw.y_values)-5, max(rw.y_values)+5)

    fig.canvas.draw()
    plt.pause(0.1)
