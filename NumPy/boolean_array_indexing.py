import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = (a > 3)
print bool_idx

print a[bool_idx]
