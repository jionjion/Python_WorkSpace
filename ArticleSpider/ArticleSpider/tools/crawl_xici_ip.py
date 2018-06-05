# -*- coding: utf-8 -*-

'''
    爬取
        http://www.xicidaili.com/nn/1
    该页面下定义了高匿的IP代理地址
        只爬取第一页
'''

import requests
from scrapy.selector import Selector
import MySQLdb


class IpDate(object):
    def __init__(self, country, ip, port, address, type, speed, live):
        self.country = country
        self.ip = ip
        self.port = port
        self.address = address
        self.type = type
        self.speed = speed
        self.live = live



def crawl_ip():
    # 将要获得的IP数组
    ip_list = []

    # 循环,获取所有url下的数据,只爬取100页即可
    for page in range(100):
        # 拼接URL
        url = "http://www.xicidaili.com/nn/{0}".format(page)
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
            try:
                # 国家
                country = tr.css(".country img ::attr('alt')")[0].extract()
                # IP
                ip = tr.css("td ::text")[0].extract()
                # 端口
                port = tr.css("td ::text")[1].extract()
                # 地址
                address = tr.css("td a ::text")[0].extract()
                # 类型
                type = tr.css("td ::text")[6].extract()
                # 速度, 0.1秒 -> 0.1
                speed = tr.css(".bar ::attr(title)")[0].extract()
                # 存活时间
                live = tr.css("td ::text")[17].extract()

                # 封装为对象
                ipDate = IpDate(country=country, ip=ip, port=port, address=address, type=type, speed=speed, live=live)
                ip_list.append(ipDate)

            except Exception as e:
                print('发生异常:', e)
            continue
    # 返回结果
    return ip_list


# 保存IP的方法
def save_ip(ip_list):
    conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", password="123456", database="scrapy",
                           charset="utf8")
    cursor = conn.cursor()
    for IP in ip_list:
        # 检查,速度过低,以及连接时间过短的,不进行保存
        if  float(IP.speed.split('秒')[0]) >= 0.1:
            continue
        # 存活不超过30天

        if not (str.endswith(IP.live,'天') and float(IP.live.split('天')[0]) >= 30) :
            continue
        # 插入SQL
        SQL = """
                insert into proxy_ip(country, ip, port, address, type, speed, live)
                values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')
                """.format(IP.country, IP.ip, IP.port, IP.address, IP.type, IP.speed, IP.live)
        cursor.execute(query=SQL)
    # 提交事务
    conn.commit()
    cursor.close()
    conn.close()


# 从数据库中随机获取一个IP,检查后返回
def get_random_ip():
    conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", password="123456", database="scrapy",
                           charset="utf8")
    cursor = conn.cursor()
    # 随机获得1条数据
    SQL = """
                select country, ip, port, address, type, speed, live from proxy_ip
                order by rand()
                limit 1
            """
    result = cursor.execute(query=SQL)
    # 循环,游标获得数据
    ip_list = []
    for ip_date in cursor.fetchall():
        ipDate = IpDate(country=ip_date[0], ip=ip_date[1], port=ip_date[2], address=ip_date[3], type=ip_date[4],
                        speed=ip_date[5],live=ip_date[6])
        # 检查IP
        if check_ip(ipDate):
            ip_list.append(ipDate)
    cursor.close()
    conn.close()
    # 如果IP全部获取失败,递归调用自身
    if ip_list.__len__() == 0:
        return get_random_ip()
    return ip_list

# 删除数据库中不能用的IP
def delete_ip(ipDate):
    conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", password="123456", database="scrapy",
                           charset="utf8")
    cursor = conn.cursor()
    SQL = """
                delete from proxy_ip 
                where ip = '{0}'
                and port = '{1}'
            """.format(ipDate.ip, ipDate.port)
    cursor.execute(query=SQL)
    conn.commit()
    cursor.close()
    conn.close()

# 测试,如果失败则删除
def check_ip(ipDate):
    baidu_url = "http://www.baidu.com"
    try:
        # 设置代理,代理类型
        proxy_dict = {
            "{0}".format(ipDate.type): "{0}://{1}:{2}".format(ipDate.type, ipDate.ip, ipDate.port)
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        res = requests.get(url=baidu_url, proxies=proxy_dict, headers=headers, timeout=2)
        print("代理IP可用:", proxy_dict)
        return True
    except Exception as e:
        print("代理失败:", e)
        return False
        # 删除IP
        delete_ip(ipDate)

if __name__ == '__main__':
    ip_list = crawl_ip()
#     # print(ip_list[10].__dict__)
#       ip_list = []
#     # ip = IpDate(1,2,3,4,5,6)
#     # ip_list.append(ip)
    save_ip(ip_list)
#     for ipDate in get_random_ip():
#         check_ip(ipDate)
