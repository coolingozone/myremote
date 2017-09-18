#import  csv package
import csv
import datetime
from datetime import timedelta
from operator import itemgetter
import tzlocal  # $ pip install tzlocal
import numpy as np
#function to read in the csv file and convert to datetime and float
def readcsv(datafile):
  #data file name

  df=[]
  #read in csv file into 2d array call data

  data=list(csv.reader(open(datafile)))
  #dd=[str(data[1][0]),datetime(1970,1,1)+timedelta(seconds=int(data[1][1][0:12])),str(data[1][2]),float(data[1][3])]
  dd=[str(data[1][0]),datetime.datetime.fromtimestamp(int(data[1][1][0:10])).strftime('%Y-%m-%d %H:%M:%S'),str(data[1][2]),float(data[1][3])]
  df.append(dd)
  #print df
 
  #df.append(datetime.datetime.strptime(data[1][0],"%Y-%m"))
  #for i in range(2,80000,1):
  for i in range(2,len(data),1):
    #print int(data[i][1][0:9].isdigit()) 
    if(data[i][1][0:10].isdigit()):
      #dd=[str(data[i][0]),datetime(1970,1,1,0,0,0)+timedelta(seconds=int(data[1][1][0:10])),str(data[i][2]),float(data[i][3])]
      dd=[str(data[i][0]),datetime.datetime.fromtimestamp(int(data[i][1][0:10])).strftime('%Y-%m-%d %H:%M:%S'),str(data[i][2]),float(data[i][3])]
      df.append(dd)
      #print i
  df=np.delete(df,[0,2],axis=1)
  return df
  
df=readcsv("reading2_20170807.csv")
print df[0:2]
print df[80000:80001]
value=df[1].T

#print df