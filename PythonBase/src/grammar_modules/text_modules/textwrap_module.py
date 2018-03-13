# -*- coding: utf-8 -*-
'''
    textwrap 用于通过限制输出宽度，添加缩进和插入换行,
        对段落中的文本进行格式化的工具
'''
import textwrap

if __name__ == '__main__':

    # 一段简单的示例文档,一般过长的文档我们可以单独存放在一个文件中.
    simple_txt = '''
                    you see, this is a stage a word , there are so many wrong word
                    and this look like not good, but what can I do ? 
                '''


    print(simple_txt)

    # [fill] 保持左对齐,并设置最大显示宽度,但是并不负责段首缩进
    print(textwrap.fill(text=simple_txt,width=40))

    # [dedent] 保持左对齐,并删除左侧缩进,注意,删除的是所有行中共有的空白部分,如果某行行首空白过多,缩进后仍会有较多空白
    print(textwrap.dedent(text=simple_txt))

    # [indent] 函数中predicate参数指定渲染的函数名,函数返回布尔值
    def show_indent(line):
        # line为传入的本行数据
        return 'word' in line

    # [indent] 为每一行的行首添加共同的字符,第三个参数,指定处理的函数名,对每一行是否添加行首修饰做限制
    print(textwrap.indent(text=simple_txt,prefix='this line has "word">>',predicate=show_indent))

    # [shorten] 截断指定长度,当段落过长时,可以设定截断,使后边的隐藏
    print(textwrap.shorten(text=simple_txt,width=50))

    # [首行缩进2字符] 悬挂缩进,只是使段首第一行缩进.initial_indent:首行前缀,subsequent_indent:其他行前置
    simple_txt = textwrap.dedent(simple_txt).strip()
    print(textwrap.fill(simple_txt,initial_indent=' ' * 4,subsequent_indent='',width=40))