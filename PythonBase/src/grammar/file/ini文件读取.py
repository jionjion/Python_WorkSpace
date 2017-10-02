#         文件结构    
#             节                [session]
#            参数                 name = value

import configparser                                         #导入配置包         

# 创建    
cfg = configparser.ConfigParser();                          #创建对象

# 读取到内存中
cfg.read("file1.ini", "UTF8");                               #读取文件
for se in cfg.sections():                                   #迭代每个session节点
    print(se);                                              #打印节点的名字
    print(cfg.items(se));                                   #迭代节点内存放的所有键值对

# 修改    
cfg.set('user', 'password', '123');                         #修改.(节点名,键,值)

# 追加
cfg.set('user', 'sex', '男');                                #追加.(节点名,键,值)

# 删除
cfg.remove_option('user', 'username');                      #删除节点
cfg.remove_section("hobby");                                #删除session

# 关闭
fp = open(file="file2.ini", mode="w" ,encoding="utf8");     #打开一个空白文件
cfg.write(fp);                                              #将内存中的文件写入到硬盘中