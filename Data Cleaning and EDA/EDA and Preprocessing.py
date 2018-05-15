
# coding: utf-8

#import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style('whitegrid')
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
#get_ipython().magic('matplotlib inline')

df = pd.DataFrame()

df = pd.read_excel('Stack_Overflow_Questions_Clean_Data.xlsx')

df.info()


df.columns


df.shape


df.head()


df.describe()

# Exercise 3.2. Find missing values

# determine which value is null
df.isnull()

df[df.isnull().any(axis=1)]

# get number of null values in each column
df.isnull().sum(axis=0)

#Let's carry out some Visualization to analyze missing data

sns.heatmap(df.isna())

#Let's replace NaN answercount values with 0

df['Answer Count'].fillna(0, inplace=True)


df.isnull().sum(axis=0)

df['Gold Badge Count'].fillna(0, inplace=True)

df['Silver Badge Count'].fillna(0, inplace=True)

df['Bronze Badge Count'].fillna(0, inplace=True)



df.isnull().sum(axis=0)


#Lets interpolate Reputation Score Values


df['Reputation Score'].describe()

type(df['Reputation Score'])


imp = Imputer(missing_values='NaN',strategy= 'median',axis=0)

imp=Imputer(missing_values="NaN", strategy="median",axis=0)
imp.fit(df[["Reputation Score"]])
df["Reputation Score"]=imp.transform(df[["Reputation Score"]]).ravel()

#Now our data is cleaned of missing values

#Now check for Duplicate Value


df[df.duplicated(['Question Id'], keep=False)]

print(len(df[df.duplicated(['Question Id'], keep=False)]))

#We have 60 duplicate values 

print(len(df[df.duplicated(['Question Id'], keep='first')]))

#And we can remove 30 of them

a = []

a = df.index[df.duplicated(['Question Id'], keep='first')]


print(len(a))

df.drop(df.index[a[:]],inplace=True)

df.index[df.duplicated(['Question Id'], keep='first')]

print(len(df[df.duplicated(['Question Id'], keep='first')]))

df.info()

#Now we have removed the duplicate values

#Exploratory Data Analysis to analyze data and remove outliers


sns.pairplot(df[1:])

sns.heatmap(df.corr(),cmap='coolwarm')
plt.title('df.corr()')

#By analyisis, 1) votes are correlated with views
# 2) Reputation Score is Correlated with the three badges
# 3) Each badge is highly correlated with other and vice versa


#Let's Analyze Individual Variables

sns.countplot(x='Votes',data=df)

sns.countplot(x='Answer Count',data=df)

sns.countplot(x='Views',data=df)

sns.jointplot(x='Reputation Score',y='Question Id',data=df)

#We can see Reputation Score has a outlier

df[df['Reputation Score'] > 250000]

df = df[df['Question Id'] != 48916579]

df[df['Reputation Score'] > 150000]


sns.jointplot(x='Reputation Score',y='Question Id',data=df)

#As votes increases, views also increase
sns.set_style('whitegrid')
sns.lmplot('Votes','Views',data=df,
           palette='coolwarm',size=6,aspect=1,fit_reg=False)


sns.jointplot(x='Votes',y='Answer Count',data=df)



sns.lmplot(x='Votes',y='Reputation Score',data=df,palette='coolwarm')

sns.jointplot(x='Votes',y='Views',data=df)


sns.lmplot(x='Views',y='Reputation Score',data=df,palette='coolwarm')


sns.jointplot(x='Answer Count',y='Reputation Score',data=df)

df[['Gold Badge Count', 'Silver Badge Count','Bronze Badge Count']].hist(figsize=(10, 10), bins=50);

sns.pairplot(data=df, x_vars=['Gold Badge Count', 'Silver Badge Count','Bronze Badge Count'],             y_vars=['Gold Badge Count', 'Silver Badge Count','Bronze Badge Count']);

#Exploratory Analysis on Text Columns


df['Question'].describe()


df['QDescription'].describe()

df['QDescription length'] = df['QDescription'].apply(len)
df.head()


df['QDescription length'].plot(bins=50, kind='hist') 


df['QDescription length'].describe()

#Explore tags

print(df['Tags'].unique())

print(df['Tags'].value_counts())

#Storing Data in Excel File

from pandas import ExcelWriter

writer = ExcelWriter('Stack_Overflow_Questions_Clean_EDA_Data.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()




