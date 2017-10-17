from selenium import webdriver                                                  # 第三方类库
import time

if __name__ == "__main__":
    '''使用PhantomJS类库 ,模拟浏览器访问页面:该页面会在访问3秒后自动跳转,这里我们采集跳转后的页面'''
    executable_path = "E:\\PhantomJS\\bin\\phantomjs";                          # 下载的phantomjs的启动程序位置
    driver = webdriver.PhantomJS(executable_path=executable_path);              # 创建了一个新的 Selenium WebDriver
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html");     # 加载页面
    time.sleep(10);                                                             # 睡眠10秒
    print(driver.find_element_by_id('content').text);                           # 利用PhantomJS类库的元素查找方式,完成解析
    driver.close();                                                             # 关闭类库