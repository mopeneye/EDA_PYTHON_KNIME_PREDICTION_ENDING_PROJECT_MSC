# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:45:38 2020

@author: MertAcikgoz
"""

import pandas as pd
import numpy as np

# ~3M satır datanın 500K bölümünü kullanmak için dataframe'e load ediyoruz
df2 = pd.DataFrame([])
for df in pd.read_csv('D:\\sehir_unv_ders_notlari\\bitirme_projesi\\data\\US_Accidents_Dec19.csv', iterator=True, chunksize=10000):
    df2 = df2.append(df)    
    if (df2.shape[0] >= 500000):
        break
print(df2.shape)

# knime için dataframei istediğimiz boyutta excellere export eden fonksiyon - ~6 dk. sürüyor   
def write_to_excel(df, size):
    i = 1
    start = 0
    end = size
    while (end < len(df)):
        print(start, end-1, i)
        df.iloc[start:end].to_excel(r'D:\\sehir_unv_ders_notlari\\bitirme_projesi\\data\\US_Accidents_Dec19_part'+str(i)+'.xlsx')
        start = end
        end += size
        i += 1
    end = len(df) 
    print(start, end, i)
    df.iloc[start:].to_excel(r'D:\\sehir_unv_ders_notlari\\bitirme_projesi\\data\\US_Accidents_Dec19_part'+str(i)+'.xlsx')
    
write_to_excel(df2, 50000)

df2.columns

states = df2.State.unique()

import seaborn as sns
import matplotlib.pyplot as plt

    
Severity_mapping = {1 : 'low', 2: 'low', 3: 'High', 
               4: 'High'}

df2['Severity_transformed'] = df2['Severity'].map(Severity_mapping)

df3 = df2[['Severity', 'Severity_transformed']].head(1000)

  
# mapping'in sağlaması'
df2.Severity_transformed.value_counts()
df2.Severity.value_counts()

df2.drop

df2.columns

df4 = df2.head(10)


