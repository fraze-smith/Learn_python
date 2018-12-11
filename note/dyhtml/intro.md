# 动态html (dynamic html)
## Selenium + PhantomJS
- Selenium web自动化测试工具
  - [官方文档](https://www.seleniumhq.org/)
  - 自动加载页面
  - 截屏
  - 获取数据
  - 使用Selenium的WebDriver的API进行操作
- PhantomJS
  - 基于webkit的无界面浏览器
  - 弃用,试过各种办法就是不行,用chrome代替.
- chrome+ chromedriver
   - 安装chromedriver
    1. 打开chrome->setting->help:查看版本
    2. 到[http://chromedriver.chromium.org/downloads]下载对应版本.
    3. 解压后将文件链接或移动到环境变量中即可.
- selenium的使用
  1. 导入包```from selenium import webdriver```
          ```from selenium.webdriver.common.keys import Keys```
          模拟键盘操作(Keys是一个类)
          ```from selenium.webdriver.support.ui import Select```
          选择类
  2. 创建一个web实例```driver = selenium.chrome()```
  3. 使用 driver.get(url) 打开一个网页. 但是如果网页使用大量ajax技术,他将不知道何时结束等待.
  4. selenium的操作
    - 得到UI元素
      - find_element_by_id 通过id查找
      - find_elements_by_name 通过姓名查找
      - find_elements_by_xpath 通过xpath查找
      - find_elements_by_link_text 通过链接文本查找
      - find_elements_by_partial_link_text 通过局部链接查找
      - find_elements_by_tag_name 通过tag名称查找
      - find_elements_by_class_name 类名查找
      - find_elements_by_css_selector css选择器查找
      - clear()清空所选元素

    - 基于UI操作的模拟:
    -
      - 鼠标输入
        - cl单击
        - 双击
        - 右键
        - 拖拽
        - 键盘输入
          - send_keys("content") 键入字符
          - send_keys(Keys.RETURN) 键入回车
          - send_keys(Keys.ALT) 键入atl
          - send_keys(Keys.ARROW+DOWN) arrow:箭头 键入下方向
          - send_keys(Keys.ARROW_UP) 键入上方向
     - [../program/sele.py]
    - 关闭浏览器
      - quit() 退出浏览器
      - close() 关闭标签页
