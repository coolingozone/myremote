import numpy as np
from datetime import datetime
import math
import matplotlib.pyplot as plt
import matplotlib
csv = np.genfromtxt ("reading2_20170807.csv", dtype=[('name','|S8'),('time','<f8'),('node1','|S5'),('value','<f8')],delimiter=",",skip_header=1)

m1=np.array([row[1] for row in csv])
m2=np.array([row[3] for row in csv])
data = np.dtype([('timestamp', np.datetime64), ('value', np.float64,)])
data=np.array([m1,m2])
data=np.transpose(data)
nonan=~np.isnan(data[:,0])
data=data[nonan,:]

dat=[]
bbw=[]
#dt = np.dtype([('timestamp', np.datetime64), ('value', np.float64,),('day',np.int)])
#dtt=[]
for i in range(0,len(data),1):
    t=data[i][0]/1000000000
    #dd=np.array(datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S'))
    #dd=np.array(datetime.datetime.fromtimestamp(t)).astype(datetime)
    mm=datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
    dd=np.datetime64(mm).astype(datetime)
    bb=datetime.weekday(dd)
    dat.append(dd)
    bbw.append(bb)

#xp = matplotlib.dates.date2num(dat)
#print dat
#plt.scatter(data[:,0],data[:,1])
fig, (ax1) = plt.subplots(nrows = 1, sharex = True)
ax1.plot(bbw, data[:,1], marker=u'+')
#ax2.plot(bbw, data[:,1], 'r-')
#print dat[0:10]
#fig, ax = plt.subplots()
#ax.plot_date(dat, data[:,1],xdate=True,ydate=True)
#plt.plot(dat,data[:,1])
plt.show()



