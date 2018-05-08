# -*- coding: utf-8 -*-

'''
    爬取
        http://www.xicidaili.com/nn/1
    该页面下定义了高匿的IP代理地址
        只爬取第一页
'''

import requests
from scrapy.selector import Selector

def crawl_ip():
    url = "http://www.xicidaili.com/nn/1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    # 转为 scrapy.selector进行获取
    selector = Selector(response=response)
    # 获得 表格对象行
    all_trs = selector.css(query="#ip_list tr")
    # 遍历,获得行数据,分片,从第一个开始
    for tr in all_trs[1:]:
        # 国家
        country = tr.css(".country img ::attr('alt')")[0].extract()
        # IP
        ip = tr.css("td ::text")[0].extract()
        # 端口
        port = tr.css("td ::text")[1].extract()
        # 地址
        address = tr.css("td a ::text")[0].extract()
        # 类型
        type = tr.css(".country ::text")[0].extract()
        # 速度, 0.1秒 -> 0.1
        speed = tr.css(".bar ::attr(title)")[0].extract().split('秒')[0]


if __name__ == '__main__':
    crawl_ip()