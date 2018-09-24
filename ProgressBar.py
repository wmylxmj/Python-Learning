# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:55:12 2018

@author: wmy
"""

import time

scale = 50

#print('start'.center(scale//2, '-'))

t = time.clock()

for i in range(scale + 1):
    a = '@' * i
    b = '-' * (scale - i)
    c = (i/scale) * 100
    t -= time.clock()
    print('\r[{}{}]{:^0.3f}%'.format(a, b, c), end='')
    time.sleep(0.5)
    pass
#print('\n' + 'end'.center(scale//2,'-'))
