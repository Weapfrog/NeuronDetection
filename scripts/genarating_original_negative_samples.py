# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:46:42 2022

@author: muzga
"""

from PIL import Image
from natsort import os_sorted
import cv2
import json
import os

def img_files():
    img_folder = os.listdir("C:/OpenCV-Python/original_images/01. Originals")

    images= []
    
    for img in img_folder:
        if img.endswith(".tif"):
            images.append(img)           
    images = os_sorted(images)
    
    return images

def dir_files():
    dir_folder = os.listdir("C:/OpenCV-Python/original_images/negative_json_directories")
    dirs = []
      
    for dirfile in dir_folder:
        if dirfile.endswith(""):
            dirs.append(dirfile)         
    dirs = os_sorted(dirs)
    
    return dirs

def json_files(path):
    json_folder = os.listdir("C:/OpenCV-Python/original_images/negative_json_directories/"+path)
    jsons = []
      
    for jsonfile in json_folder:
        if jsonfile.endswith("json"):
            jsons.append(jsonfile)         
    jsons = os_sorted(jsons)
    
    return jsons

print(json_files(dir_files()[0]))

for x in range (292):
    img = Image.open("C:/OpenCV-Python/original_images/01. Originals/"+img_files()[x])
    print(dir_files()[x])
    i=0
    while i < len(json_files(dir_files()[x])):
        with open("C:/OpenCV-Python/original_images/negative_json_directories/"+dir_files()[x]+"/"+json_files(dir_files()[x])[i]) as f:
            data = json.load(f)
            print(i)
            print(data)
            crop_rectangle = (data["x_min"],data["y_min"],data["x_max"],data["y_max"])
            cropped_img = img.crop(crop_rectangle)
            #cropped_img.show()
            cropped_img = cropped_img.save("C:/OpenCV-Python/original_images/negative_original_samples/"+str(x)+".file_"+str(i)+".sample.tif")
            i+=1















