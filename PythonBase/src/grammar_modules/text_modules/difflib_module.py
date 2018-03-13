# -*- coding: utf-8 -*-
'''
     difflib 模块
        文本比较,比较段落之间的不同
'''
import difflib

if __name__ == '__main__':
    text1 = '''this is a right essay,
                look at me QvQ.'''
    # 删除换行符
    text1 = text1.splitlines()

    text2 = '''this a wrong essay,
                don't see me TvT.'''
    # 删除换行符
    text2 = text2.splitlines()

# 比较两个文档的不同
d = difflib.Differ()
diff = d.compare(text1,text2)
print('\n'.join(diff))
