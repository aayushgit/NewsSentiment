#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:00:48 2018

@author: aayushsharma
"""

from bs4 import BeautifulSoup
import urllib.request
import company_classifier
def scrape_news():
    class AppURLOpener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"

    opener=AppURLOpener()
    news={}
    page_no=1
    news_list=[]
    #news page
    while page_no<=3:
        news_page='http://archive.sharesansar.com/category/latest/page/'+str(page_no)+'/'
        uClient=opener.open(news_page)
        #HTML Contents
        page_html = uClient.read()
        #close connection
        uClient.close()

        soup=BeautifulSoup(page_html,'lxml')

        #classify news according to company

        for article in soup.find_all('div',class_='media-body'):
            headline = article.h4.text
            news['headline']=headline
            for link_get in article.find_all('a',href=True):
                link=link_get.get('href')
                news['link']=link
                uPage=opener.open(link)
                uhtml=uPage.read()
                uPage.close()
                soup2=BeautifulSoup(uhtml,'lxml')
                date_div = soup2.find('span',class_='singleNewsPublishDate')
                news['date']=date_div.text.strip()
                news_div = soup2.find('div',class_='singleNewsParagraph')
                news['content']=news_div.text
                if (company_classifier.classifier(news['content'])):
                    news['newsof'] = company_classifier.classifier(news['content'])
                else:
                    news['newsof'] = 'NEPSE'
                news_list.append(news.copy())
                # print(news)
        print("Getting News at page" + str(page_no))
        page_no=page_no+1
    return(news_list)

print(scrape_news())