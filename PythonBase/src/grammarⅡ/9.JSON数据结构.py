# -*- coding: utf-8 -*-

JSON            一种轻量级的数据交换格式
JSON对象        不同语言定义的对象实例
JSON字符串      字符串
注意,Key-value用双引号包裹,

import json

json_str = '[{"name":"Jion","age":24},{"name":"Arise","age":25}]'
# 将JSON字符串转为dict字典类型,反序列化
students = json.loads(json_str)
# 读取元素

arr_str = [{'name': 'Jion', 'age': 24}, {'name': 'Jion', 'age': 24}]
# 将arr数组转为序列化转为JSON字符串对象
json_str = json.dumps(arr_str)
print(json_str)