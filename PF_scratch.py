import skimage.io
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import filters

import load_images

import image_processing as ip

ix=11
movie = skimage.io.imread(''.join([load_images.prefix,load_images.images[ix]['filename']]))
# print images[ix]['rounded']
stop=load_images.images[ix]['egress']

# circ=np.array(movie.shape[0])
circ=[]
for frame in range(movie.shape[0]):
    A=movie[frame,1,:,:]

    B,RP=ip.get_cell_mask(A,(250,250),ptile=25,blur_sigma=15)
    
    if len(RP)!=0:
        circ.append(4*np.pi*RP[0].area/(RP[0].perimeter**2))

    # plt.subplot(1,2,1)
    # plt.imshow(A,cmap='gray')
    # plt.subplot(1,2,2)
    # plt.imshow(B,cmap='gray')
    # plt.draw()
    # plt.pause(0.001)
    # plt.imshow(B,cmap='gray')
    #plt.imshow(L,cmap='gray')


plt.plot(range(movie.shape[0]),circ)
plt.show()