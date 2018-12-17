# 美丽汤4的使用
- Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库
- [bs4的中文文档](https://www.crummy.com/software/BeautifulSoup/bs4/do
## bs模块与函数:
- 将一段文档传入bs构建一个对象```soup = bs(open(doc)) or soup = bs("name_doc")```
  文档会被转换为unicode编码,所有的html实例都会被编码.
  bs会自动选择解析器,也可以手动选择解析器,推荐使用lxml```soup = bs("name_doc","lxml")```
  - bs对象的种类:
    - bs会将html解析成树结构,每一个节点都是一个python对象
    - tag对象:
      - name属性
        - name属性通过.name获取,```tag.name```
      - attributes属性
        - 可以使用字典查找```tag['class']```
        - 也可以点取tag.attrs
      - 属性可以被修改和删除,方法和字典相同
        ```python
        tag['class'] = 'verybold'
        tag['id'] = 1
        tag
        # <blockquote class="verybold" id="1">Extremely bold</blockquote>

        del tag['class']
        del tag['id']
        tag
        # <blockquote>Extremely bold</blockquote>

        tag['class']
        # KeyError: 'class'
        print(tag.get('class'))
        # None
        ```
      - 多值属性:
        当一个属性有多个值时,bs将返回一个list
    - NavigableString对象
      - 字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串
      - 一个 NavigableString 字符串与Python中的Unicode字符串相同,并且还支持包含在 遍历文档树 和 搜索文档树 中的一些特性. 通过 unicode() 方法可以直接将 NavigableString 对象转换成Unicode字符串
      - 未完待续...
    - BeautifulSoup对象
      - BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象,它支持 遍历文档树 和 搜索文档树 中描述的大部分的方法.
      - 因为 BeautifulSoup 对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 .name 属性是很方便的,所以 BeautifulSoup 对象包含了一个值为 “[document]” 的特殊属性 .name(也就是说当你访问bs的name时将得到docment)
    - Comment对象
      - Comment 对象是一个特殊类型的 NavigableString 对象
        comment是一个注释
- 遍历文档树
  - 获取节点最简单的办法就是直接输入name属性,但是只能匹配第一个
    ```soup.head```
    如果要获取多个需要用到find_all()方法
    ```soup.find_all(\'a\') # 获取所有soup下a标签的内容```
  - 通过tag的 .children 生成器,可以对tag的子节点进行循环
- bs支持css选择器
  - 使用selet()方法即可找到对应tag
