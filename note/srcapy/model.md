# 常用模块介绍:
- ScrapyEngine: 框架的大脑
- Schaduler调度器: 处理由大脑发出的request
- Downloader下载器: 下载response回来的地址
- Spider爬虫: 处理下载器下载的数据
- Itempipeline管道: 详细处理Item
- DownloaderMiddlewares下载中间件 : 自定义下载组件
- SpiderMiddlewares 爬虫中间件: 自定义爬虫组件
- ![原理图](scrapy_architecture.png)原理图
