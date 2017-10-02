from urllib import request                  #模拟Request请求
from urllib import parse                    #模拟POST请求


req = request.Request("http://www.baidu.com");
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36");

# 使用PSOT发送请求
postData = parse.urlencode([
        ("username","jion"),
        ("kw","搜索")
    ]);

resp = request.urlopen(req);
print(resp.read());