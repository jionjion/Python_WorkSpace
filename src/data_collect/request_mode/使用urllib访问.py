# -*- coding: utf-8 -*-

from urllib import request

url_ip = "http://httpbin.org/ip";

def use_simple_urllib():
    response = request.urlopen(url_ip);
    print("访问页面:>>>>",url_ip);
    print("响应头信息:>>>>\n",response.info());
    
    print("响应体:>>>>\n");
    for l in response.readlines():
        print(l)
    
    
    
    
    

# main方法调用
if __name__ == "__main__":
    use_simple_urllib();    
    
    