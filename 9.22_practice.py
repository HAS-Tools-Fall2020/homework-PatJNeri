#%%
import numpy as np
import pandas as pd
                                                     
# %%
a1 = np.random.randint(9, size=(3,3)) #then add 1 to all values

# print(np.array(range(2,11).reshape(3,3))
# %%
a2 = np.reshape(np.arange(2,34,2), (4,4)) #

# x=np.arange(2,33,2).reshape(4,4)

#%%
#1. Get the largest integer that is less than or equal to the division
# of the inputs x1 and x2 where x1 is all the integers from 1-10 and x2=1.3

x1 = np.arange(1,11,1)
print(x1)  # etc.
# one line  
x1 = np.divide(np.arange(1,11,1),1.3).astype(int)
# %%
# 2. given an array x1=[0, 4, 37,17] and a second array with the values
# x2=[1.2, 3, 4.6, 7] return x1/x2 rounded to two decimal places
x1=[0, 4, 37,17]
x2=[1.2, 3, 4.6, 7]
ans = np.round(np.divide(x1,x2), decimals=2)  #the round is VERY useful

#%%
# 3. Create a 10 by 100 matrix with 1000 random numbers and report the 
# average and standard deviation across the entire matrix and 
# for each of the 10 rows. Round your answer to  two decimal places

#np.random, np.round, np.mean, np.std