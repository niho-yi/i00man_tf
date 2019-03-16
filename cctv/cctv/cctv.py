


import pandas as pd
cctv = pd.read_csv('./cctv.csv', encoding='utf-8')
cctv.head()
cctv_meta = cctv.columns
cctv_meta

"""
Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')
"""

cctv.rename(columns={cctv.columns[0]:'구별'}, inplace=True)
#inplace = True
cctv.head()

#import xlrd
pop = pd.read_excel('./pop.xls', encoding='utf-8', header=2, usecols='B,D,G,J,N')
pop.head()

#DF - featuring
pop.rename(columns={
    pop.columns[0]:'구별',
    pop.columns[1]:'인구수',
    pop.columns[2]:'한국인',
    pop.columns[3]:'외국인',
    pop.columns[4]:'고령자'
    }, inplace=True)

pop.head()

import numpy as np
cctv.sort_values(by='소계', ascending=True).head(15)

#0번행 삭제
pop.drop([0], inplace=True)
pop.head()
pop['구별'].unique()
pop[pop['구별'].isnull()]

# 외국인비율과 고령자비율 계산
pop['외국인비율'] = pop['외국인']/pop['인구수']*100
pop['고령자비율'] = pop['고령자']/pop['인구수']*100
pop.head()
pop.sort_values(by='인구수', ascending=True)
data_result = pd.merge(cctv, pop, on='구별')
data_result.head()

# column : DROP
# row : del
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']

#그래프를 그리기 위해 구이름을 index로 설정
data_result.set_index('구별', inplace=True)
data_result.head()

# 상관관계
# - 상관계수 절대값이 0.1이하면 거의 무시
# - 상관계수 절대값이 0.3이하면 약한 상관관계
# - 상관계수 절대값이 0.5이하면 중립
# - 상관계수 절대값이 0.7이상이면 강한 상관관계
np.corrcoef(data_result['고령자비율'], data_result['소계'])
np.corrcoef(data_result['외국인비율'], data_result['소계'])
data_result.sort_values(by='인구수', ascending=True)
data_result.head(30)
data_result.to_csv('./data_result_2.csv')
data_result.head(30)











#import xlrd as xls1
##from . import book
#open_workbook_xls()
#dd = xls1.Book()
#dd.open_workbook_xls(

#        #filename=filename,
#        #logfile=logfile,
#        #verbosity=verbosity,
#        #use_mmap=use_mmap,
#        #file_contents=file_contents,
#        #encoding_override=encoding_override,
#        #formatting_info=formatting_info,
#        #on_demand=on_demand,
#        #ragged_rows=ragged_rows,
#    )