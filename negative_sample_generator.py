# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:46:25 2022

@author: muzga
"""

import cv2
import time
from PIL import Image
import numpy
import json
import os
from natsort import os_sorted

def img_files():
    img_folder = os.listdir("C:/OpenCV-Python/original_images/masks_jpg")

    images= []
    
    for img in img_folder:
        if img.endswith(".jpg"):
            images.append(img)           
    images = os_sorted(images)
    
    return images


iterator = 0
while iterator < 293:
    path = "C:/OpenCV-Python/original_images/masks_jpg/"+img_files()[iterator]
    img = Image.open(path)
    os.mkdir("C:/OpenCV-Python/original_images/negative_json_directories/"+img_files()[iterator])
    for x in range(21):#21 because we want 30x30 neg_images and our sample photos are 640x480
    
        for y in range(16):#16 because we want 30x30 neg_images and our sample photos are 640x480
            crop_rectangle = (x*30,y*30,(x*30)+30,(y*30)+30)
            cropped_img = img.crop(crop_rectangle)
            #cropped_img.show()
            if not cropped_img.getbbox():           
                #cropped_img = cropped_img.save("C:/OpenCV-Python/original_images/negative_script_samples/"+"file_neuron"+str(y)+"_"+str(x)+".tif")           
                #print(crop_rectangle)
                x_min = crop_rectangle[0]
                y_min = crop_rectangle[1]
                x_max = crop_rectangle[2]
                y_max = crop_rectangle[3]
                negative_dict = {
                    "x_min":x_min,
                    "y_min":y_min,
                    "x_max":x_max,
                    "y_max":y_max
                    }
                with open("C:/OpenCV-Python/original_images/negative_json_directories/"+img_files()[iterator]+"/"+str(y)+"_"+str(x)+"_negative.json","w") as json_dosya:
                    json.dump(negative_dict,json_dosya,indent=4,sort_keys=False)
    iterator+=1
            #cropped_negative = Image.open("C:/OpenCV-Python/original_images/negative_script_samples/"+"file_neuron"+str(y)+"_"+str(x)+".tif")

            
        
        



cv2.waitKey(0)
cv2.destroyAllWindows()