#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 20:57:10 2018

@author: aayushsharma
"""
import re
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#adding incognito
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

#opening an instance of browser
driver = webdriver.Chrome(executable_path='/Users/aayushsharma/python/voterlist/chromedriver',chrome_options=option)
driver.get("http://www.nepalstock.com.np/company/")
element = driver.find_element_by_xpath("//select[@name='_limit']")
element.send_keys("500")
button = driver.find_element_by_xpath("//input[@value='Filter']")
button.click()
company=driver.page_source

# class AppURLOpener(urllib.request.FancyURLopener):
#     version = "Mozilla/5.0"
#
# opener=AppURLOpener()
# uClient=opener.open(company)
# cpage=uClient.read()
# uClient.close()
company_list={}
# name_list=[]
# ab_list=[]
soup=BeautifulSoup(company,'lxml')
table =  soup.find('table',class_='my-table')
data=table.find_all('tr')
index=slice(2,len(data)-1)
data=data[index]
company=[]

for row in data:
    cols=row.find_all('td')
    rindex=slice(0,len(cols)-1)
    cols=cols[rindex]
    cols=[x.text.strip() for x in cols]
    company_list["serial_no"]=cols[0]
    company_list["name"] = cols[2]
    company_list["symbol"] = cols[3]
    company_list["category"] = cols[4]
    company.append(company_list.copy())
    print(company_list)

    # name_list.append(company_list["name"])
    # ab_list.append(company_list["symbol"])

#Creating and Replacing code for Company Classification
#
# for i,j in zip(name_list,ab_list):
#     i = re.sub(r"[^\w\s]", '', i)
#     i = re.sub(r"\s+", '\\s', i)
#     print("""
#     #Regular Expression for %s
#     %s = re.compile(r'(%s)|(%s)')
#         if %s.search(news):
#         return('%s')
#         """%(j,j,i,j,j,j))











