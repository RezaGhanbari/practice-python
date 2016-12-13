import numpy as np

v = np.array([1, 2, 3])
w = np.array([4, 5])

print np.reshape(v, (3, 1)) * w
print '\n'

x = np.array([[1, 2, 3], [4, 5, 6]])
print x
print v
print x+v

print '\n'
print (x.T+w).T
print '\n\n'

print x + np.reshape(w, (2, 1))