# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:10:56 2018

@author: yash1
"""

import pandas as pd
from pandas import ExcelWriter

a = pd.read_excel('Stack_Overflow_Answers_Data.xlsx')

a.columns = ['Question Id','Answer','User','Reputation Score','Gold Badge Count','Silver Badge Count','Bronze Badge Count']

a['Reputation Score'] = a['Reputation Score'].astype(str)
a["Reputation Score"]=a["Reputation Score"].apply(lambda x:x.replace(",",""))

a['Reputation Score'] = (a['Reputation Score'].replace(r'[k]+$', '', regex=True).astype(float) *           a['Reputation Score'].str.extract(r'[\d\.]+([k]+)', expand=False)
            .fillna(1)
            .replace(['k'], [10**3]).astype(int))

writer = ExcelWriter('Stack_Overflow_Answers_Clean_Data.xlsx')
a.to_excel(writer,'Sheet1')
writer.save()