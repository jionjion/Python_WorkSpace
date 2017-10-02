# 文件读取的方式
# 当文件写入到缓存中够一定字节长度后,默认将文件写入到硬盘文件中.当然,也可以调用flush()方法完成

# 打开文件
f = open(file="file.txt", mode="r+", encoding="utf8");

# 写入文件一行
f.write("写入内容");

# 写入文件多行
f.writelines(['写入内容2','写入内容3','写入内容4']);

f.flush();
# 关闭文件
f.close();
