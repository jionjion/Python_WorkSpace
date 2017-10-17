# 抓取网站  <战争与和平>    
# http://www.pythonscraping.com/pages/warandpeace.html
from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup


# 准备抓取的URL
url = 'http://www.pythonscraping.com/pages/warandpeace.html';

# 打开网站
try:
    warandpeace_html = urlopen(url=url);
except HTTPError as e:      
    # 网页打开失败,打印以下并结束
    print("网页打开失败");
    print(e);
else:
    # 网页打开成功,继续执行,读取整个网页
    html = BeautifulSoup(warandpeace_html.read(),"html.parser");
    # 查找其中某个样式节点          <span class="green">
    try:
        html_span_s = html.findAll(name="span",attrs={ "class" : "green"});
    except AttributeError as e:
        print("节点不存在");
        print(e);
    else:
        # 查找到节点们,并打印节点内的唯一文字
        for span in html_span_s:
            print(span.get_text());
