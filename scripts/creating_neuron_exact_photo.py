# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:49:13 2022

@author: muzga
"""

from PIL import Image
import json
import cv2
import os
from natsort import os_sorted
import time

x_max = 0
x_min = 255555
y_max = 0
y_min = 255555
color = (0,0,255)
iterator=1
iterator2 = 0
img = cv2.imread("C:/OpenCV-Python/original_images/01. Originals/1_19_41.tif")
with open("C:/OpenCV-Python/original_images/02. Jsons/1_19_41.tif_annotation.json",encoding = "utf-8-sig") as f:
    data = json.load(f)

print("Neuron count:",len(data)-1)
print("Img name:",data[1][0])
while iterator<len(data):
    
    for x in data[iterator][21]:
        if(data[iterator][21][iterator2][0] > x_max ):
            x_max = data[iterator][21][iterator2][0]
        if(data[iterator][21][iterator2][0] < x_min ):
            x_min = data[iterator][21][iterator2][0]
        if(data[iterator][21][iterator2][1] > y_max ):
            y_max = data[iterator][21][iterator2][1]
        if(data[iterator][21][iterator2][1] < y_min ):
            y_min = data[iterator][21][iterator2][1]
        iterator2 += 1
    else:
        iterator2 = 0
    

    x_max = x_max + 5
    x_min = x_min - 5
    y_max = y_max + 5
    y_min = y_min - 5
    
    if x_min < 0:
        x_min = 0
    if y_min < 0:
        y_min = 0
    
    print(x_min,x_max,y_min,y_max)
    #img = cv2.rectangle(img,(int(x_min),int(y_min)),(int(x_max),int(y_max)),color,1)
    cv2.rectangle(img,(x_min,y_min),(x_max,y_max),(255,0,0),2)
    """neuron_crop = Image.open("C:/OpenCV-Python/original_images/01. Originals/"+img_files()[berke])
    crop_rectangle = (x_min,y_min,x_max,y_max)
    cropped_img = neuron_crop.crop(crop_rectangle)
    #cropped_img.show()
    cropped_img = cropped_img.save("C:/OpenCV-Python/original_images/original_neuron_samples(all)/"+"file_"+img_files()[berke]+"_neuron"+str(iterator)+".tif")
    """
    x_max = 0
    x_min = 255555
    y_max = 0
    y_min = 255555
    iterator+=1
    
cv2.imshow(data[1][0],img)
imagesave = Image.fromarray(img)
imagesave = imagesave.save("C:/OpenCV-Python/original_images/labeled_images/ornek.tif")
cv2.waitKey(0)
cv2.destroyAllWindows()
