#coding = utf-8

import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

data = pd.read_csv('all_user_yongdian_data_2015.csv')
train = pd.read_csv('train.csv', names = ['CONS_NO', 'CHK_STATE'])

data = pd.merge(data, train, on = 'CONS_NO', how = 'left')
data['DATA_DATE'] = pd.to_datetime(data['DATA_DATE'])
data = data.dropna().sort_values(['CHK_STATE', 'CONS_NO', 'DATA_DATE'])

data_bad = data[data['CHK_STATE']==1]
data_good = data[data['CHK_STATE']==0]

'''
#using the steel power data to draw the power-use map 
data_bad = data_bad.set_index(data_bad['CONS_NO'])

for custum in data_bad.index.unique():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(data_bad['DATA_DATE'].loc[custum], data_bad['KWH'].loc[custum], 'ko--')
    plt.savefig('%d.png' % custum, dpi = 400, bbox_inches='tight')
    plt.close()


#using the good guys data to draw some map
data_good = data_good.set_index(data_good['CONS_NO'])

for custum in data_good.index.unique():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(data_good['DATA_DATE'].loc[custum], data_good['KWH'].loc[custum], 'ko--')
    plt.savefig('%d.png' % custum, dpi = 400, bbox_inches='tight')
    plt.close()

'''

#abnormal check
data_bad_check = data_bad.reset_index().drop(['index','CONS_NO','DATA_DATE','KWH_READING','KWH_READING1','CHK_STATE'],axis=1)
data_good_check = data_good.reset_index().drop(['index','CONS_NO','DATA_DATE','KWH_READING','KWH_READING1','CHK_STATE'],axis=1)


