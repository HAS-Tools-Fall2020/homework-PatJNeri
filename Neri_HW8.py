#  Patrick Neri Prediction Code for Week #8
#  Greetings and good luck! I will include comments to help decode the madness
# ReadMe file can be found in the core_review_final folder.
# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# %%

# LC - really nice documentation 
# These functions are very similar - you could potentially combine into one 
# where the week outlook is one of the input variables. 
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


def Week_pred2(week, shift1, shift2, shift3):
    """
    This utilizes a Linear Model with 3 consecutive week averages as an input.
    Same as Week_pred function but uses model 2.
    Assumes a model of:
    (intercept) + (Coef0 * shift1) + (Coef1 * shift2) + Coef2 + shift3)
    week = Integer value for how many week you would like to run the model out.
    shift1 = the most recent value
    shift2 = the second most recent value
    shift3 = the third most recent value
    """
    q_predict = np.zeros(week)
    for i in range(0, week):
        q_predict_i = model2.intercept_ \
            + model2.coef_[0] * shift1 \
            + model2.coef_[1] * shift2\
            + model2.coef_[2] * shift3
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
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly average
flow_weekly = data.resample("W", on='datetime').mean()
flow_weekly['day'] = flow_weekly.index.day
# %%
# So this plot shows all month flow_weekly values. Quantiles are given and
# used to set the colors of the lines each year. These are helpful to form an
# opinion to what data to include in the model. Months for our prediction span
# are 8 thru 12 in this class. Could do a for loop over this value if needed.
mnth = 8
data_mnth = data[data['month'] == mnth]
flow_weekly_mnth = flow_weekly[flow_weekly['month'] == mnth]
flow_quants_mnth = np.quantile(flow_weekly_mnth['flow'], q=[0, 0.5, 0.75, 0.9])
print('Method of flow quantiles for month ', mnth, ':', flow_quants_mnth)
print('For plots, Green is flow max above 75%, and Red is below 50%')
fig = plt.figure(figsize=(30, 10))
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 31):
    curr_yr = (i + 1990)
    flow_weekly_mnth_i = flow_weekly_mnth[flow_weekly_mnth['year'] ==
                                          curr_yr]
    data_mnth_i = data_mnth[data_mnth['year'] == curr_yr]
    ax = fig.add_subplot(3, 10, i)
    if (np.max(flow_weekly_mnth_i['flow']) > flow_quants_mnth[2]):
        ax.plot(flow_weekly_mnth_i['day'], flow_weekly_mnth_i['flow'],
                '-g', label='full')
        ax.plot(data_mnth_i['day'], data_mnth_i['flow'], color='grey')
    elif (np.max(flow_weekly_mnth_i['flow']) < flow_quants_mnth[1]):
        ax.plot(flow_weekly_mnth_i['day'], flow_weekly_mnth_i['flow'],
                '-r', label='full')
        ax.plot(data_mnth_i['day'], data_mnth_i['flow'], color='grey')
    else:
        ax.plot(flow_weekly_mnth_i['day'], flow_weekly_mnth_i['flow'],
                '-b', label='full')
        ax.plot(data_mnth_i['day'], data_mnth_i['flow'], color='grey')
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
# LC - you could set these inputs numbers as variables and also link them to dates. 
train = flow_weekly[1096:1357][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3']]
test = flow_weekly[1357:][['flow', 'flow_tm1', 'flow_tm2', 'flow_tm3']]

# Including a no intercept model to allow for low values, IMPORTANT
# because it is a low flow year.  (fit_intercept=False)
model = LinearRegression()
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
plot_diff = (test['flow'] - q_pred_test)/test['flow']
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

# shows that there is a positive bias, aka the model is too high.
# looking specifically at 2020 it is almost double the seen value
# for the past half of the year.
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(plot_diff, color='r', linewidth=2, label='diff')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       xlim=[datetime.date(2015, 1, 1),
             datetime.date(2020, 12, 30)])
ax.legend()

# %%
# Scatter plot of t vs t-n flow with log log axes
# Notice as the t-n gets higher, there seems to be less clear of a trend
ax.scatter(train['flow_tm1'], train['flow'], marker='o', s=3,
           color='r', label='obs')
