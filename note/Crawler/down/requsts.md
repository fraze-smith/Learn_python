# requsts模块
- 特点:
  - 更简洁
  - 封装性更好
  - 底层用urllib3
- 中文文档: [http://docs.python-requests.org/zh_CN/latest/]
## 常用函数:
- get():
  - 实例:
  - requests.get(url)
  - requests.requst("get",url) 可以带有headers和pramas参数
  - 返回<class 'requests.models.Response'>
- post():
  - 参数:
    - url
- 代理设置:
  - proxy也是个字典:
    ```
    proxies = {
      "http": "address_your",
      "https":"address_your"
    }
    requests.requsts("get",url,proxies=proxies)
    ```
  - 代理验证:
    - 当购买代理时,可能需要输入用户名和密码
    - 使用```proxies = {"http": "usrname:passwd@adress:post"}```
  - web验证:
    - 在get中添加auth=(usrnanme,passwd)
- cookies:
  - request可以自动处理cookie信息
  - 可以使用```cookiejar = req.cookie()```获取
  - 也可以将cookisjar转化为字典```cookjar_dir =requsts.utils.dict_from_cookiejar(cookiejar)```
- session:
  - 模拟一次会话,从游览器发出请求开始,到接受应答结束.
  - session是一个实例,可以保存某些参数,比如在同一个session发出的请求都使用同一个cookie
  - 可以通过```ss = requests.session()```创建一个session对象
  - 然后通过ss.post(url,headers=headers,data=data)发起请求
  - 在进行请求时,就不需要进行模仿游览器了,所有的信息都保存在ss中了
  - 发起请求: ```rsp = ss.get(url)```
- ssl证书:
  - get中的参数verify默认是Ture
  - 如果将其关闭(False)则不需要验证
