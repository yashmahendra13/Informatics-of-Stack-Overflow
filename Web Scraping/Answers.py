# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:44:28 2018

@author: yash1
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from numpy import *
from pandas import ExcelWriter
def answers():
    c = pd.read_excel('Stack_Overflow_Questions_Clean_Data.xlsx')
    s=[]
    df = pd.DataFrame()
    df = c[pd.notnull(c['Answer Count'])]
    a = np.array(df['Question Id'])
    #print(df)
    for i in range(200):
        #print(a[i])
        url = 'https://stackoverflow.com/questions/'+str(a[i])+'/'
        #print(url)
        #s=[]
        page = requests.get(url) #request connection
        soup = BeautifulSoup(page.content, 'html.parser') #initiating beautifulsoup object using the html source and Python’s html.parser
        divs=soup.find_all("div",{"class":"answer"}) #finding div and storing in variable divs
        for idx, div in enumerate(divs):
            qid=None
            desc=None
            udetail=None
            repscore=None
            bgold=None
            bsilver=None
            bbronze=None
            
            qid=a[i]
            
            d=div.select("div.post-text p")
            if d!=[]:
                desc=d[0].get_text()
        
            ud=div.select("div.user-details a")
            if ud!=[]:
                udetail=ud[0].get_text()

            rs=div.select("span.reputation-score")
            if rs!=[]:
                repscore=rs[0].get_text()

            bg=div.select("span.badge1")
            if bg!=[]:
                bgc=div.select("span.badgecount")
                bgold=bgc[0].get_text()

            bs=div.select("span.badge2")
            if bs!=[]:
                bsc=div.select("span.badgecount")
                bsilver=bsc[0].get_text()

            bb=div.select("span.badge3")
            if bb!=[]:
                bbc=div.select("span.badgecount")
                bbronze=bbc[0].get_text()
        
            s.append((qid,desc,udetail,repscore,bgold,bsilver,bbronze)) #appending values
        #print(s)
        df1=pd.DataFrame(s)
        #print(df1)
    return df1

if __name__ == "__main__": 
    a=pd.DataFrame()
    a=answers()

    writer = ExcelWriter('Stack_Overflow_Answers_Data.xlsx')
    a.to_excel(writer,'Sheet1')
    writer.save()