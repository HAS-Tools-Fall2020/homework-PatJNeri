# Example solution for HW 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week1.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

#filepath = '../Assignments/Solutions/data/streamflow_week1.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :) 
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.
data.info()
data.head()
data.iloc[:, 3:4] #gives all flow column values, can narrow range with first column numbers
data_2019 = data[data["year"] == 2019]
data_2019_9 = data_2019[data_2019["month"] == 9]
data.sort_values("flow") #will show top flow and bot flow

#%%
#run thru all months, I'm sure there is an iterative way to do this
data_month = data[data["month"] == 12]
# data_month["flow"].describe()
data_month.sort_values("flow")

#%%
i = 12
data_month = data[data["month"] == i]
data_month.sort_values("flow")

# %%
mybins = np.linspace(0, 300, num=70)
plt.hist(data_month["flow"], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
# %%
f, ax = plt.subplots()
data_2019.plot(x="___________",
                        y="flow",
                        title="Plot of Flow",
                        ax=ax)
plt.show()

# %%
data_Recent = data[data["year"] < 2010]
data_2019 = data[data["year"] == 2019]
data_2019_8 = data_2019[data_2019["month"] == 8]
data_2019_9 = data_2019[data_2019["month"] == 9]
data_2019_10 = data_2019[data_2019["month"] == 10]
data_2019_11 = data_2019[data_2019["month"] == 11]
data_2019_12 = data_2019[data_2019["month"] == 12]
#flow_wk1_avg = # 8/30 - 9/5; 8/30 is index # 11198 flow = 38.4
#flow_wk2_avg = #9/6 - 9/12; 9/6 is index # 11205 flow = 61.5
#flow_wk3_avg = #9/13 - 9/19; 9/13 is index # 11212 = 52.2
#flow_wk4_avg = #9/20 - 9/26; 9/20 is index # 11219 = 57.1
#flow_wk5_avg = #9/27 - 10/3; # 11226 flow = 126
#flow_wk6_avg = #10/4 - 10/10 # 11233 flow = 80.4
#flow_wk7_avg = #10/11 - 10/17 # 11240 flow = 90.8
#flow_wk8_avg = #10/18 - 10/24 # 11247 flow = 74.3
#flow_wk9_avg = #10/25 - 10/31 # 11254 flow = 83.0
#flow_wk10_avg = #11/1 - 11/7 # 11261 flow = 118.0
#flow_wk11_avg = #11/8 - 11/14 # 11268 flow = 132.0
#flow_wk12_avg = #11/15 - 11/21 # 11275 flow = 131.0
#flow_wk13_avg = #11/22 - 11/28 # 11282 flow = 279.0
#flow_wk14_avg = #11/29 - 12/5 # 11289 flow = 533.0
#flow_wk15_avg = #12/6 - 12/12 # 11296 flow = 4390.0
#flow_wk16_avg = #12/13 - 12/19 # 11303 flow = 499.0
# %%
plt.plot( __________, data_month["flow"], label = "month")
# %%
guesses = [114.0,65.0,84.0,89.0,59.0,120.0,110.0,80.0,123.0,160.0,132.0,182.0,205.0,225.0,180.0,204.0]
last_year = [38.4, 61.5, 52.2, 57.1, 126.0, 80.4, 90.8, 74.3, 83.0, 118.0, 132.0, 131.0, 279.0, 533.0, 4390.0, 499.0]
# %%
i = 16
suum = guesses[i] + last_year[i]
print(suum*0.5)
# %%
