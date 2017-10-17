import builtwith
import whois

if __name__ == '__main__':
    '''分析抓取网站中使用到的技术'''
    result = builtwith.parse('http://www.zhihu.com');
    print(result);
    
    result = whois.whois('http://www.zhihu.com');
    print(result);
    