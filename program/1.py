from requests_html import HTMLSession
ss = HTMLSession()
rsp = ss.get('https://www.baidu.com')
for link in rsp.html.links():
    print(link)
rsp.html.absolute_links
