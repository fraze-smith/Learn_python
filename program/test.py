import requests
url = "http://www.baidu.com"

html = requests.get(url)
print(type(html))
print(html.text)
import time
