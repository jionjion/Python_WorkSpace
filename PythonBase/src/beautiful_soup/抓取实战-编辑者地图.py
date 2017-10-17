from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

random.seed(datetime.datetime.now());                                           # 将当前日期作为随机数种子

def getLinks(articleUrl):                                                       
    '''传入URL,获得当前页面的其他URL站内链接'''
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    '''查找当前词条页面的历史编辑信息,返回编辑者的IP的哈希集合'''
    pageUrl = pageUrl.replace("/wiki/", "");                                    # 在当前页面的URL地址中,剔除字符串/wiki/
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history";
    print("当前历史页面:",historyUrl);                                             # 获得当前词条页面的历史页面
    html = urlopen(historyUrl);
    bsObj = BeautifulSoup(html,"html.parser");
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"});              # 查询包含有IP节点的字符串
    addressList = set();                                                        # 为当前词条编辑者IP单独创建Set集合,避免重复编辑人
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList                                                          # 返回当前IP的哈希集合

def getCountry(ipAddress):                                              
    '''根据传入IP查询所在国家'''
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8');  # 调用API
    except HTTPError:
        return None                                                             # 发生错误时,不做返回
    responseJson = json.loads(response);
    return responseJson.get("country_code");                                    # 返回API响应中的国家信息


if __name__ == '__main__':                                                      # 主方法中调用
    links = getLinks("/wiki/Python_(programming_language)");                    # 调用方法,搜索起始页面,获得该页面下的链接 
    while(len(links) > 0):
        for link in links:                                                      # 对每个内链的历史进行抓取
            print("-------------------");
            historyIPs = getHistoryIPs(link.attrs["href"]);                     # 调用方法,获得编辑者的IP
            for historyIP in historyIPs:
                country = getCountry(historyIP);                                # 调用方法,获得编辑者的地理位置信息
                if country is not None:
                    print(historyIP+"来自"+country);                             # 对非空的地址信息进行打印
    
        newLink = links[random.randint(0, len(links)-1)].attrs["href"];         # 随机挑选下个页面的URL
        links = getLinks(newLink);                                              # 获得下个页面的内链信息