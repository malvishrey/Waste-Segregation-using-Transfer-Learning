import matplotlib.pyplot as plt

from skimage import data, color,io
from skimage.transform import rescale, resize, downscale_local_mean
import skimage
#image = color.rgb2gray(data.astronaut())

#image_rescaled = rescale(image, 1.0 / 4.0)
#plt.imshow(image_rescaled)
img=skimage.io.imread("dataset-resized\\cardboard\\cardboard11.jpg")

img1 = rescale(img, 5.0)
print(img.shape)
fig, axes = plt.subplots(nrows=1, ncols=2)

ax = axes.ravel()

ax[0].imshow(img)
ax[0].set_title("Original image")

ax[1].imshow(img1)
ax[1].set_title("Rescaled image (aliasing)")

plt.show()
