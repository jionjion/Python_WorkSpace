# -*- coding: utf-8 -*-

import re
import requests
# 引入Cookies模块,兼容版本引入
try:
    import cookielib as cookiejar
except:
    import http.cookiejar as cookiejar


# 实例化当前会话,Cookies保存本地
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename="cookies.txt")

# 尝试加载原有的cookies信息
try:
    session.cookies.load(filename="cookies.txt",ignore_discard=True)
except:
    print("未找到本地Cookies")

# 伪造使用者的浏览器信息
header = {
    "HOST":"www.zhihu.com",
    "Referer": "https://www.zhizhu.com",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
}

# 知乎手机登录
def zhihu_login(phone,password):
    print("开始登录...")
    post_url = "https://www.zhihu.com/login/phone_num"
    post_data = {
        "phone_num": phone,
        "password": password
    }
    response = session.post(url=post_url,data=post_data,headers=header)
    # 响应状态码
    print(response.status_code)
    print(response.text)
    with open(file="zhihu_index.html",mode="wb") as file:
        file.write(response.text.encode("UTF-8"))
    print("输出响应页面为本地文件: zhihu_index.html ")
    # 获得响应cookies信息,保存本地
    session.cookies.save()



zhihu_login(15516559772,"zhangqian")