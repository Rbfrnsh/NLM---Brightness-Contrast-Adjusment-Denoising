# -*- coding: utf-8 -*-
"""
Created on Fri May 22 23:13:20 2020

@author: Adithia Jo
"""

## brightness and contrast
#import liblary
import cv2
import glob
import numpy as np
import os 
from layeris.layer_image import LayerImage

## path yang digunakan 
root_path_testing = 'data/*.jpg' ## di path mana gambar akan di blend
root_path_saving = 'Brightness Frame/'  ## dimana gambar akan disave
file_path = glob.glob(root_path_testing)

#make new directory
os.makedirs(root_path_saving, exist_ok = True)

for path in file_path:
    image = LayerImage.from_file(path)
    image.grayscale()
    image.brightness(0.1)
    #image.lightness(-0.1)
    #image.saturation(2)
    #image.hue(2)
    image.contrast(4)
    # split filename
    filename = path.split('\\')[-1]
    image.save(root_path_saving + filename,100)
    
    
#