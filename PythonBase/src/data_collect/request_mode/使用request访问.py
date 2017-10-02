# -*- coding: utf-8 -*-
import requests

url_ip = "http://httpbin.org/ip";

def use_simple_request():
    #构建请求参数
    params = {'key':'value'};
    
    #使用get方法请求(请求路径,参数,头部信息)
    response = requests.get(url_ip,params);
    print("访问页面:>>>>",url_ip);
    
    #获得请求头
    print("响应头信息:>>>>\n",response.headers);                 
    
    #获得响应体
    print("响应体:>>>>\n",response.text);                      
        
        

# main方法调用
if __name__ == "__main__":
    use_simple_request();          