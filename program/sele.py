from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# driver基本相当于html界面
driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)
# 得到wrapper元素的文本
text = driver.find_element_by_id("wrapper").text
print(text)

# 在输入框中输入文字
driver.find_element_by_id("kw").send_keys(u"吴法宗")
# 点击搜索按钮
driver.find_element_by_id("su").click()
time.sleep(5)

driver.save_screenshot("baidu.png")

# 获取cookie

cookies = driver.get_cookies()
print(cookies)

driver.quit()