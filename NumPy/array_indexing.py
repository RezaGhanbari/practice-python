import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print a
# b = a[:2, 1:3]
# print b

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
# print a[0, 1]   # Prints "2"
# b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
# print a[0, 1]


row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print row_r1, row_r1.shape  # Prints "[5 6 7 8] (4,)"
print row_r2, row_r2.shape  # Prints "[[5 6 7 8]] (1, 4)"
print '\n\n\n'
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print col_r1, col_r1.shape  # Prints "[ 2  6 10] (3,)"
print col_r2, col_r2.shape