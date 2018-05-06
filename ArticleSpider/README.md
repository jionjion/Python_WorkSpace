工具方法
首先在 http://blog.jobbole.com/all-posts/ 这个网址中获得可以查询到所有的页面

## 创建项目 
    scrapy startproject ArticleSpider
创建一个新的空项目,在scrapy框架下进行不同URL的爬取访问

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
安装PL
    pip install pillow


使用shell脚本启动,访问某个页面,将响应加载入内存,进而通过本地命令行直接进行查询
    scrapy shell http://blog.jobbole.com/110287/                    访问某个页面

## xpath
    article                     选取所有的<article>元素的所有子节点
    /article                    选取根元素<article>
    article/a                   选取所有属于<article>的直接子元素的<a>元素
    //div                       选取所有<div>子元素,无论出现在文档的任何位置
    article//div                选取所有属于<article>元素的后代的div元素,不管它出现在<article>下的任何位置
    //@class                    选取所有名为class的属性,@表示选择属性
    /article/div[1]             选取<article>子元素的第一个<div>元素,下标从1开始
    /article/div[last()-1]      选取<article>子元素的倒数第一个<div>元素
    //div[@lang]                选择所有拥有lang属性的<div>元素
    //div[@lang='en']           选取所有lang属性值为en的<div>元素
    /div/*                      选取属于<div>元素的所有子节点
    //*                         选取所有元素
    //div[@*]                   选取带有属性的<div>元素
    /div/a | //div/p            选取<div>元素下的<a>和<p>元素
    //span | //ul               选取所有的<span>和<ul>元素
    article/div/p | //span      选取所有的<article>元素的<div元素的<p>元素,以及文档中的<span>元素

- 获得标题
    title = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()')      查询xpath路径信息,调用text()方法,只获得文本
    title.extract()     获取文本信息,返回数组信息

- 获得创建时间
    create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()  只获得text文本内容,其他标签自动过滤,返回为一个数组
    create_date = create_date[0].strip()                         去除回车换行符
    create_date = create_date.replace('·','').strip()           去除特殊符号和换行

- 获得点赞
    # contains(属性,包含属性值) 内置函数,搜索属性值匹配的函数
    thumb_num = int( response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0] )

- 获得收藏
    mark_num = response.xpath('//span[contains(@class,"bookmark-btn")]/text()')[0].extract()
    # 获得内容中的数字部分
    mark_num = int ( re.match(r'.*?(\d+).*',mark_num).group(1) )

## CSS选择器

- 选择标题
    # .entry-header类下的h1标签内容, ::text伪类选择器,获得文字内容,返回为一个数组.
    title = response.css('.entry-header h1 ::text').extract()

- 选择创建时间
    create_date = response.css('.entry-meta-hide-on-mobile ::text').extract()[0].replace('·','').strip()

- 选择点赞
    thumb_num = response.css('.vote-post-up h10 ::text').extract()[0]

- 选择收藏
    mark_num = int( re.match(r'.*?(\d+).*',response.css('.bookmark-btn ::text').extract()[0]).group(1) )

# 实战
## 爬取拉钩
### 创建项目
    scrapy genspider -t crawl lagou www.lagou.com
    
### 编写lagou.py,设计抓取规则,设置请求格式

### 编写items.py,设计数据库对象

### 使用shell,设置请求参数或者配置文件获得请求参数

标题:     response.css('.job-name ::attr(title)').extract()
薪资:     response.css('span[class=salary] ::text').extract()
工作地点: response.xpath("//*[@class='job_request']/p/span[2]/text()").extract()
工作经验: response.xpath("//*[@class='job_request']/p/span[3]/text()").extract()
学历要求: response.xpath("//*[@class='job_request']/p/span[4]/text()").extract()
工作性质: response.xpath("//*[@class='job_request']/p/span[5]/text()").extract()
标签:     response.css(".position-label li::text").extract()
发布时间: response.css(".publish_time ::text").extract()
职位诱惑: response.css(".job-advantage p ::text").extract()
职位描述: response.css(".job_bt div").extract()
工作地点: response.css(".work_addr").extract()
公司名称: response.css("#job_company img::attr('alt')").extract()
公司主页: response.css("#job_company ul a::attr('href')").extract()

进一步提炼获取信息

### 分页页面,获得