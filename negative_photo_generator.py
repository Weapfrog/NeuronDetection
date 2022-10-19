# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:02:19 2022

@author: muzga
"""
from PIL import Image
import random
import cv2
import os
from natsort import os_sorted

def img_files():
    img_folder = os.listdir("C:/OpenCV-Python/original_images/Labeled_images")

    images= []
    
    for img in img_folder:
        if img.endswith(".tif"):
            images.append(img)           
    images = os_sorted(images)
    
    return images


def click_event(event,x,y,flag,params):
    number = random.randint(1,255000)
    # checking for left mouse clicks 
    if event==cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates on the Shell
        neuron_crop = Image.fromarray(img)
        crop_rectangle = (x-15,y-15,x+15,y+15)
        cropped_img = neuron_crop.crop(crop_rectangle)
        #cropped_img.show()
        cropped_img = cropped_img.save("C:/OpenCV-Python/original_images/negative_samples/example_"+str(number)+".tif")
        print("(",x,",",y,"),")    
        # displaying the coordinates on the image window 
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img,(x-15,y-15),(x+15,y+15),(0,0,255),1)
        cv2.imshow("image", img)
    # checking for right mouse clicks
    if event==cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates on the Shell
        print(x,",",y)
        # displaying the coordinates on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        b = img[y, x, 0] 
        g = img[y, x, 1] 
        r = img[y, x, 2] 
        cv2.putText(img, str(b) + "," +
                    str(g) + "," + str(r), 
                    (x,y), font, 1, 
                    (255, 255, 0), 2) 
        cv2.imshow("image", img)
if __name__=="__main__": 
  
    # reading the image 
    
    for berke in range(292): 
        img = cv2.imread("C:/OpenCV-Python/original_images/Labeled_images/"+img_files()[berke])
        cv2.imshow("image", img)
        print(img_files()[berke])
    # setting mouse hadler for the image  and calling the click_event() function 
        cv2.setMouseCallback("image", click_event) 
        cv2.waitKey(0)
    # displaying the image 
    """cv2.imshow("image", img) 
  
    # setting mouse hadler for the image  and calling the click_event() function 
    cv2.setMouseCallback("image", click_event) 
    # wait for a key to be pressed to exit """
    cv2.waitKey(0) 
  
    # close the window 
    cv2.destroyAllWindows() 