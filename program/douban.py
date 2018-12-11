#_*_ coding= UTF-8 _*_
'''
page1: https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0
page2: https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=20
page3: https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=40
start标志开始数
'''
from urllib import request,parse
import json
import requests
url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0"

rsq = request.urlopen(url)
html = rsp.read().decode()
data = json.loads(html)
print(data)
    
