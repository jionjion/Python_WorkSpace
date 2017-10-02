#文件的属性查询

# 打开文件
f = open(file="file.txt", mode="r", encoding="utf8");

# 文件的描述符
print("文件的描述符:",f.fileno());

# 文件的打开权限
print("文件的打开权限:",f.mode);

# 文件的编码格式
print("文件的编码格式:",f.encoding);

# 文件是否关闭
print("文件是否关闭:",f.closed);

#.........


# 文件标准输入
# sys.stdin;

# 文件标准输出
# sys.stdout;

# 文件标准错误
# sys.stderr;

# 得到命令行中的参数列表
# sys.argv