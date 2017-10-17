# 从页面中的经过最少次跳转,到达另一个不相关的页面,这里忽略异常捕获
# 对Wike中的链接进行递归打开
import re                                                                       # 正则模块
from urllib.request import urlopen                                              # 请求模块
import datetime                                                                 # 时间模块
import random                                                                   # 随机数模块
from bs4 import BeautifulSoup                                                   # - -

pages = set();                                                                  # 全局变量,去重存放抓取的页面

random.seed(datetime.datetime.now());                                           # 随机数设置种子为当前时间
def getLinks(a_url):                                                            # 创建函数
    '''根据传入的url打开网页,返回抓取的页面中的<a>标签下的链接'''
    a_url = "https://en.wikipedia.org"+a_url;
    html = urlopen(url=a_url);                                                  # 打开页面
    html = BeautifulSoup(html,"html.parser");                                   # 解析为对象
    
    ''' 匹配规则:
        URL 都在 id 是 bodyContent 的 div 标签里
        URL 链接不包含分号
        URL 链接都以 /wiki/ 开头
    '''
    return html.find("div",{"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"));          # 查找所有<a>标签
        
def getContext(a_url):
    '''根据传入的URL,打印维基百科的词条名称和第一行简介'''
    html = urlopen(url=a_url);
    html = BeautifulSoup(html,"html.parser");
    print("词条:",html.find("h1").get_text());
    print("简介:",html.find(id="mw-content-text").findAll("p")[0].get_text());
    

links = getLinks("/wiki/Kevin_Bacon");                                          # 开始查询的URL
while len(links)>0:
    new_link = links[random.randint(0,len(links)-1)].attrs["href"];             # 从抓取页面中的所有链接地址中随机选取一个
    if new_link not in pages:                                                   # 不为已存的链接,为新链接
        pages.add(new_link);
        print("随机获取链接:","https://en.wikipedia.org"+new_link);
        getContext("https://en.wikipedia.org"+new_link);                                                   # 打印获取页面的词条名称和第一段简介
        links = getLinks(new_link);                                             # 将随机获取的链接传入,继续打开,递归查询
            
