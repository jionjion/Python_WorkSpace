import datetime
import random
import re    
from urllib.request import urlopen 

from bs4 import BeautifulSoup
import pymysql


def getLinks(a_url):                                                            # 创建函数
    '''根据传入的url打开网页,返回抓取的页面中的<a>标签下的链接'''
    a_url = "https://en.wikipedia.org"+a_url;
    html = urlopen(url=a_url);                                                  # 打开页面
    html = BeautifulSoup(html,"html.parser");                                   # 解析为对象
    
    ''' 匹配规则:
        URL 都在 id 是 bodyContent 的 div 标签里
        URL 链接不包含分号
        URL 链接都以 /wiki/ 开头
    '''                                                                         # 查找所有<a>标签
    return html.find("div",{"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"));          

def getContext(a_url):
    '''根据传入的URL,打印维基百科的词条名称和第一行简介'''
    html = urlopen(url=a_url);
    html = BeautifulSoup(html,"html.parser");
    html_dict = {'title':html.find("h1").get_text()
        ,'context':html.find(id="mw-content-text").findAll("p")[0].get_text()}; # 词条和段首
    return html_dict;


def store(title, content):
    '''插入标题及首短内容'''
    conn = pymysql.Connect(host='127.0.0.1', user='root',charset='utf8',
                       passwd='123456', database='python');                     # 创建连接    
    cur = conn.cursor();                                                        # 创建游标    
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")"
                , (title, content));                                            # 执行插入操作
    cur.connection.commit();                                                    # 手动提交
    cur.close();                                                                # 关闭资源
    conn.close();


if __name__ == "__main__":
    '''将查询到的词条和其简介储存在数据库中'''
    pages = set(); 
    links = getLinks("/wiki/Kevin_Bacon");                                      # 开始查询的URL
    while len(links)>0:
        new_link = links[random.randint(0,len(links)-1)].attrs["href"];         # 从抓取页面中的所有链接地址中随机选取一个
        if new_link not in pages:                                               # 不为已存的链接,为新链接
            pages.add(new_link);
            print("随机获取链接:","https://en.wikipedia.org"+new_link);
            html_dict = getContext("https://en.wikipedia.org"+new_link);        # 打印获取页面的词条名称和第一段简介
            store(title=html_dict['title'], content=html_dict['context']);
            links = getLinks(new_link);                                         # 将随机获取的链接传入,继续打开,递归查询
                

    
    


