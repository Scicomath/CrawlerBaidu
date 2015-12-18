#coding=utf-8

import urllib
import urllib2
import re
from bs4 import BeautifulSoup as BS

def search(word, startPageNum, endPageNum, fileName, writeMode):
    baseUrl = 'http://www.baidu.com/s'
    page = 1 #第几页
    #word = '穿戴设备'  #搜索关键词
    file = open(fileName,writeMode)

    for page in range(startPageNum,endPageNum+1):
        data = {'wd':word,'pn':str(page-1)+'0','tn':'baidurt','ie':'utf-8','bsst':'1'}
        data = urllib.urlencode(data)
        url = baseUrl+'?'+data

        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
        except urllib2.HttpError,e:
            print e.code
            exit(0)
        except urllib2.URLError,e:
            print e.reason
            exit(0)

        html = response.read()
        soup = BS(html)
        td = soup.find_all(class_='f')

        for t in td:
            titleStr = t.h3.a.get_text()+u'\n'
            file.write(titleStr.encode('GBK'))
    
search('宜昌',1,3,u'yichang.txt','w')
