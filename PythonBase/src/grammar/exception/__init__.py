# 对于异常的解析抛出
#
#    常见错误:
#        SyntaxError:语法错误
#        NameError:未定义就使用变量
#        IOError:文件类型错误
#        ZeroDivisionError:零除
#        ValueError:强制类型转换
#   
#   异常分类
#     /----BaseException:所有异常的父类
#      |---KeyboardInterrupt:用户中断异常
#      |---Exception:常见错误的父类
#      |---SystemExit:Python解释器退出
#