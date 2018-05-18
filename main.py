#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:00:48 2018

@author: aayushsharma
"""

from bs4 import BeautifulSoup
import urllib.request
from dateutil import parser
from selenium import webdriver
import csv
import company_classifier

class AppURLOpener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener=AppURLOpener()

#adding incognito
option = webdriver.ChromeOptions()
option.add_argument("--incognito")



def getCompanyList(): #function to return a list of dictionary of companies
    # opening an instance of browser
    driver = webdriver.Chrome(executable_path='/Users/aayushsharma/python/voterlist/chromedriver',
                              chrome_options=option)
    driver.get("http://www.nepalstock.com.np/company/")
    element = driver.find_element_by_xpath("//select[@name='_limit']")
    element.send_keys("500")
    button = driver.find_element_by_xpath("//input[@value='Filter']")
    button.click()
    company = driver.page_source
    company_list = {}
    soup = BeautifulSoup(company, 'lxml')
    table = soup.find('table', class_='my-table')
    data = table.find_all('tr')
    index = slice(2, len(data) - 1)
    data = data[index]
    company=[]
    for row in data:
        cols = row.find_all('td')
        rindex = slice(0, len(cols) - 1)
        cols = cols[rindex]
        cols = [x.text.strip() for x in cols]
        company_list["serial_no"] = cols[0]
        company_list["name"] = cols[2]
        company_list["symbol"] = cols[3]
        company_list["category"] = cols[4]
        company.append(company_list.copy())

    return company



all_companies=getCompanyList()

# a list f dictionary of all news
def getAllNews():
    news={}
    page_no = 1
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
        news_list=[]

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
                news['date']=parser.parse(date_div.text.strip()).strftime('%d/%m/%Y')
                news_div = soup2.find('div',class_='singleNewsParagraph')
                news['content']=news_div.text
                if(company_classifier.classifier(news['content'])):
                    news['newsof']=company_classifier.classifier(news['content'])
                else:
                    news['newsof']='NEPSE'
                news_list.append(news.copy())
        page_no+1
    return news_list

all_news=getAllNews()
print(all_news)

def write_news(news_list):
    fin_news = "fin_news.csv"
    csv = open(fin_news, "w")
    columnTitleRow = "date, link, headline, content, newsof \n"
    csv.write(columnTitleRow)
    for i in all_news:
            date=i['date']
            link = i['link']
            headline = i['headline']
            content = i['content']
            newsof = i['newsof']
            row=date+","+link+","+headline+","+content+","+newsof+"\n"
            csv.write(row)
    return ()

write_news(all_news)
print(all_news)