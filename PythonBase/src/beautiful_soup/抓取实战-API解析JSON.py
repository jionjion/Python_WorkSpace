import json
from urllib.request import urlopen

def getCountry(ipAddress):
    '''解析公网IP,返回IP注册的国家'''
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8');
    responseJson = json.loads(response);
    return responseJson.get("country_code");
    
    
print(getCountry("50.78.253.58"));


# 解析JSON字符串
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}';
jsonObj = json.loads(jsonString);                                               # 加载JSON字符串,转为JSON对象
print(jsonObj.get("arrayOfNums"));                                              # 获得第一层的数组对象
print(jsonObj.get("arrayOfNums")[1]);                                           # 获得第一层的数组对象的第二个对象
print(jsonObj.get("arrayOfNums")[1].get("number"));                             # 获得第一层的数组对象的第二个对象的属性
print(jsonObj.get("arrayOfFruits")[2].get("fruit"));                            # 获得第二层的数组对象的第三个对象的属性