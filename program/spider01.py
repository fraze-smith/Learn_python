from urllib import request

url = "http://www.baidu.com"
resp = request.urlopen(url)
html = resp.read().decode()
with open('baidu.html',"w") as f:
    f.write(html)
