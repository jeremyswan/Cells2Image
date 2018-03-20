import skimage.io
import numpy as np
import matplotlib.pyplot as plt

import load_images

prefix = '../Curated Images/'

images = load_images.images

# for image in images:
#     img = skimage.io.imread(''.join([prefix,image['filename']]))
#     print image['rounded']
#     plt.plot([np.sum(img[i,0,:,:]) for i in range(img.shape[0])])
#
# plt.show()

img = skimage.io.imread(''.join([prefix,images[0]['filename']]))
#plt.hist(img[0,0,:,:].flatten())
a=img[1,1,:,:]
b=np.abs(a-np.mean(a.flatten()))
#plt.imshow(a<np.percentile(b.flatten(),1),cmap='gray')
plt.figure()
plt.imshow(b,cmap='gray')
plt.draw()

import numpy as np
from skimage.segmentation import active_contour
centr=np.array([250,250])
rad=100
si=np.array([centr[0]+rad*np.sin(np.linspace(0,2*np.pi,50)), centr[1]+rad*np.cos(np.linspace(0,2*np.pi,50))])
si=np.transpose(si)
s=active_contour(a,si,alpha=0.01,beta=0.01,w_line=1)
#print(s)
plt.figure()
plt.imshow(a,cmap='gray')
plt.plot(si[:,0],si[:,1])
plt.plot(s[:,0],s[:,1])
plt.draw()

plt.show()