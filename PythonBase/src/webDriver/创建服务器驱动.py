from selenium import webdriver                                                  # 浏览器对象
from selenium.common.exceptions import TimeoutException                         # 异常包,超时异常
from selenium.webdriver.support.ui import WebDriverWait                         # 工具包,浏览器等待
from selenium.webdriver.support import expected_conditions as EC                # 工具包,逾期情况
from selenium.webdriver.common.by import By                                     # 元素查找,集合类

'''
这里模仿浏览器访问百度搜索页面,输入关键字,点击搜索的过程
'''
executable_path = "E:\\PhantomJS\\bin\\phantomjs";                              # 下载的phantomjs的启动程序位置

driver = webdriver.PhantomJS(executable_path=executable_path);                  # 创建了一个新的  WebDriver浏览器实例

driver.get("https://www.baidu.com/");                                           # 访问百度

print (driver.title);                                                           # 获得浏览器标题

inputElement = driver.find_element_by_name("wd");                               # 获得输入框对象,其name属性值为wd
inputElement = driver.find_element(by=By.NAME, value="wd");                     # 通过name属性获取对象

inputElement.send_keys("哔哩哔哩");                                               # 向输入框输入关键字

inputElement.submit();                                                          # 表单对象提交

try:
    WebDriverWait(driver, 10).until(EC.title_contains("哔哩哔哩"));               # 等待十秒,直到预期浏览器标题页中包含关键词,表示搜索完成,实际显示为:哔哩哔哩_百度搜索

    print (driver.title);                                                       # 获得当前浏览器标题
    print (driver.find_element_by_id("content_left"));                          # 通过ID查询,获得搜索结果
    print (driver.find_element(by=By.ID, value="content_left").text);           # 通过ID查询,获得搜索结果
    driver.get_screenshot_as_file('F:\PYTHON_WorkSpace\PythonBase\src\webDriver\哔哩哔哩.png');
finally:
    driver.quit();                                                              # 浏览器退出
    
