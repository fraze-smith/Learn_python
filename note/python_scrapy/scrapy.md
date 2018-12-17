# scrapy学习
 - 爬虫框架(frame)
 - 著名框架:
   - pyspider
   - scrapy
   - crawley
- [官方文档](https://docs.scrapy.org/en/latest/)
- [中文文档](https://scrapy-chs.readthedocs.io/zh_CN/0.24/)
- 安装```pip3 install Scrapy``` 
# 常用模块介绍:
- ScrapyEngine: 框架的大脑
- Schaduler调度器: 处理由大脑发出的request
- Downloader下载器: 下载response回来的地址
- Spider爬虫: 处理下载器下载的数据
-  Itempipeline管道: 详细处理Item
- DownloaderMiddlewares下载中间件 : 自定义下载组件
- SpiderMiddlewares 爬虫中间件: 自定义爬虫组件
- ![原理图](scrapy_architecture.png)原理图

# 工作流程:
- 新建工程: scrapy startproject project_name
- 明确目标与产出: 编写item.py
- 制作爬虫: 地址 spider/xxspider.py
- 储存内容: piplines.py


# ITemPipeline
- 对应pipeline文件
- 爬虫爬取出输出存入item后, item中保存的数据需要进一步处理,
比如说清洗,去重,储存
- pipeline需要处理process_item函数
    - spider提取出来的item作为参数穿入, 同时传入spider
    - 返回一个Item对象,被丢弃的item不会被之后的pipeline处理
    - 这个方法一定要实现
- __init__: 初始化参数
- open_spider(spider): 
    - 当spider对象开启时被调用
- close_spider(spoder):
    - 当spider对象被关闭时调用
# Spider
- 对应文件夹spiders下的文件
- __init__:初始化爬虫名称,start_urls列表
- start_requests: 生成requests对象交给Scrapy下载返回rsp
- parse: 根据返回的rsp解析出响应的item,item自动进入pipeline;
如果需要,解析出url,url自动交给requests模块,进行循环
- start_request(self)只能被调用一次,读取start_urls内容,并启动循环
- name: 设置爬虫名称
- start_urls: 设置第一批爬取的url
- allow_domains: 允许爬取的域名列表
- log: 日志