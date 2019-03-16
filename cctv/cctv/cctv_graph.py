
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
import platform

font = 'c:/windows/fonts/H2GTRM.ttf'
font_name = font_manager.FontProperties(fname=font).get_name()
font_name
rc('font', family=font_name)

import pandas as pd
data_result = pd.read_csv('./data_result.csv', encoding='utf-8')
data_result

data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
#data_result['CCTV비율'].sort_values().plot(
#    kind = 'density',
#    grid = True,
#    figsize = (10,10),
#    title = '인구수와 CCtv의 관계'
#    )
#plt.show() #가로막대

#data_result['CCTV비율'].sort_values().plot(
#    kind = 'barh',
#    grid = True,
#    figsize = (10,10),
#    title = '인구수와 CCtv의 관계'
#    )
#plt.show() #가로막대

#plt.figure(figsize = (20,20))
#plt.scatter(data_result['인구수'],data_result['소계'],s=50) #산점도
#plt.xlabel('인구수')
#plt.ylabel('CCTV')
#plt.grid()
#plt.show()

import numpy as np
fp1 = np.polyfit(
    data_result['인구수'],
    data_result['소계'],
    1
    ) #직선 그리기
fp1
fy = np.poly1d(fp1) #Y축
fx = np.linspace(100000, 700000,100)

#plt.figure(figsize = (20,20))
#plt.scatter(data_result['인구수'],data_result['소계'],s=50) #산점도
#plt.plot(fx, fy(fx), ls='dashed', lw=3, color='g')
#plt.xlabel('인구수')
#plt.ylabel('CCTV')
#plt.grid()
#plt.show()


data_result['오차'] = np.abs(data_result['소계'] - fy(data_result['인구수']))
df_sort = data_result.sort_values(by='오차', ascending=False)
df_sort

plt.figure(figsize = (14,10))
plt.scatter(data_result['인구수'],data_result['소계'],c=data_result['오차'],s=50) #산점도
plt.plot(fx, fy(fx), ls='dashed', lw=3, color='r')
for i in range(10):
    plt.text(df_sort['인구수'][i] * 1.02, 
             df_sort['소계'][i] * 0.098,
             df_sort.index[i],
             fontsize = 15
             )
plt.xlabel('인구수')
plt.ylabel('인구당비율')
plt.grid()
plt.show()