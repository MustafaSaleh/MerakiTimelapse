import cv2
import numpy as np
import glob
import os


camera = input("Please insert Camera Serial Number! ")
fps =  int(input("How many frames per second? "))

img_array = []
i = 0
for filename in sorted(glob.glob('cameras/'+camera+'/*.jpeg')):
    print(filename)
    i +=i
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter('cameras/'+camera+'.mp4',cv2.VideoWriter_fourcc(*'MP4V'), fps, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
