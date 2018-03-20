import skimage.io
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import filters

import load_images

prefix = '../Curated Images/'

images = load_images.images

ix=1
movie = skimage.io.imread(''.join([prefix,images[ix]['filename']]))
#print images[ix]['rounded']

A=movie[0,1,:,:]

# B=A-ndimage.gaussian_filter(A,sigma=15)

# B=ndimage.grey_dilation(A,15)-ndimage.gaussian_filter(A,15)

# B=filters.scharr(A)

# thr = filters.threshold_otsu(ndimage.gaussian_filter(A,55))
# B=A-thr

# B=ndimage.morphological_gradient(A,15)

plt.imshow(A,cmap='gray')
# plt.imshow(B,cmap='gray')

plt.show()