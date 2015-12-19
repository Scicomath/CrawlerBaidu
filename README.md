# CrawlerBaidu
简单爬虫爬出百度搜索结果页面

需要下载BeautifulSoup4

使用方法：
```
Usage: CrawlerBaidu.py [options]

Options:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword=KEYWORD
  -s STARTPAGE, --startPage=STARTPAGE
  -e ENDPAGE, --endPage=ENDPAGE
  -f FILENAME, --fileName=FILENAME
  -m WRITEMODE, --writeMode=WRITEMODE
```
例子：
```
python CrawlerBaidu.py -k 宜昌 -f yichang.txt -s 1 -e 5 -m w
```

