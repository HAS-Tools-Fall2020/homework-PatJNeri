# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd

# %%
data = np.ones((7,3))
data_frame = pd.DataFrame(data, 
                columns = ['data1', 'data2', 'data3'],
                index=['a','b','c','d','e','f','g'])

#A) Change the values for all of the vowel rows to 3
#data[0:1] = [3., 3., 3.]
#data[4:5] = [3., 3., 3.]

# data_frame.loc["a"] *=3   #; Then do the same to 'e' OR
data_frame.loc[['a', 'e']] = 3   #; uses list of rows
# data[(data_frame.index=='a') | (data_frame.index=='e')]=3

#B) multiply the first 4 rows by 7
data_frame = data_frame.iloc[:4, ] * 7
#C) Make the dataframe into a checkerboard  of 0's and 1's using loc
data_frame.loc[['a', 'c', 'e', 'g'], ['data1', 'data3']]=0
data_frame.loc[['b', 'd', 'f'], ['data2']]=0
#D) Do the same thing without using loc

# %%
data_frame = pd.DataFrame([[1, np.nan, 2],
                            [2, 3, 5],
                            [np.nan, 4, 6]])

# %%
# 1) Use the function fill.na to fill the na values with 999
data_frame9 = data_frame.fillna(999)
# %%
# 2) Turn the 999 values back to nas. See how many different ways you can do this
# Alcely
ans1 = np.where(data_frame9 == 999, np.nan, data_frame9)
# Alexa
data_frame9[data_frame9 == 999] = np.nan
# Laura
data_frame9[data_frame.isnull()] = np.nan
# Jill
data_frame9.replace(999, np,nan)
# %%
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_markdown.html
