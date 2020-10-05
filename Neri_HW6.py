# Starter code for week 6 illustrating how to build an AR model 
# and plot it

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
#note you may need to do pip install for sklearn

# %%
# Set the file name and path to where you have stored the data
filename = 'streamflow_week1.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly 
flow_weekly = data.resample("W", on='datetime').mean()

# %%
# Building an autoregressive model 
# You can learn more about the approach I'm following by walking 
# Through this tutorial
# https://realpython.com/linear-regression-in-python/

# Step 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries

Flow_agg = data
Flow_agg['-1'] = Flow_agg['flow'].shift(1)
Flow_agg['-2'] = Flow_agg['flow'].shift(2)
Flow_agg['-3'] = Flow_agg['flow'].shift(3)
Flow_agg['-4'] = Flow_agg['flow'].shift(4)
Flow_agg['-5'] = Flow_agg['flow'].shift(5)
Flow_agg['-6'] = Flow_agg['flow'].shift(6)
Flow_agg['wkly_avg_running'] = (Flow_agg['flow'] + Flow_agg['-1'] + Flow_agg['-2'] + Flow_agg['-3'] + Flow_agg['-4'] + Flow_agg['-5'] + Flow_agg['-6'])/7

flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)

Flow_agg_wk = Flow_agg.resample("W", on='datetime').mean()
Flow_agg_wk['flow_tm1'] = Flow_agg_wk['wkly_avg_running'].shift(1)
Flow_agg_wk['flow_tm2'] = Flow_agg_wk['wkly_avg_running'].shift(2)
# Step 2 - pick what portion of the time series you want to use as training data
# here I'm grabbing the first 800 weeks 
# Note1 - dropping the first two weeks since they wont have lagged data
# to go with them  
train = flow_weekly[2:800][['flow', 'flow_tm1', 'flow_tm2']]
test = flow_weekly[800:][['flow', 'flow_tm1', 'flow_tm2']]

# Step 3: Fit a linear regression model using sklearn 
model = LinearRegression(fit_intercept=False) #NOTE THE CHANGE TO INTERCEPT MADE A DIFFERENCE!!!! fit_intercept=False
x=train['flow_tm1'].values.reshape(-1,1) #See the tutorial to understand the reshape step here 
y=train['flow'].values
model.fit(x,y)

#Look at the results
# r^2 values
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq,2))

#print the intercept and the slope 
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Step 4 Make a prediction with your model 
# Predict the model response for a  given flow value
q_pred_train = model.predict(train['flow_tm1'].values.reshape(-1,1))
q_pred_test = model.predict(test['flow_tm1'].values.reshape(-1,1))

#altrenatievely you can calcualte this yourself like this: 
q_pred = model.intercept_ + model.coef_ * train['flow_tm1']

# you could also predict the q for just a single value like this
last_week_flow = 500
prediction = model.intercept_ + model.coef_ * last_week_flow


# %%
# Another example but this time using two time lags as inputs to the model 
model2 = LinearRegression()
x2=train[['flow_tm1','flow_tm2']]
model2.fit(x2,y)
r_sq = model2.score(x2, y)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# generate preditions with the funciton
q_pred2_train = model.predict(train[['flow_tm1', 'flow_tm2']])

# or by hand
q_pred2 = model2.intercept_   \
         + model2.coef_[0]* train['flow_tm1'] \
         +  model2.coef_[1]* train['flow_tm2'] 

# %% 
# Here are some examples of things you might want to plot to get you started:

# 1. Timeseries of observed flow values
# Note that date is the index for the dataframe so it will 
# automatically treat this as our x axis unless we tell it otherwise
fig, ax = plt.subplots()
ax.plot(flow_weekly['flow'], label='full')
ax.plot(train['flow'], 'r:', label='training')
ax.set(title="Observed Flow", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.legend()
# an example of saving your figure to a file
fig.set_size_inches(5,3)
fig.savefig("Observed_Flow.png")

#2. Time series of flow values with the x axis range limited
fig, ax = plt.subplots()
ax.plot(flow_weekly['flow'], label='full')
ax.plot(train['flow'], 'r:', label='training')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2000, 1, 26), datetime.date(2014, 2, 1)])
ax.legend()


# 3. Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots(figsize=(20,10))
ax.plot(train['flow'], color='grey', linewidth=2, label='observed')
ax.plot(train.index, q_pred_train, color='green', linestyle='--', 
        label='simulated')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.legend()

