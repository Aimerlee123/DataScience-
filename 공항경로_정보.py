# -*- coding: utf-8 -*-
"""공항경로 정보.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17NLKR0C29rPJr_2sC0hqmUrWSveQPQI6
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df2=pd.read_csv('/content/drive/MyDrive/datasience/airports.dat',header=None,encoding='UTF-8')

df3=pd.read_csv('/content/drive/MyDrive/datasience/routes.dat',header=None,encoding='UTF-8')

df2n=df2[[0,6,7]]  #id,lat,long
df3n=df3[[3,5]]  #source 공항 destination 공항 
df2n.head(3).append(df2n.tail(3))

df2n.dtypes,df2n.shape

df3n.head(10)

df3n.dtypes,df3n.shape

df2n.isna().sum().sum(),df3n.isna().sum().sum() #no missing values

df3n[3].values  #모든 정보가 stirng 형태인 것을 확인

sum([i.isnumeric() for i in df3n[3].values]) #들어 있는 값중 정수로 숫자로 바뀔 수 있는 것 확인

df3n.shape #220개가 숫자 아닌 개 있는 것을 확인할 수 있다. 이것을 걸러내야 한다.

df2n=df2n.set_index(0) #공항 id를 index로 사용
df2n

from geopy.distance import great_circle,geodesic

distances=[]

for i in range(df3n.shape[0]):
  src=df3n.iloc[i][3]
  dst=df3n.iloc[i][5]
  if (not src.isnumeric()) or (not dst.isnumeric()):  #숫자로 바뀌지 않는 경우 제외 
    continue


  src, dst= int(src),int(dst)

  if src in df2n.index and dst in df2n.index:
    src_lat, src_long= df2n.loc[src][6],df2n.loc[src][7]
    dst_lat, dst_long= df2n.loc[dst][6],df2n.loc[dst][7]
    dist=great_circle((src_lat,src_long),(dst_lat,dst_long)).km
    distances.append(dist)

len(distances),sum(distances)/len(distances)

plt.hist(distances,bins=100,facecolor='b')
plt.xlabel('Distances (km)')
plt.ylabel('Number of flights')

df2n.iloc[0][6]