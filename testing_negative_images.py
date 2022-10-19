# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:21:07 2022

@author: muzga
"""
import cv2
import json
from PIL import Image
import os
from natsort import os_sorted

def json_files():
    json_folder = os.listdir("C:/OpenCV-Python/original_images/negative_json_directories/suero5_19-04-22_neurons_background.ome0.jpg")
    jsons = []
      
    for jsonfile in json_folder:
        if jsonfile.endswith(".json"):
            jsons.append(jsonfile)         
    jsons = os_sorted(jsons)
    
    return jsons

img_path = "C:/OpenCV-Python/original_images/masks_jpg/suero5_19-04-22_neurons_background.ome0.jpg"
json_path = "C:/OpenCV-Python/original_images/negative_json_directories/suero5_19-04-22_neurons_background.ome0.jpg"

img = Image.open(img_path)
iterator=0

for i in range(198):
    with open('C:/OpenCV-Python/original_images/negative_json_directories/suero5_19-04-22_neurons_background.ome0.jpg/'+json_files()[iterator]) as f:
        veri = json.load(f)
    crop_rectangle = (veri["x_min"],veri["y_min"],veri["x_max"],veri["y_max"])
    cropped_img = img.crop(crop_rectangle)
    #cropped_img.show()
    cropped_img = cropped_img.save("C:/OpenCV-Python/original_images/berke/"+str(iterator)+"negative.tif")
    iterator+=1






cv2.waitKey(0)
cv2.destroyAllWindows()