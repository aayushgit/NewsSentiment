#!/usr/bin/env python3
#-*- coding: utf-8 -*-
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
import news_scraper

news_list = []


class AppURLOpener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


opener = AppURLOpener()

# adding incognito
option = webdriver.ChromeOptions()
option.add_argument("--incognito")


def getCompanyList():  # function to return a list of dictionary of companies
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
    company = []
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

