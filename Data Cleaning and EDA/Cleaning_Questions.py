import pandas as pd
import numpy as np
from pandas import ExcelWriter

a = pd.read_excel('Stack_Overflow_Questions_Data.xlsx')

a.columns = ['Question Id','Votes','Answer Count','Views','Question','QDescription','User','Reputation Score','Gold Badge Count','Silver Badge Count','Bronze Badge Count','Tags']

a["Votes"]=a["Votes"].apply(lambda x:x.strip())

a["Views"]=a["Views"].apply(lambda x:x.strip())
a["QDescription"]=a["QDescription"].apply(lambda x:x.strip())
a["Tags"]=a["Tags"].apply(lambda x:x.strip())

a["Views"]=a["Views"].apply(lambda x:x.replace("views",""))

a["Votes"]=a["Votes"].apply(lambda x:x.replace("\nvotes",""))

a["Votes"]=a["Votes"].apply(lambda x:x.replace("\nvote",""))

a['Answer Count'] = a['Answer Count'].astype(str)
a["Answer Count"]=a["Answer Count"].apply(lambda x:x.replace("\n",""))
a["Answer Count"]=a["Answer Count"].apply(lambda x:x.replace("answer\r",""))
a["Answer Count"]=a["Answer Count"].apply(lambda x:x.replace("answers\r",""))

a['Answer Count'] = a['Answer Count'].astype('float64')

a["Views"]=a["Views"].apply(lambda x:x.replace("k","000"))
a['Views'] = a['Views'].astype('float64')

a['Reputation Score'] = a['Reputation Score'].astype(str)
a["Reputation Score"]=a["Reputation Score"].apply(lambda x:x.replace(",",""))

a['Reputation Score'] = (a['Reputation Score'].replace(r'[k]+$', '', regex=True).astype(float) *           a['Reputation Score'].str.extract(r'[\d\.]+([k]+)', expand=False)
            .fillna(1)
            .replace(['k'], [10**3]).astype(int))

a['Votes'] = a['Votes'].astype('float64')

writer = ExcelWriter('Stack_Overflow_Questions_Clean_Data.xlsx')
a.to_excel(writer,'Sheet1')
writer.save()




