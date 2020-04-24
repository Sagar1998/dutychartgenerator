import pandas as pd
import warnings
import numpy as np
from numpy import *
from random import shuffle,randint
warnings.filterwarnings("ignore")
df=pd.read_csv("chart.csv")                  #read csv
df = df[df['X2'].notna()]
day=[]
rday=[]
data=[]
Sum=[]
Zero=[]
#print(len(df.columns)-4)                           #no of row's=123
#print(len(df) - 2)                                 #no of col's=52
day=[df.iloc[:,i+4] for i in range(0,len(df.columns)-4)]           #list of days from november-devembe
rday=[i[1] for i in day]                            #required no of faculty in list rday

for i in range (0,len(df.columns)-4):               #set's all values to NaN from list day
    day[i][2:]='NaN'
for i in range(0,len(df.columns)-4):
    if rday[i] is nan:
        rday[i]=0

for i in range(0,len(df.columns)-4):
    data.append([0] * (len(day[i][2:])-int(rday[i])-2) + [1] * int(rday[i]) + [0] * 1 + [0] * 1)                #no of faculty present
    shuffle(data[i])
    for j in range(0, len(df)-2):
        if data[i][j] is 0:
            data[i][j] = 0
    day[i][2:] = data[i]
#print(day)
#print(len(data))
for j in range(0,len(df)-2):
        Sum.append(sum(i[j] for i in data))                           #find sum of each rows aka find the requirments of each faculty

length=len(data[0])
for j,x in enumerate(data):
    while(True):
        index=randint(0,length-1)                                     # add E in the dataframe
        if x[index]==0:
            data[j][index]="E"
            break
        else:
            continue
for j,x in enumerate(data):
    while(True):
        index=randint(0,length-1)                                   # add R in dataframe
        if x[index]==0:
            data[j][index]="R"
            break
        else:
            continue

for i in range (0,len(df.columns)-4):                               #replace all values
    day[i][2:] = data[i]

for i in range(0,len(df.columns)-4):
    for j in range(0, len(df)-2):
        if data[i][j] is 0:                                         #replace 0 with nan values
            data[i][j] = nan

for i in range(0,len(df.columns)-4):
    day[i][2:] = data[i]
#print(day)
df['X4'][2:]=Sum                                                   #replace sum of all row's
#print(day)
#print(df)
df.to_csv('allotclass.csv')              #print final csv name final1234.csv
print("done check your new csv and now put the csv in your r project and run it!!....")