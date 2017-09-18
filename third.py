import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import math 

df=pd.read_csv('reading2_20170807.csv',names=['name', 'time', 'node1', 'value'],skiprows=1)
df=pd.DataFrame(df.ix[:,['time','value']],columns=['name','time','node1','value'])

df['time'] = pd.to_numeric(df['time'], errors='coerce')
df['value'] = pd.to_numeric(df['value'], errors='coerce')
df['time']=df['time']/1000000000
df['time']=pd.to_datetime(df['time'],unit='s')
df['time']=df['time'].dt.tz_localize('UTC').dt.tz_convert('Asia/Singapore')
df['day_of_week'] = df['time'].dt.weekday
df['hour']=df['time'].dt.hour
df.set_index('time',inplace=True)
#df['hour']=df['realtime'].dt.hour
#print df
figf, (axf) = plt.subplots(nrows = 1, sharex = True)
axf.scatter(df['day_of_week'], df['value'], alpha=0.5)
grouped=df.groupby(['day_of_week','hour']).mean()
#new=grouped.aggregate(np.mean)
day=['Mon','Tues','Wed','Thur','Fri','Sat','Sun']
#print temp['value'].shape
fig, (ax1) = plt.subplots(nrows = 1, sharex = True)
for i in range(0,7,1):
  #ax1.plot(grouped.loc[i], marker=u'+')
  temp= grouped.loc[i]
  ax1.scatter(range(0,24,1),temp['value'].T,alpha=0.5,label=day[i])
legend = ax1.legend(loc='upper right', shadow=True)
fig2, am = plt.subplots(nrows = 7, sharex = True)
for i in range(0,7,1):
  temp= grouped.loc[i]
  am[i].scatter(range(0,24,1),temp['value'].T,alpha=0.5)
fig3, at = plt.subplots(nrows = 1, sharex = True)
for i in range(0,7,1):
  temp= grouped.loc[i]
  hb=at.hexbin(range(0,24,1),temp['value'].T,cmap='inferno')

cb = fig3.colorbar(hb, ax=at)

cb.set_label('counts')
#ax1.plot(df['day_of_week'], df['value'], marker=u'+')
#plt.plot(grouped.loc[0.0])
#plt.plot(grouped.loc[1.0])
#print new.get_group['0']



plt.show()