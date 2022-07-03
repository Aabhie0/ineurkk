#!/usr/bin/env python


from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\lenovo\Documents\Datasets\enereffici\Dataset\Scaling.csv")
df.head()

df.drop(['Unnamed: 0'],axis=1,inplace=True)


df.head()


scaling_feature =[feature for feature in df.columns if feature not in ['cooling load','heating load']]
df[scaling_feature].head()



scaler = MinMaxScaler()
data = scaler.fit_transform(df[scaling_feature])
data

data.shape

VIF = pd.DataFrame()
VIF['vif'] = [variance_inflation_factor (data,i) for i in range(data.shape[1])]
VIF['feature'] = df[scaling_feature].columns
VIF


pca=PCA()
data2=pca.fit_transform(data)
data2


data2.shape


VIF = pd.DataFrame()
VIF['vif'] = [variance_inflation_factor (data2,i) for i in range(data2.shape[1])]
VIF['feature'] = df[scaling_feature].columns
VIF

one = df[['heating load','cooling load']]

two = pd.DataFrame(data2,columns=df[scaling_feature].columns)



df_new = pd.concat([one,two],axis=1)
df_new.head()

#df_new.to_csv(r'C:\Users\lenovo\Documents\Datasets\enereffici\Model_Building.csv')


import pickle
file = 'Energy_Efficiency_pca.pkl'

pickle.dump(pca, open(file,'wb'))









