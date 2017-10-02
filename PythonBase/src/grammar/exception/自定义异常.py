# 使用自定义异常,完成解析

class FileError(IOError):                           #自定义FileError异常,继承自IOError
    pass;                                           #占位符,不做任何处理




raise FileError("抛出自定义异常!");                      #主动抛出异常
