# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:15:18 2018

@author: wmy
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def creat_kernel_3x3():
    kernel = np.array([[-2,  2, -2], 
                       [ 2,  0,  2], 
                       [-2,  2, -2]])
    return kernel

def open_image(path, size=(256, 256)):
    img = Image.open(path)
    img = img.resize(size)
    img = np.array(img)
    return img 

def conv2d_3x3(img, kernel):
    h, w, c = img.shape
    output = []
    for m in range(1, h-1):
        output.append([])
        for n in range(1, w-1):
            pix = kernel[0][0] * img[m-1][n-1] + \
            kernel[0][1] * img[m-1][n] + \
            kernel[0][2] * img[m-1][n+1] + \
            kernel[1][0] * img[m][n-1] + \
            kernel[1][1] * img[m][n] + \
            kernel[1][2] * img[m][n+1] + \
            kernel[2][0] * img[m+1][n-1] + \
            kernel[2][1] * img[m+1][n] + \
            kernel[2][2] * img[m+1][n+1]
            output[m-1].append(pix)
            pass
        pass
    return output            
  
def check(img, threshold=64, draw=False):
    warning = False
    warning_pixes_index = []
    y1 = int(len(img)*0.7)
    y2 = int(len(img))
    x1 = int(len(img[0])*0.15)
    x2 = int(len(img[0])*0.85)
    copy = np.copy(img)
    for m in range(y1, y2):
        for n in range(x1, x2):
            if img[m][n][0] > threshold or img[m][n][1] > threshold \
            or img[m][n][2] > threshold:
                warning_pixes_index.append((m, n))
                copy[m][n] = [255, 0, 0]
                warning = True
                pass
            pass
        pass
    if warning:
        print('warning!')
        pass
    else:
        print('ok!')
        pass
    if draw:
        for n in range(x1, x2):
            copy[y1-1][n] = [0, 0, 255]
            copy[y2-1][n] = [0, 0, 255]
            pass
        for m in range(y1, y2):
            copy[m][x1-1] = [0, 0, 255]
            copy[m][x2-1] = [0, 0, 255]
            pass
        plt.imshow(copy)
        plt.show()
        pass
    return warning_pixes_index
                
kernel = creat_kernel_3x3()
image = open_image('./test1.jpg')
plt.imshow(image)
plt.show()
image = conv2d_3x3(image, kernel)
warning_pixes_index = check(image, draw=True)
print(warning_pixes_index)
image = open_image('./test2.jpg')
plt.imshow(image)
plt.show()
image = conv2d_3x3(image, kernel)
warning_pixes_index = check(image, draw=True)
print(warning_pixes_index)
