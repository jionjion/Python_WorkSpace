# -*- coding: utf-8 -*-

正则表达式,用于检测一个字符串与我们所设定的字符串符合,实现检索文本,替换文本.

a = 'C1C++2C#3Python4JAVA'

判断是否存在,存在返回位置,否则返回-1
a.index('Python')
使用in关键字,判断是否存在
'Python' in a

re模块,用来做正则的支持
import re

通过findall函数,查询并返回符合要求的字符串
result = re.findall('Python',a)
查找所的数字
result = re.findall('\d',a)

\d      表示[0-9]
\D      表示非数字
\w      表示数字和字母和下划线,不包括特殊字符
\W      表示匹配非单词字符
\s      表示匹配空白字符  空格,回车,换行,制表
\S      表示匹配非空白字符
.       匹配换行符\n以外的所有字符

s = 'abc , acc , adc , aec , afc , ahc'
查找中间字符为b或者c的字符串,普通字符多用于定界
result = re.findall('a[bc]c',s)
查找中间字符是a到c的字符
result = re.findall('a[b-c]c',s)
查找中间不是b或者c的字符串
result = re.findall('a[^bc]c',s)

s = 'python , java , php'

贪婪:尽量匹配数量最大的值,匹配结果尽可能往后,尽可能长
非贪婪:返回首个符合要求的字符

查找字符重复出现3次到6次,贪婪匹配,便于查找最大的长度的符合要求的字符
result = re.findall('[a-z]{3,6}',s)

非贪婪模式,返回最先匹配的字符
result = re.findall('[a-z]{3,6}?',s)

s = 'pytho12python123pythonn123456'

*   表示匹配前面的字符0到无穷次,匹配字符pytho,n可以出现任意次
result = re.findall('python*',s)

+   表示匹配前面的字符1到无穷次,匹配字符pytho,n至少出现一次
result = re.findall('python+',s)

?   表示匹配前面的字符0次或者1次,匹配字符pytho,n可以出现1次或者0次
result = re.findall('python?',s)

{m,n} 表示匹配前面的字符m到n次,匹配字符pytho,n可以出现1到2次,?,返回匹配一次的
result = re.findall('python{1,2}?',s)


s = '8939860'

^   表示从开头匹配
$   表示从结尾匹配
当两者同时出现时,表示匹配传入的整个字符
匹配4-8的数字
result = re.findall('^\d{4,8}$',s)

组
s = 'AbcAbcAbcAbc'
()  用来组成组,将组作为一个整体,匹配'Abc'出现三次的
result = re.findall('(Abc)',s)

匹配模式
s = 'java,python'
re.I    匹配忽略大小写
result = re.findall('Java',s,re.I)
re.S    忽略大小写,全部匹配,包括换行符
result = re.findall('Java',s,re.I|re.S)

字符传串查找替换
s = 'java,python'
替换java为JAVA,默认0无限制替换
result = re.sub('java','JAVA',s,0)

定义自定义处理函数,传入处理函数,解析
def convert(value):
    # value , 传入匹配结果    <_sre.SRE_Match object; span=(0, 4), match='java'>
    print(value)
    return  '!' + value.group() + '!' # 将返回结果作为替换值

传入函数对象,进行复杂的解析过程
result = re.sub('java',convert,s,0)


列如:将字符串中的数字替换,大于5替换为1,否则替换为0
s = '1A1B3D4E9'
def convert(value):
    # 获得匹配结果
    matched = int(value.group())
    if matched > 5 :
        return '1'
    else:
        return '0'

# 对数字替换
result = re.sub('\d',convert,s)

re.match(pattern,string,flags)
    尝试从首字母进行匹配,如果未命中,则返回None,命中则返回 <_sre.SRE_Match object; span=(1, 2), match='1'>

正则匹配
s = 'A1A1B3D4E9'
result = re.match('\d',s)
result = re.search('\d',s)
获得字符的匹配结果
获得分组后的匹配结果,0表示完整分组,1以后表示分组后的结果
result.group(0)     0默认表示完整分组
result.group(0,1)   完整的分组结果,和第一个结果
result.groups(0)    完整的分组结果
获得字符的匹配位置
result.span()


获取字符串中的中文
s = 'hello 上海'
result = re.match('.*?([\u4E00-\u9FA5]+)',s)
result.group(1)


