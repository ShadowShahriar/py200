import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

mean = x.mean(axis=0)
print(mean)
print("")

std = x.std(axis=0)
print(std)
print("")

x_std = (x - mean) / std
print(x_std)
