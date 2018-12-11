未完待续....
# XML: eXtensible Markup Language(可拓展标记语言)
- [xml中文文档](http://www.w3school.com.cn/xml/index.asp)
- Xpath的开发工具
  - Xpath表达式工具: XMlquire
  - chrome插件: Xpath Helper
# Xpath
  - Xpath是在XML文件中进行查找的规则,根据元素和属性进行遍历.
  - XML: eXtensible Markup Language(可拓展标记语言)
  ## Xpath语法:
  1. 选取节点
    - nodename: 选取此节点的所有子节点
    - /: 从根节点选取
    - //: 从匹配选择的当前节点选择文档的节点,而不考虑他们的位置 (即所有的子孙节点)
    - . 从当前节点选取
    - .. 从父节点选取
    - @: 选择属性.
  2. 谓语:
    - 谓语用于查找某个特定节点或者包含某个特定值的节点.
    - 谓语镶嵌在括号[]中.
    - 例子:
      - /booksotre/book[1]: 选取bookstore中第一个book元素.
      - /bookstore/book[last()]: 选取最后一个元素.
      - /bookstore/book[last()-1]: 选取倒数第二个元素.
      - /bookstore/book[positon()<n]: 选取前n-1个元素.
      - //title[@lang]: 选取所有title中有lang属性的元素
      - //title[@lang='eng']: 选取所有title中lang属性为eng的元素
      - /bookstore/book[price>35.00]/title: 选取book元素中price元素大于35中的title元素
  3. 通配符:
    - * 匹配所有元素节点
    - @* 匹配任何属性节点
    - node() 匹配任何类型节点
  4. 选取多个路径
    - 使用管道符
    - 例如: //book/title | //book/price
  5. 运算符 算数运算符和布尔运算符
# lxml
- pyhton的html或xml的解析器
- [官方文档](https://lxml.de/)
- 未在pyhton标准库中,需要安装.
- import lxml
