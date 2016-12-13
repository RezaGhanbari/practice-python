import numpy as np
from scipy.spatial.distance import pdist, squareform, cdist

x = np.array([[0, 1], [1, 0], [2, 0]])
y = np.array([[1, 2], [2, 0], [4, 1]])
print x

d = squareform(pdist(x, 'euclidean'))
print d