ax.set(xlabel='flow t-1', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()

ax.scatter(train['flow_tm2'], train['flow'], marker='o', s=3,
           color='r', label='obs')
ax.set(xlabel='flow t-2', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm2']), np.sort(q_pred_train), label='AR model')
ax.legend()

ax.scatter(train['flow_tm3'], train['flow'], marker='o', s=3,
           color='r', label='obs')
ax.set(xlabel='flow t-3', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm3']), np.sort(q_pred_train), label='AR model')
ax.legend()

# %%
# Proof that this year is completely different then any previous year
# make sure to update the xlim as dataset grows (set to current date)
data_mnth_r = data[data['month'] > 7]
flow_weekly_mnth_r = flow_weekly[flow_weekly['month'] > 7]
flow_quants_mnth_b = np.quantile(flow_weekly_mnth_r['flow'],
                                 q=[0, 0.5, 0.75, 0.9])
print('Method of flow quantiles for month ', '8-12', ':', flow_quants_mnth_b)
print('For plots, Green is flow max above 75%, and Red is below 50%')
fig = plt.figure(figsize=(30, 10))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

# LC - the lines of code that are repeated exactly in your if else statements
# Can be moved outside this logic so you don't have to repeat it
for i in range(1, 31):
    curr_yr = (i + 1990)
    flow_weekly_mnth_i = flow_weekly_mnth_r[flow_weekly_mnth_r['year'] ==
                                            curr_yr]
    data_mnth_i = data_mnth_r[data_mnth_r['year'] == curr_yr]
    ax = fig.add_subplot(3, 10, i)
    if (np.max(flow_weekly_mnth_i['flow']) > flow_quants_mnth[2]):
        ax.plot(flow_weekly_mnth_i.index, flow_weekly_mnth_i['flow'],
                '-g', label='full')
        ax.plot(data_mnth_i.datetime, data_mnth_i['flow'], color='grey')
        ax.set(title=curr_yr, xlim=[datetime.date(curr_yr, 8, 1),
                                    datetime.date(curr_yr, 10, 14)],
               ylim=[0, 2*np.mean(flow_weekly_mnth_i['flow'])])
    elif (np.max(flow_weekly_mnth_i['flow']) < flow_quants_mnth[1]):
        ax.plot(flow_weekly_mnth_i.index, flow_weekly_mnth_i['flow'],
                '-r', label='full')
        ax.plot(data_mnth_i.datetime, data_mnth_i['flow'], color='grey')
        ax.set(title=curr_yr, xlim=[datetime.date(curr_yr, 8, 1),
                                    datetime.date(curr_yr, 10, 14)],
               ylim=[0, 2*np.mean(flow_weekly_mnth_i['flow'])])
    else:
        ax.plot(flow_weekly_mnth_i.index, flow_weekly_mnth_i['flow'],
                '-b', label='full')
        ax.plot(data_mnth_i.datetime, data_mnth_i['flow'], color='grey')
        ax.set(title=curr_yr, xlim=[datetime.date(curr_yr, 8, 1),
                                    datetime.date(curr_yr, 10, 14)],
               ylim=[0, 2*np.mean(flow_weekly_mnth_i['flow'])])
# %%
flow_weekly['datetime'] = flow_weekly.index
train2 = flow_weekly[1635:][['datetime', 'flow', 'flow_tm1', 'flow_tm2',
                             'flow_tm3']]

# Including a no intercept model to allow for low values, IMPORTANT
# because it is a low flow year.  (fit_intercept=False)
model2 = LinearRegression()
x = train2[['flow_tm1', 'flow_tm2', 'flow_tm3']]
y = train2['flow'].values
model2.fit(x, y)
r_sq = model2.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 4))
q_pred_train2 = model2.predict(train2[['flow_tm1',
                                       'flow_tm2', 'flow_tm3']])
fig, ax = plt.subplots()
ax.scatter(train2['flow_tm1'], train2['flow'], marker='o', s=3,
           color='r', label='obs')
ax.set(xlabel='flow t-1', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train2['flow_tm1']), np.sort(q_pred_train2), label='AR model')
ax.legend()
# %%
# Updated model showing the new improvement if we decide that only this year
# is relevant in our predictions. Note I think the index for q_pred_train2
# is off by a week maybe? Need to look at closer...
data_2020 = data[data['year'] == 2020]
flow_weekly_2020 = flow_weekly[flow_weekly['year'] == 2020]
q_pred_train2_graph = pd.DataFrame(model2.predict(train2[['flow_tm1',
                                                          'flow_tm2',
                                                          'flow_tm3']]),
                                   train2['datetime'])
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(data_2020.datetime, data_2020['flow'], color='grey')
ax.plot(flow_weekly_2020.index, flow_weekly_2020['flow'], '-b')
ax.plot(q_pred_train2_graph, 'r')
ax.set(yscale='log')
ax.legend()
# %%
# adjust based on 3 of weeks (make sure to check the streamflow doc used)
forecast = Week_pred2(16, flow_weekly.iloc[-1][['flow']],
                      flow_weekly.iloc[-2][['flow']],
                      flow_weekly.iloc[-3][['flow']])
print(forecast)
# %%
