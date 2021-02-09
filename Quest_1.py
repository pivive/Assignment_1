# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:01:24 2021

@author: Felipe
"""
import numpy as np
import matplotlib.pyplot as plt

Xtest = np.loadtxt("Xtest.txt")
Xtrain = np.loadtxt("Xtrain.txt")
Ytrain = np.loadtxt("Ytrain.txt")

#%% i
#dont forget to load Xtest, Xtrain and Ytrain!!
print("i)")
print("Amount of training examples:",len(Xtest))
print("Amount of test examples:",len(Xtrain))
"""
for i in range (0,10):
    r = np.random.randint(len(Xtest))
    A = np.reshape(Xtest[r],(28,28))
    plt.matshow(A)
    plt.title('Image No: %d' %r)
    plt.show()
"""    
#%% ii
pos_count, neg_count, zero_count = 0, 0, 0
for i in Xtest:   
    if Xtest.any(i) > 0: 
        pos_count += 1  
    elif i < 0: 
        neg_count += 1
    else:
        zero_count += 1
