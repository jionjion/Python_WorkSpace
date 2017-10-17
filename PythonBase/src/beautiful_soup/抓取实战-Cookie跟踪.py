import requests                                                                 # 第三方类库


if __name__ == "__main__":
    '''使用Cookie跟踪技术,维持登录状态'''
    params = {'username': 'Jion', 'password': 'password'};                      # 表单参数
    r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params); # 携带表单参数进行提交
    print("获得服务器响应Cookie:");
    print(r.cookies.get_dict());                                                # 从返回的响应中获取键值对信息
    print("-----------");
    print("正在跳转向欢迎页面...");
    r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",
    cookies=r.cookies);                                                         # 下次请求其他页面,携带cookie信息
    print(r.text);
