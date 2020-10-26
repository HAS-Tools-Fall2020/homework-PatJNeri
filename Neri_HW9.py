# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from sklearn.linear_model import LinearRegression
import os
import json
import urllib.request as req
import urllib

# %%
# Separated into 2 to divide between the availible data of Daymet
# (should just have one and call separate, need to fix)
filename = 'streamflow_week9_part1.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)
flow1 = pd.read_table(filepath, sep='\t', skiprows=29,
                      names=['agency_cd', 'site_no', 'datetime', 'flow',
                             'code'], parse_dates=['datetime']
                      )
flow1['year'] = pd.DatetimeIndex(flow1['datetime']).year
flow1['month'] = pd.DatetimeIndex(flow1['datetime']).month
flow1['day'] = pd.DatetimeIndex(flow1['datetime']).day
flow1['dayofweek'] = pd.DatetimeIndex(flow1['datetime']).dayofweek
filename = 'streamflow_week9_part2.txt'
filepath = os.path.join('data', filename)
flow2 = pd.read_table(filepath, sep='\t', skiprows=30,
                      names=['agency_cd', 'site_no', 'datetime', 'flow',
                             'code'], parse_dates=['datetime']
                      )
flow2['year'] = pd.DatetimeIndex(flow2['datetime']).year
flow2['month'] = pd.DatetimeIndex(flow2['datetime']).month
flow2['day'] = pd.DatetimeIndex(flow2['datetime']).day
flow2['dayofweek'] = pd.DatetimeIndex(flow2['datetime']).dayofweek
flowtot = flow1.append(flow2, ignore_index=True)
# %%
# Daymet Data:
# You can get Daymet data for a single pixle form this site:
# https: // daymet.ornl.gov/single-pixel/
# This lat & lon is the same as the data for the streamflow chosen.
lat = '34.26'
lon = '-111.47'
strtdate = '1990-01-01'
enddate = '2019-12-31'
# Example reading it as a json file
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=" + lat + "&lon=" \
       + lon + "&vars=prcp,srad,tmax,tmin&start=" + strtdate + "&end=" \
       + enddate + "&format=json"
response = req.urlopen(url)
# Look at the kesy and use this to grab out the data
responseDict = json.loads(response.read())
responseDict['data'].keys()
year = responseDict['data']['year']
yearday = responseDict['data']['yday']
precip = responseDict['data']['prcp (mm/day)']
shrtwve = responseDict['data']['srad (W/m^2)']
Tmax = responseDict['data']['tmax (deg c)']
Tmin = responseDict['data']['tmin (deg c)']

# %%
# This is done because the Daymet data set for whatever reason appears to not
# count leap days, so the indexed numbers are all 2/29 days.
flow1_corrected = flow1.drop([789, 2250, 3711, 5172, 6633, 8094, 9555])

# %%
Mod_data = pd.DataFrame({'datetime': flow1_corrected['datetime'],
                         'year': flow1_corrected['year'],
                         'month': flow1_corrected['month'],
                         'day': flow1_corrected['day'],
                         'DoW': flow1_corrected['dayofweek'],
                         'flow': flow1_corrected['flow'],
                         'precip': precip, 'shrtwve': shrtwve,
                         'Tmax': Tmax, 'Tmin': Tmin})
Mod_data_wkly = Mod_data.resample("W", on='datetime').mean()
Mod_data_wkly['flow_s1'] = Mod_data_wkly['flow'].shift(1)
Mod_data_wkly['flow_s2'] = Mod_data_wkly['flow'].shift(2)
Mod_data_wkly['flow_s3'] = Mod_data_wkly['flow'].shift(3)
# %%
# Mesonet
# Here are some helpful links for getting started
# https: // developers.synopticdata.com/about/station-variables/
# https: // developers.synopticdata.com/mesonet/explorer/
# Insert your token here
mytoken = '5b1fc31e931b4559a20dac65e4a9610c'
base_url = "http://api.mesowest.net/v2/stations/timeseries"

# Specific arguments for the data that we want
args = {
    'start': '199701010000',
    'end': '202010240000',
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
    'token': mytoken}
apiString = urllib.parse.urlencode(args)
fullUrl = base_url + '?' + apiString
print(fullUrl)

response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())

# The complete format of this dictonary is descibed here:
# https://developers.synopticdata.com/mesonet/v2/getting-started/

# Long story short we can get to the data we want like this:
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

# Now we can combine this into a pandas dataframe
data = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))

# Now convert this to daily data using resample
data_daily = data.resample('D').mean()

# %%
# This matches the Timeframe for above MesoWest dataset data_daily
Mod_data_2 = flowtot[2557:11254]
Mod_data_2.reset_index(inplace=True)
data_daily.reset_index(inplace=True)
Mod_data_2['Temp'] = data_daily['Temperature'].shift(1)
# %%
Mod_data_wkly2 = Mod_data_2.resample("W", on='datetime').mean()
Mod_data_wkly2['flow_s1'] = Mod_data_wkly2['flow'].shift(1)
Mod_data_wkly2['flow_s2'] = Mod_data_wkly2['flow'].shift(2)
Mod_data_wkly2['flow_s3'] = Mod_data_wkly2['flow'].shift(3)

# %%
# Produces a comparison graph of flow vs. Temp
# In gen, shows at lower temp seasons, there is higher flow
plt.style.use('seaborn-darkgrid')
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels=[], ylim=(0, 120))
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(10, 5000), yscale='log')
ax1.plot(Mod_data_wkly2['Temp'], '-b')
ax2.plot(Mod_data_wkly2['flow'], 'r')
# %%
train = Mod_data_wkly2.iloc[1000:]

# Including a no intercept model to allow for low values, IMPORTANT
# because it is a low flow year.  (fit_intercept=False)
model = LinearRegression()
x = train[['flow_s1', 'flow_s2', 'flow_s3', 'Temp']]
y = train['flow'].values
model.fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 5))
q_pred_train = model.predict(train[['flow_s1',
                                    'flow_s2', 'flow_s3', 'Temp']])
fig, ax = plt.subplots()
ax.scatter(train['flow_s1'], train['flow'], marker='o', s=3,
           color='r', label='obs')
ax.set(xlabel='flow t-1', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_s1']), np.sort(q_pred_train), label='AR model')
ax.legend()
# %%
q_pred_test = model.predict(Mod_data_wkly2.iloc[5:][['flow_s1', 'flow_s2', 'flow_s3', 'Temp']])

# %%
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(Mod_data_wkly2.index, Mod_data_wkly2['flow'], color='grey', linewidth=2, label='observed')
ax.plot(q_pred_test, color='r', linestyle='--',
        label='simulated')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
ax.legend()
# %%
