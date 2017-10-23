# 对WebDriver的API进行使用


# WebDriver与phantomjs的关系
'''
前者是一个浏览器驱动,可以看做是各种浏览器的实例,比如谷歌浏览器,火狐浏览器,可以模拟浏览器完成浏览器事件
后者是一个自定义浏览器,可以完成浏览器的解析JS,加载HTTP请求等操作.

一般我们通过phantomjs生成WebDriver的实例,模拟各种HTML动态操作,便于抓取某一时刻的页面
'''


    
# 获得元素的常用方式    
'''
    通过ID获得
    element = driver.find_element_by_id("元素的id值")
    element = driver.find_element(by=By.ID, value="元素的id值")

    通过class获得
    cheeses = driver.find_elements_by_class_name("元素的class值")
    cheeses = driver.find_elements(By.CLASS_NAME, "元素的class值")
    
    通过tag获得
    div = driver.find_element_by_tag_name("div")
    div = driver.find_element(By.TAG_NAME, "div")
    
    通过name属性获得
    cheese = driver.find_element_by_name("元素的name值")
    cheese = driver.find_element(By.NAME, "元素的name值")

    通过链接文本
    cheese = driver.find_element_by_link_text("链接中的本文")
    cheese = driver.find_element_by_partial_link_text("链接中包含的文本")
    cheese = driver.find_element(By.LINK_TEXT, "链接中的文本")
    cheese = driver.find_element_by_partial_link_text("链接中包含的文本")
    
    通过CSS选择器,看各位CSS样式的功底咯    T^T
    cheese = driver.find_element_by_css_selector("#food span.dairy.aged")
    cheese = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")
'''    
    
# 执行页面的JS文件
'''
    通过元素的获取,进而执行文件
    element = driver.execute_script("alert('哔哩哔哩')")
'''

# element对象属性,方法
'''
    element.text            获得本文属性值
    
'''
    
# 表单填写
'''
    文本框,文本域
    inputElement.send_keys("填入内容")
    
    下拉选框
    select = driver.find_element_by_tag_name("select")                          获得下拉框对象
    allOptions = select.find_elements_by_tag_name("option")                     获得选项
    select.deselect_all()                                                       全选
    select.select_by_visible_text("选项值")                                       通过选项值选择
    for option in allOptions:                                                   遍历选项
        print "Value is: " + option.get_attribute("value")                      获得选项值
        option.click()                                                          模拟点击操作

    表单提交
    submit = driver.find_element_by_id("submit")                                获得提交按钮
    submit.click()                                                              点击提交
    
    通用提交
    element.submit()                                                            获得表单元素的form下的提交按钮,并执行
'''    

# 窗口切换
'''
    切换不同的窗口
    driver.switch_to.window("窗口的名字")
    
    切换不同的框架
    driver.switch_to.frame("框架的名字")
'''    

# 网页浏览记录
'''
    打开网页
    driver.get("http://www.example.com")
    历史前进
    driver.forward()
    历史后退
    driver.back()
'''

# cookies操作
'''
    添加
    driver.add_cookie({'name':'key', 'value':'value', 'path':'/'})
    获得
    for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value'])
    指定删除
    driver.delete_cookie("CookieName")
    删除全部
    driver.delete_all_cookies()
'''

# 浏览器等待
'''
    显式等待
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "特征id出现")))
    finally:
    
    显式等待
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID,'特征id出现')))
    
    隐式等待,默认不指定则一直等待
    driver.implicitly_wait(10)
'''

# 截图
'''
    对当前访问页面进行截图保存
    driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX.copy())
    driver.get("http://www.google.com")
    driver.get_screenshot_as_file('/Screenshots/google.png')
'''