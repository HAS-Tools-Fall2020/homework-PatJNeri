#  Patrick Neri Prediction Code for Week #7
#  Greetings and good luck! I will include comments to help decode the madness

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# %%


def Week_pred(week, shift1, shift2, shift3):
    """
    This utilizes a Linear Model with 3 consecutive week averages as an input.
    Assumes a model of:
    (intercept) + (Coef0 * shift1) + (Coef1 * shift2) + Coef2 + shift3)
    week = Integer value for how many week you would like to run the model out.
    shift1 = the most recent value
    shift2 = the second most recent value
    shift3 = the third most recent value
    """
    q_predict = np.zeros(week)
    for i in range(0, week):
        q_predict_i = model.intercept_ \
            + model.coef_[0] * shift1 \
            + model.coef_[1] * shift2\
            + model.coef_[2] * shift3
        q_predict[i] = q_predict_i
        shift3 = shift2
        shift2 = shift1
        shift1 = q_predict_i
    return q_predict


# %%
# Here it is, the hardest part of making the program work. In the readme file I
# have given directions to hopefully make it work
filename = 'streamflow_week1.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)
# %%
# Read the data into a pandas df
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow',
                            'code'], parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly average
flow_weekly = data.resample("W", on='datetime').mean()
# %%
# So this plot shows all month flow_weekly values. Quantiles are given and
# used to set the colors of the lines each year. These are helpful to form an
# opinion to what data to include in the model. Months for our prediction span
# are 8 thru 12 in this class. Could do a for loop over this value if needed.
mnth = 9

flow_weekly_mnth = flow_weekly[flow_weekly['month'] == mnth]
flow_quants_mnth = np.quantile(flow_weekly_mnth['flow'], q=[0, 0.5, 0.75, 0.9])
print('Method of flow quantiles for month ', mnth, ':', flow_quants_mnth)
print('For plots, Green is flow max above 75%, and Red is below 50%')
fig = plt.figure(figsize=(30, 10))
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 31):
    flow_weekly_mnth_i = flow_weekly_mnth[flow_weekly_mnth['year'] ==
                                          (i + 1990)]
    ax = fig.add_subplot(3, 10, i)
    if (np.max(flow_weekly_mnth_i['flow']) > flow_quants_mnth[2]):
        ax.plot(flow_weekly_mnth_i['flow'], '-g', label='full')
    elif (np.max(flow_weekly_mnth_i['flow']) < flow_quants_mnth[1]):
        ax.plot(flow_weekly_mnth_i['flow'], '-r', label='full')
    else:
        ax.plot(flow_weekly_mnth_i['flow'], '-b', label='full')
# %%
# Looking at the various graph of the months and noting that this year has
# overall been a low flow year, I limit my allowed flow to 2010 or later.
# (prefer 2015 or later, as they are most similar to this year)
# Other then that, same steps as given model.

# Could probably parameterize this step if more data needed
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)
flow_weekly['flow_tm3'] = flow_weekly['flow'].shift(3)

# This period is from start of 2010 to start of 2015
train = flow_weekly[1096:1357][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3']]
test = flow_weekly[1357:][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3']]

# Including a no intercept model to allow for low values, IMPORTANT
# because it is a low flow year.
model = LinearRegression(fit_intercept=False)
x = train[['flow_tm1', 'flow_tm2', 'flow_tm3']]
y = train['flow'].values
model.fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 4))
# %%
q_pred_train = model.predict(train[['flow_tm1', 'flow_tm2', 'flow_tm3']])
q_pred_test = model.predict(test[['flow_tm1', 'flow_tm2', 'flow_tm3']])
plt.style.use('seaborn-darkgrid')
plot_diff = np.absolute(test['flow'] - q_pred_test)/test['flow']
# Line plot of Training data vs. Predicted over training
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(train['flow'], color='grey', linewidth=2, label='observed')
ax.plot(test['flow'], color='b', linewidth=2, label='observed')
ax.plot(train.index, q_pred_train, color='green', linestyle='--',
        label='simulated')
ax.plot(test.index, q_pred_test, color='r', linestyle='--',
        label='simulated')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       yscale='log', xlim=[datetime.date(2010, 1, 1),
                           datetime.date(2020, 12, 30)])
ax.legend()

# ax.plot(test['flow'], color='b', linewidth=2, label='observed')
# ax.plot(test.index, q_pred_test, color='g', linestyle='--',
#       label='simulated')
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(plot_diff, color='r', linewidth=2, label='diff')

ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       xlim=[datetime.date(2015, 1, 1),
             datetime.date(2020, 12, 30)])
ax.legend()

# Scatter plot of t vs t-n flow with log log axes
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='o', s=3,
           color='r', label='obs')
ax.set(xlabel='flow t-1', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()

fig, ax = plt.subplots()
ax.scatter(train['flow_tm2'], train['flow'], marker='o', s=3,
           color='r', label='obs')
ax.set(xlabel='flow t-2', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm2']), np.sort(q_pred_train), label='AR model')
ax.legend()

fig, ax = plt.subplots()
ax.scatter(train['flow_tm3'], train['flow'], marker='o', s=3,
           color='r', label='obs')
ax.set(xlabel='flow t-3', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm3']), np.sort(q_pred_train), label='AR model')
ax.legend()

# %%
# Pick out the last 3 values in the flow_weekly dataset
flow_weekly.tail
# then run the Week_pred(week, shift1, shift2, shift3) program for 2 weeks
# %%
