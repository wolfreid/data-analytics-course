# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 11:39:40 2025

@author: Roman.Prylypko
"""
import numpy as np

array = np.arange(1e-5,)

print(array.shape)
list_array = array.tolist()
%timeit -n10 y = [val * 5 for val in list_array]

#%quickref

a = %cd
%timeit print("hello")


