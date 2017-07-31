# 文件读取的方式

from os import SEEK_SET

# 打开文件
f = open(file="file.txt", mode="r+", encoding="utf8");

# 一次读取指定长度的行,(默认读取一整行),当当前行字节长度小于指定长度时,全部读取
line = f.readline(2);
print("文件内容:",line);

# 一次性读取缓冲大小的文件8000多字节,返回每一行构成的列表,当前
lines = f.readlines();                                  #小于当前行的字节时仍产输出当前行的字节    
print("文件内容:",lines);

# 获取指针的位置
print("当前的文件指针位置:",f.tell())
# 将指针回到文件开始处
f.seek(0,SEEK_SET);                                     #首先将指针移动到文件开始,随后进行修正

# 使用迭代器完成对每行的读取
iter_f = iter(f);                                       #将文件传入到迭代器中,进行迭代
for line in iter_f:
    print("当前行内容:",line);

# 关闭文件
f.close();

