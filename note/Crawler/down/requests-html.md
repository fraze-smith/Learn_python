# request-html 学习文档 未完待续---
*其实只用到了HTMLSession模块*

1. 导入
    ```from requests_html import HTMLSession```
2. 首先实例化一个对象
    - ```ss = HTMLSession()```
    - ss 可以理解为一个游览器(就当是吧).
3. get()
    - ```rsp = ss.get('https://www.baidu.com')```
    - rsp可以当成一个标签页.现在我们就打开了一个标签页.
4. 对网页进行操作
    1. 获取网页内容
    
        ```html = rsp.html.html```
        第一个html是说操作对象是html,第二个html是说获取html
        
        或者```text = rsp.text```
        获取rsp的文本,不过好像需要解码.
    2. 获取网页链接   
     ```links = rsp.html.links```
     以列表形式返回页面的所有链接,可以用循环规整输出.
     如果要返回绝对链接可以使用
      ```rsp.html.absolute_links```
     绝对链接总共定义了文档的位置，包括获取文档所需的协议，从中获取文档的服务器，它所在的目录以及文档本身的名称。
     
       ***简单点说就是跟当前目录树没关系,在哪打开都一样***
    3. css选择器    
    不展开讲了,不懂先可以看看[十分钟搞懂css选择器](https://www.cnblogs.com/dolphinX/p/3347713.html).
    ```lg = rsp.html.find('body .s_form_warapper #lg',frist=ture)```
    选中body标签下的s_form_warapper类下的id=lg中间用空格隔开.  
    first选项的意思是只选中第一个,默认返回一个列表.
        - 符号含义:
            - \#  id
            - . 类
            - 输入标签名 直接选择标签  
           ```attr = lg.attr```返回lg的所有属性,类型为字典.  
    4. render方法
    当页面使用大量js渲染时,返回结果只是一些js,这是用浏览器直接打开更为方便.