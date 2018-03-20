import skimage.io
import numpy as np
import matplotlib.pyplot as plt

import load_images

prefix = '../Curated Images/'

images = load_images.images

img = skimage.io.imread(''.join([prefix,images[0]['filename']]))
a=img[1,1,:,:]
b=np.abs(a-np.mean(a.flatten()))
plt.imshow(b,cmap='gray')

plt.show()