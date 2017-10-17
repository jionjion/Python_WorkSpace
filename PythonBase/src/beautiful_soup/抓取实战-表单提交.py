import requests                                                                 # 第三方类库

if __name__ == "__main__":
    '''简单表单提交'''
    params = {'firstname': 'Jion', 'lastname': 'Jion'};                         # 表单数据
    r = requests.post("http://pythonscraping.com/files/processing.php", data=params); # 发送请求
    print(r.text);                                                              # 读取响应
    
    
    files = {'uploadFile': open('../files/Python-logo.png', 'rb')}              # 打开文件
    r = requests.post("http://pythonscraping.com/pages/processing2.php",            
    files=files);                                                               # 提交文件