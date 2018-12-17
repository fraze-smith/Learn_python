# request详解
- construction:
  - reuqest:
    - get:(一下为参数)
      - url
      - params(url参数)
        需要字典传值,params将自动对字典进行编码
      - headers 需要以字典传入请求头,在能判断内容长度的情况下，header 的 Content-Length 会被自动
        改写
        注意:所有的 header 值必须是 string、bytestring 或者 unicode.尽管传递 unicode header 也是允许的，但不建议这样做.
      - timeout 指定等待时间,单位为秒,如果超出时间将会停止请求.
    - post:(以下为参数)
      - url
      - data 传入字典或元组格式的表单 data也可以读入文件,但应该以二进制格式打开,以免出错.
      - headers
  - reuqests的实例
    - url 返回请求的url requests将对http请求进行重定向到https
    - text 输出实例的文本
    - encoding 输出实例的编码, 也可以自行制定
    - content 以字节形式访问实例
    - json() 对实例进行json解码,如果失败将会抛出ValueError: No JSON object could be decoded
    - cookies[cookis_name] 查看实例的cookie
      - cookies的返回对象为cookiesJar对象
      - 可以通过jar = requests.cookies.RequestsCookieJar()将cookie作为一个实例,在
        再次请求时传入cookies
    - status_code 查看请求的响应态
      - 为方便引用，Requests还附带了一个内置的状态码查询对象
        - if r.status_code == requests.codes.ok(判断响应态正常与否)
      - raise_for_status() 可以用于抛出异常
    - raw 不常用
