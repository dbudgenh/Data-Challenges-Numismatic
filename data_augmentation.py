import cv2
from scipy import ndimage
import numpy as np
import imutils 



IMG_PATH = 'workspace\\images\\113744714802_2.jpg'
img = cv2.imread(IMG_PATH)

rotated = imutils.rotate_bound(img, angle=25)
#rotated = ndimage.rotate(img,angle=25)
#rotated = ndimage.rotate(img, 22,reshape=True)
cv2.imwrite('images\\rotated-image.jpg',rotated)

rotated_flip = cv2.flip(rotated,flipCode=1)
cv2.imwrite('images\\rotated-flip-image.jpg',rotated_flip)

random_crop = rotated_flip[50:400,100:500]
cv2.imwrite('images\\rotated-flip-crop-image.jpg',random_crop)