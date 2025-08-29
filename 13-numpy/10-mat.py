import numpy as np

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat[1])  # ======= 2nd row [4 5 6]
print(mat[0, 2])  # ==== (row, column) 3
print(mat[-1, -1])  # == last row, last column
