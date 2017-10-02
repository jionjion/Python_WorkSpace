# 文件的读写练习
# 
# 打开方法
#       open(name[,mode[buf]])
#    name:打开的文件
#    mode:打开方式,默认只读方式打开
#    buf:缓冲区大小
#    
# 读取方式
#    read([size]):读取文件,一次读取多少字节,默认读取完
#    readline([size]):一次读取一行
#    readlines([size]):读取完缓冲期大小的文件,返回每一行构成的列表
#    iter:使用迭代器完成访问
#
# 写入方法
#    write(str):将字符串写入到文件中
#    writelines(sequence_of_strings):写入到多行文件中
#
#
#         文件打开模式:
#             r               只读                                                          文件必须存在
#             w               只写                                                          不存在创建;存在清空
#             a               追加                                                          文件不存在创建
#             r+  w+          读写                                                          
#             a+              读写追加
#             rb,wb,ab,wb+,ab+    二进制方式打开
#
# 文件指针
#       seek(offset[,whence])
#    offset:偏移量,可以为负数,默认向下移动.
#    whence:相对移动的位置.这里首先将文件指针移动到开始/当前/结束位置,随后进行偏移量的修正
#         os.SEEK_SET:相对文件的开始位置
#         os.SEEK_CUR:相对文件当前的位置
#         os.SEEK_END:相对文件结束的位置

