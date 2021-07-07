import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import sobel
from scipy import ndimage as ndi
from skimage.segmentation import watershed

img = cv2.imread('eBay-Daten\\Ebay_2019_09_03_bis_2019_11_30\\ItemPictures\\153619873202_6.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.medianBlur(img,7)
hist = np.histogram(img, bins=np.arange(0, 256))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
ax1.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.plot(hist[1][:-1], hist[0], lw=2)
ax2.set_title('histogram of grey values')

#dst = cv2.equalizeHist(img)

elevation_map = sobel(img)

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(elevation_map, cmap=plt.cm.gray, interpolation='nearest')
ax.axis('off')
ax.set_title('elevation_map')
plt.show()

markers = np.zeros_like(img)
markers[img < 50] = 1
markers[img > 150] = 2

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(markers, cmap=plt.cm.Spectral,interpolation='nearest')
ax.axis('off')
ax.set_title('markers')
plt.show()

segmentation = watershed(elevation_map, markers)
#segmentation = ndi.binary_fill_holes(segmentation)

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(segmentation, cmap=plt.cm.gray,interpolation='nearest')
ax.axis('off')
ax.set_title('segmentation')
plt.show()

mask = np.where((segmentation == 2) | (segmentation == 0),0,1).astype('uint8')
segmented_coins = img*mask[:,:]
segmented_coins[segmented_coins == 0] = 255

#segmented_coins = np.multiply(img,segmentation)
fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(segmented_coins,cmap=plt.cm.gray, interpolation='nearest')
ax.axis('off')
ax.set_title('Segmentated coins')
plt.show()