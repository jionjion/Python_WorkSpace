# -*- coding: utf-8 -*-    
# 行首表示统一编译语言为UTF-8

# 打印函数
print ('hello world');                  #直接打印
print('hello','world');                 #中间逗号间隔,会被解析为空格输�?

print('\'转义字符\'')                      #使用\转义字符
print(r'哔哩哔哩>0<');                     #使用r修饰后的字符内的全部标点默认进行转义输出
print(''' 这是�?个多行输�?
            可以进行换行,制表输出''');                 #使用'''''',中间写入多行文字进行输出
            
# 截取字符
string = 'ABCDEFG';
s = string[:3];                         #截取前三个字符
s = string[-3:];                        #从倒数第三个到结束 
s = string[::2];                        #每两个取一个
print(s);