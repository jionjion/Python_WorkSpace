# -*- coding: utf-8 -*-

'''
    使用selenium 操控浏览器
'''
from selenium import webdriver
from scrapy.selector import Selector
import time
'''
    模拟登陆知乎
'''
chrome_driver_path = 'E:\PhantomJS\driver\chromedriver.exe'

# 创建浏览器对象
browser = webdriver.Chrome(executable_path=chrome_driver_path)
# 线程睡眠15s
time.sleep(15)

# 请求页面
browser.get('https://www.zhihu.com/signin')

# 输入用户名密码
browser.find_element_by_css_selector('.SignFlow .SignFlow-account input[name="username"]').send_keys('15516559772')
browser.find_element_by_css_selector('.SignFlow .SignFlow-password input[name="password"]').send_keys('zhangqian')

# 模拟点击登陆
browser.find_element_by_css_selector('.SignFlow-submitButton').click()


# 打印游览器获得的页面的源码
print(browser.page_source)

# 转为spider框架
t_selector = Selector(response=browser.page_source)

# 关闭页面
# browser.close()