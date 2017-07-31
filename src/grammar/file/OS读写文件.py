# 使用os模块下的文件操作符,完成文件的读写操作

#   os.open(filename,flag[,mode])
#    flag:打开文件的方式
#        os.O_CREATE:创建文件
#        os.O_RDONLY:只读
#        os.O_WRONLY:只写
#        os.O_RDWR:读写
#    
#   读取文件  
#     os.read(file,buffersize):读取文件
#     
#   写入文件 
#     os.write(file,string)
# 
#   文件指针
#     os.lseek(file,pos,how)
# 
#   文件关闭 
#     os.close(file)
# 
#   判断文件的权限
#     access(path,mode)    F_OK:存在        R_OK,W_OK,X_OK:读写执行权限
# 
#   返回当前目录下的文件列表 
#     listdir(path)
# 
#   删除文件  
#     remove(path)
# 
#   修改文件或者目录名
#     rename(old,new)
# 
#   创建目录
#     mkdir(path[,mode])
# 
#   创建多级目录
#     makedirs(path[,mode])
# 
#   删除多级目录
#     removedirs(path)
# 
#   删除目录,目录必须为空
#     rmdir(path)
# 
#   判断当前目录是否存在
#     exists(path)
# 
#   判断是否为一个目录 
#     isdir(file)
# 
#   判断是否为一个文件 
#     isfile(file)
# 
#   返回文件大小
#     getsize(file)
#
#   返回路径的目录 
#     dirname(path)
#
#   返回路劲的文件名 
#     basename(path)






