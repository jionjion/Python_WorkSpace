# https://www.taobao.com/markets/promotion/shumajiadianshiyue

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

# 准备抓取的URL
url = 'https://www.taobao.com/markets/promotion/shumajiadianshiyue';

# 打开网站
try:
    taobao_html = urlopen(url=url);
except HTTPError as e:      
    # 网页打开失败,打印以下并结束
    print("网页打开失败");
    print(e);
else:
    # 网页打开成功,继续执行,读取整个网页
    html = BeautifulSoup(taobao_html.read());
    # 查找其中某个样式节点          <li class="ZM_arrayLi">
    try:
        html_li = html.findAll(name="p",attrs={ "class_" : "ZM_desc"});
    except AttributeError as e:
        print("节点不存在");
        print(e);
    else:
        print(html.prettify());
#         print("查找到节点",html_li);