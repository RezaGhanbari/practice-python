from scipy.misc import imread, imsave, imresize

img = imread('assets/cat.jpg')
print img.dtype, img.shape

img_tinted = img * [1, 0.95, 0.9]
img_tinted = imresize(img_tinted, (img.shape[0] - 100, 100))

imsave('assets/cat_tinned.jpg', img_tinted)
