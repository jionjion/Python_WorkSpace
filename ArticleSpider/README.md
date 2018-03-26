工具方法
首先在 http://blog.jobbole.com/all-posts/ 这个网址中获得可以查询到所有的页面

## 创建项目 
    scrapy startproject ArticleSpider
创建一个新的空项目

## 文件说明
../spiders/             存放爬虫代码
./items.py              自定义数据类型
./middlewares.py        中间扩展软件
./pipelines.py          数据库储存
./settings.py           配置文件
scrapy.cfg              整体配置文件


## 爬取伯乐在线
在当前项目下,执行
    scrapy genspider jobbole blog.jobbole.com
会创建一个jobbole.py文件在spiders文件夹下

启动当前项目
    jobbolescrapy crawl jobbole

安装win32 
    pip install pypiwin32
    
## xpath
    article                     选取所有的<article>元素的所有子节点
    /article                    选取根元素article
    article/a                   选取所有属于article的直接子元素的a元素
    //div                       选取所有div子元素,无论出现在文档的任何位置
    article//div                选取所有属于article元素的后代的div元素,不管它出现在article下的任何位置
    //@class                    选取所有名为class的属性,@表示选择属性
    /article/div[1]             选取article子元素的第一个div元素
    /article/div[last()-1]      选取article子元素的倒数第一个div元素
    //div[@lang]                选择所有拥有lang属性的div元素
    //div[@lang='en']           选取所有lang属性值为en的div元素
    /div/*                      选取属于div元素的所有子节点
    //*                         选取所有元素
    //div[@*]                   选取带有属性的div元素
    /div/a | //div/p            选取div元素下的a和p元素
    //span | //ul               选取所有的span和ul元素    
    article/div/p | //span      选取所有的article元素的div元素的p元素,以及文档最中的span元素

