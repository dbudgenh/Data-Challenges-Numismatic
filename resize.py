# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:55:40 2021

@author: leonidas devetzidis & david budgenhagen
"""

import cv2 
import os

image_path = os.path.join(os.getcwd(), 'eBay-Daten','images')

width = 300
height = 300

# dsize
dsize = (width, height)
    
os.makedirs(os.path.join("eBay-Daten",str(dsize)))

for root, dirs, files in os.walk(image_path):
    for file in files:
        if not file.endswith('.jpg'):
            print('skipped',file)
            continue
        print('now reading', file)

        src = cv2.imread(os.path.join(root,file), cv2.IMREAD_UNCHANGED)
        
        #percent by which the image is resized
        #scale_percent = 50
        
        #calculate the 50 percent of original dimensions
        #width = int(src.shape[1] * scale_percent / 100)
        #height = int(src.shape[0] * scale_percent / 100)
        
        # resize image
        output = cv2.resize(src, dsize)
        
        
        cv2.imwrite(os.path.join("eBay-Daten",str(dsize),file),output)