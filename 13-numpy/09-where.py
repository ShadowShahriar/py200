import numpy as np

arr = np.array([5, 10, 15, 20])
print(np.where(arr > 10))
print(np.where(arr > 10, 1, 0))
