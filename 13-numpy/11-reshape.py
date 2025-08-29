import numpy as np

arr = np.arange(1, 10).reshape(3, 3)
print(arr)
print(arr[::2, 1::2])
print(arr[::2, 1::2].sum())
