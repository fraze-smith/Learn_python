# 正则表达式
# 此md不能预览
- 正则表达式是通过一定的规则对数据进行选择的一种语言
1. 正则的语法:
  1. 匹配任意字符: .
  2. 匹配单个或多个字符: +
  3. 匹配零个或多个字符: *
  4. 匹配字符集合: [first-last]
    - eg: [a-z] 匹配一个a-z的字符
  5. 匹配数字和字母: \w 匹配非数字和字母: \W
  6. 匹配数字: \d 匹配非数字: \D
  7. 匹配空白字符: \s 匹配非空表字符: \S
  8. 指定重复次数: [a]{num}
    - eg: [a]{5} a字符重复五次
    - eg: [a-c]{2,3} a到c的字符重复2到3次
  9. 分组匹配: (context)
    - 将匹配字符分组
  10. 分组不匹配
    - (字符1|字符2)
  11. 正向预查: (?=字符)
    - eg: \d+(?=元) 匹配数字后面跟着元的字符,而不匹配元
  12. 反向预查: (字符=?)
  13. -eg: (杀手=?)[a-z]+
  - 练习:
    1. 匹配一个邮箱
      [\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?
    2. 匹配url
      (https|http)://[\s]
2. python中正则的使用
  - 需要导入re包
  - match()方法
  - ```python
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    # 第一个参数为正则,第二个为待匹配字符串.若匹配失败则返回None
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
     print(result)
    print(result.group())
    print(result.span())
    ```
  - group()方法
  - ```python
    import re

    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello\s(\d+)\sWorld', content)
    print(result)
    print(result.group())
    print(result.group(1))
    print(result.span())
    ```
    group()将返回所有匹配字符
    group(n) 将返回第n个括号中的字符串
