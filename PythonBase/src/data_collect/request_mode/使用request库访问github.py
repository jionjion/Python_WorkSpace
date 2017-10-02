# -*- coding: utf-8 -*-
import json

from requests import exceptions, auth
import requests
from requests.models import Request
from requests.sessions import Session


Request

def json_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def request_method():
    #使用get方式,获得github上的用户信息
    response = requests.get('https://api.github.com/users/jionjion');       
    print(json_print(response.text));
    
def request_method_within_3():
    #使用get方式,获得github上的前三个用户
    response = requests.get('https://api.github.com/users',params={"since":3});       
    print(json_print(response.text));    
    print("请求头",response.request.headers);
    print("请求路径",response.url);
    
def timeout_request():
    #设置超时时间,捕捉超时异常
    try:
        response = requests.get('https://api.github.com/users',timeout=0.1);#设置超时时间
        response.raise_for_status();
    except exceptions.Timeout as e:                             #捕获超时异常
        print("超时异常..",e);
    except exceptions.HTTPError as e:                           #捕获请求异常
        print("http异常...",e);    
        
def hard_request():
    #定义request请求的内容
    session = Session();
    headers = {'User-Agent':'fake1.3.4'};
    request = Request(method="get",url="https://api.github.com/users/jionjion", headers=headers);
    prepped = request.prepare();
    print("请求体:>>>",prepped.body);
    print("请求头:>>>",prepped.headers);
    
    response = session.send(prepped,timeout=5);
    print("响应码:>>>",response.status_code);
    print("响应头:>>>",response.headers);
    print("相应内容:>>>",response.text);
    
def response_method():
    response = requests.get('https://api.github.com/users/jionjion');       
    print("响应状态码:>>>",response.status_code);
    print("响应头部:>>>",response.headers);
    print("响应路由:>>>",response.url);
    print("响应方式:>>>",response.reason);
    print("响应跳转路由:>>>",response.elapsed);
    print("响应耗费:>>>",response.request);
    print("响应体编码:>>>",response.encoding);
    print("响应体原始内容:>>>",response.raw);
    print("响应体字节文本:>>>",response.content);
    print("响应体txt文本:>>>",response.text);
    print("响应体JSON版本:>>>",response.json);                               #可以使用json()['KEY']的方法,获得内容
    
    
def download_images():
    #从网络下载图片.注意下载图片的格式
    url = "https://avatars2.githubusercontent.com/u/24974015?v=4&s=460";
    response = requests.get(url=url, stream=True);                                      #支持数据流传播
    print("响应状态码:>>>",response.status_code);
    print("二级制信息:>>>",response.content)
    with open(file="photo.jpg", mode="wb", ) as jpg:                                     #打开文件
        for data_block in response.iter_content(256):                                   #读取数据流,写入文件中
            jpg.write(data_block);
        
def basic_auth():
    #使用认证,传入用户密码作为请求
    response = requests.get('https://api.github.com/user',auth=('jionjion','zhangqian520'));           
    print("认证内容:>>>",response.text);
    
def basic_oauth():
    #使用oauth认证,修改服务器端资料
    headers = {'Authorization':'token 你的令牌'};
    response = requests.get("https://api.github.com/user", params=headers);
    print("响应体:>>>",response.request.headers);
    print("响应文:>>>",response.text);
        
# main方法调用
if __name__ == "__main__":
#     request_method();
#     request_method_within_3();
#     timeout_request();
#     hard_request();
#     response_method()
#     download_images();
    basic_auth();