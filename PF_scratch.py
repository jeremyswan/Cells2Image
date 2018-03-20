import skimage.io
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import filters

import load_images

ix=0
movie = skimage.io.imread(''.join([load_images.prefix,load_images.images[ix]['filename']]))
#print images[ix]['rounded']

A=movie[68,1,:,:]

B=np.abs(A-np.percentile(A.flatten(),75))
B=ndimage.gaussian_filter(B,15)
thr = filters.threshold_otsu(B)
B=B>thr

L=skimage.measure.label(B)
RP=skimage.measure.regionprops(L,intensity_image=A,)

print 4*np.pi*RP[0].area/(RP[0].perimeter**2)

# B=A-ndimage.gaussian_filter(A,sigma=15)

# B=ndimage.grey_dilation(A,15)-ndimage.gaussian_filter(A,15)

# B=filters.scharr(A)

# thr = filters.threshold_otsu(ndimage.gaussian_filter(A,55))
# B=A-thr

# B=ndimage.morphological_gradient(A,15)

plt.subplot(1,2,1)
plt.imshow(A,cmap='gray')
plt.subplot(1,2,2)
plt.imshow(A*B,cmap='gray')
# plt.imshow(B,cmap='gray')
#plt.imshow(L,cmap='gray')

plt.show()