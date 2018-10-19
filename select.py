# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 12:55:55 2018

@author: wmy
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def divide_into_groups():  
    group = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    while True:
        if len(group) == 0:
            group = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            pass
        ch = input()
        if ch == 'q' or ch == 'Q':
            break
        result = random.choice(group)
        group.remove(result)
        print('\n\n\n\n\n\n\n\n\n')
        image = plt.imread(result + '.png')
        plt.imshow(image)
        plt.axis('off')
        plt.show()
        print("Your group id is '" + result + "'.")
        pass
    pass

if __name__ == '__main__':
    divide_into_groups()
    pass

    
