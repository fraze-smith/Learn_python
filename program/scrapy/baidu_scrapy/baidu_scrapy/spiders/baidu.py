import scrapy

class baidu_scrapy(scrapy.Spider):
    name = 'baidu_html'
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        with open('baidu.html','w',encoding='utf') as f:
            f.write(response.body.decode('utf-8'))
