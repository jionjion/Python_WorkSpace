import requests


if __name__ == "__main__":
    '''使用Session技术,完成会话跟踪'''
    session = requests.Session();                                               # 创建Session对象,基于Session进行各种请求
    params = {'username': 'Jion', 'password': 'password'};                      # Post验证,用户信息 
    s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params); # Session获取
    print("获得服务器响应Cookie");                                                                                                   
    print(s.cookies.get_dict());                                                # Session中维持Cookie信息
    print("-----------");
    print("正在跳转向欢迎页面...");
    s = session.get("http://pythonscraping.com/pages/cookies/profile.php");     # 使用Session进行请求
    print(s.text);