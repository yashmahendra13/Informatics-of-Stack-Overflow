# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:34:21 2018

@author: yash1
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
def scrapeSO(max_pages):
    p=1
    #df = pd.DataFrame()
    scrape = []
    while p <= max_pages:   
        #scrape=[]
        page_url="https://stackoverflow.com/questions/tagged/python?page="+str(p)+"&sort=newest&pagesize=15" #storing variable
        page = requests.get(page_url) #request connection
        soup = BeautifulSoup(page.content, 'html.parser') #initiating beautifulsoup object using the html source and Python’s html.parser
        divs=soup.find_all("div",{"class":"question-summary"}) #finding div and storing in variable divs
    
        for idx, div in enumerate(divs):
            quesid=None
            votes=None
            acount=None
            views=None
            question=None
            desc=None
            tags=None
            udetail=None
            repscore=None
            bgold=None
            bsilver=None
            bbronze=None
            
            qid=div.select("a.question-hyperlink")
            if qid!=[]:
                quesid=qid[0].get('href')[11:19]
            
            v=div.select("div.votes")
            if v!=[]:
                votes=v[0].get_text()

            ac=div.select("div.status.answered")
            if ac!=[]:
                acount=ac[0].get_text()

            vi=div.select("div.views")
            if vi!=[]:
                views=vi[0].get_text()

            q=div.select("a.question-hyperlink")
            if q!=[]:
                question=q[0].get_text()

            d=div.select("div.excerpt")
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

            t=div.select("div.tags")
            if t!=[]:
                tags=t[0].get_text()

            scrape.append((quesid,votes,acount,views,question,desc,udetail,repscore,bgold,bsilver,bbronze,tags)) #appending values
            #print(scrape)
        df = pd.DataFrame(scrape)
        p+=1
        #print(p)
    return df

if __name__ == "__main__": 
    a=pd.DataFrame()
    a=scrapeSO(1)

    writer = ExcelWriter('Stack_Overflow_Questions_Data.xlsx')
    a.to_excel(writer,'Sheet1')
    writer.save()