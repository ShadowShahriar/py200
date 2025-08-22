import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 15, 25, 30, 35]
y2 = [5, 10, 20, 25, 30]

plt.fill_between(x, y1, y2, color="red", alpha=0.5)
plt.title("Area Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
