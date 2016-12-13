import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imresize

img = imread('assets/cat.jpg')
img_tinned = img * [1, 0.95, 0.9]

plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinned))
plt.show()
