from bs4 import BeautifulSoup as bs
import requests
url = "http://www.baidu.com"
rsp = requests.get(url)
html = rsp.text
soup = bs(html)
print(soup)