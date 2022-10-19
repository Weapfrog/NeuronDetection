# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 01:29:37 2022

@author: muzga
"""

from PIL import Image
import json
import cv2
import os
from natsort import os_sorted
import time

def img_files():
    img_folder = os.listdir("C:/OpenCV-Python/original_images/01. Originals")

    images= []
    
    for img in img_folder:
        if img.endswith(".tif"):
            images.append(img)           
    images = os_sorted(images)
    
    return images

def json_files():
    json_folder = os.listdir("C:/OpenCV-Python/original_images/02. Jsons")
    jsons = []
      
    for jsonfile in json_folder:
        if jsonfile.endswith(".json"):
            jsons.append(jsonfile)         
    jsons = os_sorted(jsons)
    
    return jsons

x_max = 0
x_min = 255555
y_max = 0
y_min = 255555
color = (0,0,255)
iterator=1
iterator2 = 0

#LOOP AROUND EVERY PHOTOGRAPH

for berke in range(292):
    
    img = cv2.imread("C:/OpenCV-Python/original_images/01. Originals/"+img_files()[berke])
    with open("C:/OpenCV-Python/original_images/02. Jsons/"+json_files()[berke],encoding = "utf-8-sig") as f:
        data = json.load(f)

    print("Neuron count:",len(data)-1)
    print("Img name:",data[1][0])
    os.mkdir("C:/OpenCV-Python/original_images/original_neuron_samples(all)/"+img_files()[berke])
    # LOOP AROUND EVERY NEURON IN EACH PHOTOGRAPH
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
        img = cv2.rectangle(img,(int(x_min),int(y_min)),(int(x_max),int(y_max)),color,2)
        
        #TO SAVE THE NEURON SAMPLES ONE BY ONE IN EACH PHOTOGRAPH
        neuron_crop = Image.open("C:/OpenCV-Python/original_images/01. Originals/"+img_files()[berke])
        crop_rectangle = (x_min,y_min,x_max,y_max)
        cropped_img = neuron_crop.crop(crop_rectangle)
        #cropped_img.show()
        cropped_img = cropped_img.save("C:/OpenCV-Python/original_images/original_neuron_samples(all)/"+img_files()[berke]+"/file_"+img_files()[berke]+"_neuron"+str(iterator)+".tif")
        
        x_max = 0
        x_min = 255555
        y_max = 0
        y_min = 255555
        iterator+=1
    #TO SAVE THE IMAGES WITH THE BORDERS AROUND NEURONS
    
    """labelimg = Image.fromarray(img)
    #labelimg.show()
    labelimg = labelimg.save("C:/OpenCV-Python/original_images/labeled_images/"+img_files()[berke]+"_labeled.tif")
    """
    iterator = 1
cv2.waitKey(0)
cv2.destroyAllWindows()
