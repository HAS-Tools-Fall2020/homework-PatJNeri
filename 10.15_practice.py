# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# %%
data = np.random.rand(4, 5)
np.mean(data, axis=0)
# to make functions

def get_mean(data):
    mean = data.mean(axis=0)
    return mean

get_mean(data)

def get_mean2(data):
    ans=[]
    for i in range(5):
        ans.append(data[:,i].mean())
    return ans

get_mean2(data)

def simple_mean(input):
    average = np.mean(input)
    return average

average = np.zeros(data.shape[1])
for i in range(data.shape[1]):
    average[i] = simple_mean(data[:,i])

#%%

