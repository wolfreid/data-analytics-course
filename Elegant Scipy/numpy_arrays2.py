# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 11:49:46 2025

@author: Roman.Prylypko
"""
import numpy as np
# Create an ndarray x
x = np.array([1, 2, 3], np.int32)
print(x)

y = np.copy(x[:2])
#y = x[:2]
print(y)
print(x)

y[0] = 6
print(y)
print(x)