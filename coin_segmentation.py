import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt

MAX_SIZE = 500

img = cv2.imread('eBay-Daten\\Ebay_2019_09_03_bis_2019_11_30\\ItemPictures\\153735540929_5.jpg',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)


#Scale bigger dimension to max-size
bigger = max(img.shape[0],img.shape[1]) 
multiplier = MAX_SIZE / bigger 
resized_img = cv2.resize(img,(int(multiplier*img.shape[0]),int(multiplier*img.shape[1])))

hsv_img = cv2.cvtColor(resized_img,cv2.COLOR_BGR2HSV)
hue = hsv_img[:,:,0]
saturation = hsv_img[:,:,1]
value = hsv_img[:,:,2]

median_blur_hue = cv2.medianBlur(hue,11)
median_blur_value = cv2.medianBlur(value,11)

mask_hue = cv2.adaptiveThreshold(median_blur_hue,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
mask_value = cv2.adaptiveThreshold(median_blur_value,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(8, 6))
ax1.imshow(mask_hue, cmap=plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax1.set_title('Hue Mask')
ax2.imshow(mask_value, cmap=plt.cm.gray, interpolation='nearest')
ax2.axis('off')
ax2.set_title('Value Mask')
plt.show()

bgModel = np.zeros((1,65),np.float64)
fgModel = np.zeros((1,65),np.float64)

mask = np.zeros(resized_img.shape[:2],np.uint8)
mask[mask_value == 255] = 2
mask[mask_value == 0] = 3

mask2, bgdModel, fgdModel = cv2.grabCut(resized_img,mask,None,bgModel,fgModel,8,cv2.GC_INIT_WITH_MASK)
mask2 = np.where((mask2 == 2) | (mask2 == 0),0,1).astype('uint8')
resized_img = resized_img*mask2[:,:,np.newaxis]

#convert black to white
resized_img[resized_img == 0] = 255

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(cv2.cvtColor(resized_img,cv2.COLOR_BGR2RGB), interpolation='nearest')
ax.axis('off')
ax.set_title('Segmented image')
plt.show()