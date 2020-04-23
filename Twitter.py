from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import urllib.request
import datetime
import re

time1 = datetime.date(2018, 1, 1)
x=0
value = '麻倉もも'

while x < 5000:
    time2 = time1-datetime.timedelta(days=1)    #时间

    print('正在爬取：'+str((time2))+'—'+str(time1)+'的图片')
    #带入浏览器数据
    # browser = webdriver.ChromeOptions()
    browser = webdriver.Chrome()
    # browser.add_argument(r"user-data-dir=C:\Users\mocho\AppData\Local\Google\Chrome\User Data")
    # browser = webdriver.Chrome("chromedriver",0,browser)
    url = 'https://twitter.com/search?f=images&vertical=default&q=' + value + 'since%3A'+str(time2)+'%20until%3A'+str(time1)+'&src=typed'
    browser.get(url)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    #下拉到最底端
    elements = []
    img_list = []
    count = -1
    time.sleep(0.5)
    while len(elements)>count:  #判断是否到底
        count = len(elements)
        changdu_list=[]
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(0.8)
        htmlss = BeautifulSoup(browser.page_source,'html.parser')
        for htmls in htmlss.find_all("img"):  #遍历寻找img
            img = htmls.get('src')
            changdu_list.append(img)
        elements = changdu_list
    html = browser.page_source  #源码
    browser.close()       #关闭浏览器
    html = BeautifulSoup(html,'html.parser')
    for htmls in html.find_all("img"):  #遍历寻找img
        img = htmls.get('src')
        img_list.append(img)
    img_list = img_list[1:-1]
    print('共：'+str(len(img_list))+' 张')
    print(str(img_list))
    # 下载
    for img_lists in img_list:
        x = x+1
        try:
            print('正在下载第', x, '张')
            urllib.request.urlretrieve(img_lists, 'C:\py3\mocho\{}.jpg'.format(x))
        except:
            print("超时")
            x = x-1
            pass

    time1 = time1 - datetime.timedelta(days=1)