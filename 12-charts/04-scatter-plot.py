import matplotlib.pyplot as plt
import numpy as np

points = 50
x = np.random.rand(points)
y = 2 * x + 1 + 0.3 * np.random.rand(points)
c = np.random.rand(points)

plt.scatter(x, y, c=c, cmap="viridis", edgecolors="black", alpha=1)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.xlabel("Y-axis")
plt.show()
