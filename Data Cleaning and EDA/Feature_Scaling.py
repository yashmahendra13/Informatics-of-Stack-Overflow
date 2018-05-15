

#Standardizing Data


import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('Stack_Overflow_Questions_Clean_EDA_Data.xlsx')


df.head()
df.shape
df.columns

scaled_data = pd.DataFrame()


scaled_data = df[['Votes', 'Answer Count', 'Views','Reputation Score', 'Gold Badge Count',
       'Silver Badge Count', 'Bronze Badge Count','QDescription length']]


scaled_data.head()


#Feature Scaling


scaler = StandardScaler()

#Fit scaler to the features.
scaler.fit(scaled_data)

#Use the .transform() method to transform the features to a scaled version.
scaled_features = scaler.transform(scaled_data)

df_feat = pd.DataFrame(scaled_features)
df_feat.head()

df_feat.columns = ['Votes','Answer Count','Views','Reputation Score','Gold Badge Count','Silver Badge Count','Bronze Badge Count','QDescription length']

df_feat.head()



#Let's Add rest of the coulumns to the primary data
df['Votes'] = df_feat['Votes']
df['Answer Count'] = df_feat['Answer Count']
df['Views'] = df_feat['Views']
df['Reputation Score'] = df_feat['Reputation Score']
df['Gold Badge Count'] = df_feat['Gold Badge Count']
df['Silver Badge Count'] = df_feat['Silver Badge Count']
df['Bronze Badge Count'] = df_feat['Bronze Badge Count']
df['QDescription length'] = df_feat['QDescription length']

df.head()



from pandas import ExcelWriter

writer = ExcelWriter('Stack_Overflow_Questions_Feature_Scaled_Data.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()




