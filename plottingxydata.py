"""
Examples using the pitch plotting fuction and xy data in football
"""

from plottingpitches import plot_pitch
import random
import matplotlib.pyplot as plt

# Plot some random xy data on a horizontal pitch

plot_pitch(pitchcolour="#195905", linecolour="#faf0e6",
          orientation="horizontal", view="full")

sample = 20
zo = 12

x = [random.randint(0, 104) for p in range(0, sample)]
y = [random.randint(0, 68) for p in range(0, sample)]

plt.scatter(x, y, marker='o', color='red', edgecolors='black', zorder=zo)
plt.show()

# Plot the same data on a vertical pitch (need to reverse y-axis)

plot_pitch(pitchcolour="#195905", linecolour="#faf0e6",
          orientation="vertical", view="full")

y1 = [68 - i for i in y]
plt.scatter(y1, x, marker='o', color='red', edgecolors='k', zorder=zo)
plt.show()

# Plot some imaginary shots made from random data and scale with an imaginary expected goals value. Legend included.

plot_pitch(pitchcolour="#195905", linecolour="#faf0e6",
          orientation="vertical", view="half")

x = [random.randint(72, 104) for p in range(0, sample)]
y = [random.randint(10, 58) for p in range(0, sample)]
y1 = [68 - i for i in y]
z = [random.uniform(0, 1) for p in range(0, sample)]
z1 = [500 * i for i in z]
plt.scatter(y1, x, s=z1, marker='o', color='red', edgecolors='k', zorder=zo)
mSize = [0.05, 0.10, 0.2, 0.4, 0.6, 1]
mSizeS = [500 * i for i in mSize]
mx = [5.5, 7, 9, 11, 13.5, 16.5]
my = [60, 60, 60, 60, 60, 60]
plt.scatter(mx, my, s=mSizeS, facecolors='white',
            edgecolors='white', zorder=zo)
plt.plot([5.5, 17], [57, 57], color='white', lw=2, zorder=zo)
i = 0
for i in range(len(mx)):
    plt.text(mx[i], my[i], mSize[i], fontsize=mSize[i]*18,
             color='#195905', zorder=zo, ha='center', va='center')
plt.text(11, 55, 'xG', color='white', ha='center',
         va='center', zorder=zo, fontsize=16)
plt.show()

# Real match example