# 4. Scatter plot of t vs t-1 flow with log log axes
plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='o', s=3,
              color='r', label='obs')
ax.set(xlabel='flow t-1', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()

# 5. Scatter plot of t vs t-1 flow with normal axes
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='p',
              color='blueviolet', label='observations')
ax.set(xlabel='flow t-1', ylabel='flow t')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()

# 6. Attempting to plot the weekly values
#fig, ax = plt.subplots()
#ax
plt.show()


# %%
# comparing the overall histogram of flow and the weekly sample to see if its representative
flow_quants1 = np.quantile(data['flow'], q=[0,0.5, 0.75, 0.9])
print('Method of flow quantiles for all data:', flow_quants1)
flow_quants2 = np.quantile(flow_weekly['flow'], q=[0,0.5, 0.75, 0.9])
print('Method of flow quantiles for all data:', flow_quants2)

# Not sure how to remove the Nan values from the quartile counts....
flow_quants3 = np.quantile(Flow_agg['wkly_avg_running'], q=[0,0.5, 0.75, 0.9])
print('Method of flow quantiles for all data:', flow_quants3)
flow_quants4 = np.quantile(Flow_agg_wk['wkly_avg_running'], q=[0,0.5, 0.75, 0.9])
print('Method of flow quantiles for all data:', flow_quants4)

mybins = np.linspace(0, 400, num=100)
plt.hist(data['flow'], bins = mybins, alpha=0.8, label='All flow')
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

#plt.hist(Flow_agg['wkly_avg_running'], bins = mybins, alpha=0.9)
#plt.title('Streamflow weekly average')
#plt.xlabel('Flow [cfs]')
#plt.ylabel('Count')
#Flow_month = [Flow_agg.iloc[:, 6:7]== 9]
#plt.hist(Flow_agg[Flow_agg['month']== 9, 15], bins = mybins, alpha=0.9)
#plt.title('Streamflow weekly average')
#plt.xlabel('Flow [cfs]')
#plt.ylabel('Count')

#plt.hist(Flow_agg_wk['wkly_avg_running'], bins = mybins, alpha=0.8)
#plt.title('Streamflow')
#plt.xlabel('Flow [cfs]')
#plt.ylabel('Count')

plt.hist(flow_weekly['flow'], bins = mybins, alpha=0.8, label='Weekly flow')
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
plt.legend()
# %%
# This is the final model that I end up using.

train = Flow_agg_wk[400:1000][['wkly_avg_running', 'flow_tm1', 'flow_tm2']]
test = flow_weekly[1000:][['flow', 'flow_tm1', 'flow_tm2']]

# Step 3: Fit a linear regression model using sklearn 
model3 = LinearRegression(fit_intercept=False) #NOTE THE CHANGE TO INTERCEPT MADE A DIFFERENCE!!!! fit_intercept=False
x3=train['flow_tm1'].values.reshape(-1,1) #See the tutorial to understand the reshape step here 
y=train['wkly_avg_running'].values
model3.fit(x3,y)

#Look at the results
# r^2 values
r_sq = model3.score(x3, y)
print('coefficient of determination:', np.round(r_sq,2))

#print the intercept and the slope 
print('intercept:', np.round(model3.intercept_, 2))
print('slope:', np.round(model3.coef_, 2))

# Step 4 Make a prediction with your model 
# Predict the model response for a  given flow value
q_pred_train = model3.predict(train['flow_tm1'].values.reshape(-1,1))
q_pred_test = model3.predict(test['flow_tm1'].values.reshape(-1,1))

#altrenatievely you can calcualte this yourself like this: 
q_pred = model3.intercept_ + model3.coef_ * train['flow_tm1']

fig, ax = plt.subplots(figsize=(20,10))
ax.plot(Flow_agg_wk['wkly_avg_running'], color='grey', linewidth=2, label='observed')
ax.plot(test.index, q_pred_test, color='green', linestyle='--', 
        label='simulated')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2004, 1, 26), datetime.date(2020, 8, 19)])
ax.legend()

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['wkly_avg_running'], marker='o', s=3,
              color='r', label='obs')
ax.set(xlabel='flow t-1', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()

# %%
last_week_flow = 29.12739274
prediction = model3.intercept_ + model3.coef_ * last_week_flow
print(prediction)
# %%
