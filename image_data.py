import skimage.io
import gc
import random

prefix = '../Curated Images/'

images = [
            { 'filename':'recording1.czi - recording1.czi #03.tif', 'rounded':69, 'egress':76, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #07.tif', 'rounded':95, 'egress':102, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #09.tif', 'rounded':109, 'egress':114, 'notes':'egress fail' },
            { 'filename':'recording1.czi - recording1.czi #12.tif', 'rounded':23, 'egress':28, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #13.tif', 'rounded':90, 'egress':100, 'notes':'egress fail' },
            { 'filename':'recording1.czi - recording1.czi #14.tif', 'rounded':8, 'egress':12, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #17.tif', 'rounded':73, 'egress':81, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #18.tif', 'rounded':9, 'egress':13, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #03.tif', 'rounded':61, 'egress':69, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #04.tif', 'rounded':38, 'egress':42, 'notes':'egress fail' },
            { 'filename':'recording2.czi - recording2.czi #05.tif', 'rounded':28, 'egress':40, 'notes':''},
            { 'filename':'recording2.czi - recording2.czi #06.tif', 'rounded':104, 'egress':110, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #09.tif', 'rounded':63, 'egress':69, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #11.tif', 'rounded':26, 'egress':31, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #14.tif', 'rounded':26, 'egress':33, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #15.tif', 'rounded':75, 'egress':82, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #17.tif', 'rounded':73, 'egress':78, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #18.tif', 'rounded':0, 'egress':6, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #20.tif', 'rounded':90, 'egress':96, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #10.tif', 'rounded':455, 'egress':463, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #12.tif', 'rounded':194, 'egress':198, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #13.tif', 'rounded':134, 'egress':139, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #16.tif', 'rounded':250, 'egress':254, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #19.tif', 'rounded':145, 'egress':151, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #20.tif', 'rounded':254, 'egress':259, 'notes':'' }
        ]

def all_images():
    for image in images:
        img = skimage.io.imread(''.join([prefix,image['filename']]))
        yield img, image['rounded'], image['egress']
        gc.collect()

def all_timepoints(img):
    for frame in range(img.shape[0]):
        timepoint = img[frame,:,:,:].squeeze()
        yield timepoint

def fetch_random_image():
    imgnum = random.randint(0,len(images))
    img = skimage.io.imread(''.join([prefix,images[imgnum]['filename']]))
    framenum = random.randint(0,img.shape[0])
    return img[framenum,:,:,:].squeeze()

# for image in images:
#     img = skimage.io.imread(''.join([prefix,image['filename']]))
#
#     print image['rounded']
#
#     plt.plot([np.sum(img[i,0,:,:]) for i in range(img.shape[0])])
#     plt.show()
