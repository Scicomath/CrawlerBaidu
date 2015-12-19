#!/usr/bin/env python
#coding=utf-8

import optparse
import urllib
import urllib2
import re
from bs4 import BeautifulSoup as BS

def main():
    p = optparse.OptionParser()
    p.add_option('--keyword','-k',default="宜昌")
    p.add_option('--startPage','-s',default=1)
    p.add_option('--endPage','-e',default=5)
    p.add_option('--fileName','-f',default="result.txt")
    p.add_option('--writeMode','-m',default="w")
    options, arguments = p.parse_args()

    baseUrl = 'http://www.baidu.com/s'
    page = 1 #第几页
    #word = '穿戴设备'  #搜索关键词
    file = open(options.fileName,options.writeMode)

    for page in range(options.startPage,options.endPage+1):
        data = {'wd':options.keyword,'pn':str(page-1)+'0','tn':'baidurt','ie':'utf-8','bsst':'1'}
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
    
#search('宜昌',1,3,u'yichang.txt','w')
if __name__=='__main__':
    main()
