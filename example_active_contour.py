import skimage.io
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import active_contour

import load_images
prefix = '../Curated Images/'
images = load_images.images

img = skimage.io.imread(''.join([prefix,images[0]['filename']]))

# initial snake
centr=np.array([250,250])
rad=100
si=np.array([centr[0]+rad*np.sin(np.linspace(0,2*np.pi,50)), centr[1]+rad*np.cos(np.linspace(0,2*np.pi,50))])
si=np.transpose(si)

s=active_contour(img,si,alpha=0.01,beta=0.01,w_line=1)
plt.imshow(img,cmap='gray')
plt.plot(si[:,0],si[:,1])
plt.plot(s[:,0],s[:,1])

plt.show()