# -*- coding: utf-8 -*-

from enum import  Enum

# 枚举类中创建中,不能出现重复key,当value重复时,后一个会作为前一个的别名
# 单例模式实现,不能实例化

# 枚举类定义
class VIP(Enum):
    YELLOW = 1
    YELLOW_A = 1        # 别名
    GREEN  = 2
    BLACK  = 3
    RED    = 4

@unique    # 单例模式
class VIP(Enum):
    YELLOW = 1
    GREEN  = 2
    BLACK  = 3
    RED    = 4


# 获得枚举类型
VIP.BLACK
# 获得枚举名
VIP.BLACK.name
# 获得枚举值
VIP.BLACK.value

# 枚举的遍历
for v in VIP:
    print(v)

# 遍历全部的枚举,包含别名
for v in VIP.__members__.items():
    print(v)

# 枚举不能比较,但是可以做身份比较  is

# 枚举值转为枚举类
yellow = VIP(1)

