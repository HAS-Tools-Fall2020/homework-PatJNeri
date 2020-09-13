# %%
# Step 1 - Download the data from the USGS website
# https: // waterdata.usgs.gov/nwis/dv?referred_module = sw & site_no = 09506000
# For now you should save this file to the directory you put this script in

# %%
# Step 2 - Import the modules we will use
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
print ("The current working directory is", os.getcwd())
# %% 
# Step 3 - Read in the file in as dataframe
# You will need to change the filename to match what you downloaded
#filename = 'streamflow_week2.txt'
filepath = os.path.join('streamflow_week2.txt')

data=pd.read_table(filepath, sep = '\t', skiprows=30, 
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )
data = data.set_index('datetime')


# %%
# Step 4 - Look at the data
data.shape  # See how many rows and columns the data has
data.head(6) # look at the first x rows of the data
data.tail(6) # look at the last  x rows  of the data

data.iloc[200:3600] # grab any subset of rows to look at
data.flow[11150:11300]  #Grab a subset of just the flow data dat look at
data.loc['1990-01-01']  #find a specific date

# %%
# Step 5 - Make a plot of the data
# Change the numbers on the followin lines to plot a different portion of the data
ax=data.iloc[10550:11300]['flow'].plot(linewidth=0.5)
ax.set_ylabel('Daily Flow [cfs]')
ax.set_xlabel('Date')


# %%
a = np.mean(data.flow, axis=0)
UnderAverage = [i for i in data.flow if i < a]
print (len(UnderAverage))
print (np.mean(UnderAverage))
print (np.std(UnderAverage))
print ()

# %%
