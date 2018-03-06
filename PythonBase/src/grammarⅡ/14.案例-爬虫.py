# -*- coding: utf-8 -*-

'''
    使用爬虫,爬取熊猫TV下的主播排名
    beautifuSope
    Scrapy
    代理IP库
'''
from urllib import request
import re

class Spider():

    # 熊猫TV
    url = 'https://www.panda.tv/cate/lol'
    # 根节点,匹配正则,定位标签内的全部,避免贪婪模式,在最近一个</div>结束,使用组概念,匹配跟组元素一致的标签
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    # 主播名字,匹配正则,使用分组,匹配标签内的元素
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # 关注人数,匹配正则

    # 私有方法
    def __fetch_content(self):
        res = request.urlopen(url=Spider.url)
        # 读取字节
        htmls = res.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    # 分析方法
    def __analysis(self,htmls):
        # 1.寻找到标示符下的所有标签
        root_html = re.findall(Spider.root_pattern,htmls)
        # 2.循环,获得各个的信息
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {'name':name , 'number':number}
            anchors.append(anchor)
        return anchors

    # 精炼数据
    def __refine(selfs,anchors):
        # 去除换行,空格
        l = lambda anchor: {'name':anchor['name'][0].strip(),'number':anchor['number'][0].strip()}
        return  map(l,anchors)

    # 排序函数,返回一个可以比较的数值,这里取观看人数
    def __sort_seed(self,anchor):
        # 提取数字,返回是一个列表
        result = re.findall('\d*',anchor['number'])
        number = float(result[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    # 业务处理,排序
    def __sort(self,anchors):
        # 排序比较函数,传入自定义的比价函数,降序排列
        anchors = sorted(anchors,key=self.__sort_seed,reverse=True)
        return  anchors

    # 展现数据
    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print( 'rank ' +str(rank+1) + ' : ' + anchors[rank]['name'] + ' -- ' + anchors[rank]['number'])

    # 入口方法
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = self.__refine(anchors)
        anchors = self.__sort(anchors)
        self.__show(anchors)

if __name__ == '__main__':
    # 实例化
    spider = Spider()
    # 执行入口函数
    spider.go()