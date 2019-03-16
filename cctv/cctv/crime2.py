

import pandas as pd
import numpy as np
import googlemaps
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
import folium

#crime= pd.read_excel('./Crime.xls', thousands=',', encoding='utf-8') #, header=2, usecols='B,D,G,J,N')
crime_anal_police = pd.read_csv('./crime_in_Seoul_include_gu_name.csv', thousands=',', encoding='utf-8')
crime_anal_police#.head()


crime_anal_raw = pd.read_csv('./crime_in_Seoul_include_gu_name.csv', thousands=',', encoding='utf-8')

crime_anal = pd.pivot_table(crime_anal_raw, index='구별', aggfunc=np.sum)
"""
aggfunc은 numpy의 평균값을 리턴
"""
crime_anal#.head()

police = crime_anal
police['강간검거율'] = police['강간 검거'] / police['강간 발생'] * 100
police['강도검거율'] = police['강도 검거'] / police['강도 발생'] * 100
police['살인검거율'] = police['살인 검거'] / police['살인 발생'] * 100
police['절도검거율'] = police['절도 검거'] / police['절도 발생'] * 100
police['폭력검거율'] = police['폭력 검거'] / police['폭력 발생'] * 100

del police['강간 검거']
del police['강도 검거']
del police['살인 검거']
del police['절도 검거']
del police['폭력 검거']

con_list = ['강간검거율',
             '강도검거율',
             '살인검거율',
             '절도검거율',
             '폭력검거율']
con_list
for i in con_list:
     police.loc[police[i] > 100, i] = 100
police

police.rename(columns = {'강간 발생':'강간',
                         '강도 발생':'강도',
                         '살인 발생':'살인',
                         '절도 발생':'절도',
                         '폭력 발생':'폭력'
                         }, inplace=True)
police

col = ['강간',
             '강도',
             '살인',
             '절도',
             '폭력']
x = police[col].values
x
min_max_scalar = preprocessing.MinMaxScaler()

x_scared = min_max_scalar.fit_transform(x.astype(float))
police_norm = pd.DataFrame(x_scared, columns=col, index=police.index)

col2 = ['강간검거율',
             '강도검거율',
             '살인검거율',
             '절도검거율',
             '폭력검거율']
police_norm[col2] = police[col2]
police_norm

data_result = pd.read_csv('./data_result.csv', encoding='utf-8',index_col='구별')
data_result

police_norm[['인구수','CCTV']] = data_result[['인구수','소계']]
police_norm['범죄'] = np.sum(police_norm[col], axis=1)
police_norm['검거'] = np.sum(police_norm[col2], axis=1)
police_norm
police_norm.columns

from matplotlib import rc, font_manager
font = 'c:/windows/fonts/H2GTRM.ttf'
font_name = font_manager.FontProperties(fname=font).get_name()
font_name
rc('font', family=font_name)

sns.pairplot(police_norm,
             vars = ['강도','살인','폭력'],
             kind = 'reg',
             height = 3
             )
plt.show()

sns.pairplot(police_norm,
             x_vars = ['인구수','CCTV'],
             y_vars = ['살인','강도'],
             kind = 'reg',
             height = 3
             )
plt.show()

sns.pairplot(police_norm,
             x_vars = ['인구수','CCTV'],
             y_vars = ['살인검거율','폭력검거율'],
             kind = 'reg',
             height = 3
             )
plt.show()

tmp_max = police_norm['검거'].max()
police_norm['검거'] = police_norm['검거']/tmp_max * 100
police_norm_sort = police_norm.sort_values(by='검거', ascending=False)
police_norm_sort

target_col = col2
police_norm_sort = police_norm.sort_values(by='검거', ascending=False)
plt.figure(figsize=(10,10))
sns.heatmap(police_norm_sort[target_col], annot=True,fmt='f', linewidths=5)
plt.title("범죄 검거 비율(정규화된 검거의 합의 정렬)")
plt.show()

target_col = ['강간','강도', '살인', '절도', '폭력','범죄'] 
police_norm['범죄'] = police_norm['범죄'] / 5
police_norm_sort = police_norm.sort_values(by='범죄', ascending=False)
plt.figure(figsize=(10,10))
sns.heatmap(police_norm_sort[target_col], annot=True,fmt='f', linewidths=5)
plt.title("범죄 비율(정규화된 검거의 합의 정렬)")
plt.show()


police_norm.to_csv('./crime_in_Seoul_include_)