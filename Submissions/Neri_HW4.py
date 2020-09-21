# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data

filename = 'streamflow_week2.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

#%%
# Count the number of values with flow > mean and month ==Y
Y = 9
all_time_mean = np.mean(flow_data[:,3])
all_time_max = np.max(flow_data[:,3])
flow_month = flow_data[flow_data[:,1]==Y, 3]
month_max = np.max(flow_month)
month_mean = np.mean(flow_month)
flow_count = np.sum((flow_data[:,3] > month_mean) & (flow_data[:,1]==Y))
print('The number of days in month', Y, 'is', flow_month.size)
print('The mean flow of month', Y, 'is' ,month_mean)
if all_time_mean > month_mean:
        print('This is less than the total average, ', all_time_mean)
elif all_time_mean == month_mean:
        print('This is the same as the total average')
else:
        print('This is more than the total average, ', all_time_mean)
print('The number of times the flow was higher is', flow_count, 'with a maximum of', month_max) 
print('This is ', ((flow_count)/(flow_month.size))*100. , '% of the time')
# %%
# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, all_time_mean, num=70)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.5, 0.75, 0.9])
print('Method of flow quantiles for all data:', flow_quants1)

plt.hist(flow_month, bins = mybins)
plt.title('Streamflow Month')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

flow_quants2 = np.quantile(flow_month, q=[0,0.5, 0.75, 0.9])
print('Method of flow quantiles for month:', flow_quants2)
# %%
# This part is for accurate prediction (probably too ambitious)
#flow_wk1_avg = # 8/30 - 9/5
#flow_wk2_avg = #9/6 - 9/12
#flow_wk3_avg = #9/13 - 9/19
#flow_wk4_avg = #9/20 - 9/26
#flow_wk5_avg = #9/27 - 10/3
#flow_wk6_avg = #10/4 - 10/10
#flow_wk7_avg = #10/11 - 10/17
#flow_wk8_avg = #10/18 - 10/24
#flow_wk9_avg = #10/25 - 10/31
#flow_wk10_avg = #11/1 - 11/7
#flow_wk11_avg = #11/8 - 11/14
#flow_wk12_avg = #11/15 - 11/21
#flow_wk13_avg = #11/22 - 11/28
#flow_wk14_avg = #11/29 - 12/5
#flow_wk15_avg = #12/6 - 12/12
#flow_wk16_avg = #12/13 - 12/19
flow_count2 = np.sum((flow_data[:,3] > 84) & (flow_data[:,1]==9))
print(flow_count2)
# %%
flow_count3 = np.sum((flow_data[:,3] > 84) & (flow_data[:,1]==9) & (flow_data[:,0] > 2009))
print(flow_count3)
# %%
First_Half = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] < 15),3]
Second_Half = flow_data[(flow_data[:,1]==9) & (flow_data[:,2] > 15),3]
mybins = np.linspace(0, all_time_mean, num=70)
plt.hist(Second_Half, bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

plt.hist(First_Half, bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# %%
