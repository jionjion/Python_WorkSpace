from PIL import Image
from PIL import ImageOps
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
import requests
import subprocess

def cleanImage(imagePath):
    '''本地验证码图片二值化处理'''
    image = Image.open(imagePath);                                              # 根据路径,打开图片
    image = image.point(lambda x: 0 if x < 143 else 255);                       # 图片二值化,非黑即白
    borderImage = ImageOps.expand(image, border=20, fill='white');              # 修改图片
    borderImage.save(imagePath);                                                # 保存图片
    

if __name__ == "__main__":
    html = urlopen("http://www.pythonscraping.com/humans-only");                # 打开具有验证码的图片
    bsObj = BeautifulSoup(html,"html.parser");                                  # 解析为对象
    # 收集需要处理的表单数据（ 包括验证码和输入字段）
    imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"];       # 验证码图片相对地址
    formBuildId = bsObj.find("input", {"name":"form_build_id"})["value"];       # 验证码隐藏的input输入框
    captchaSid = bsObj.find("input", {"name":"captcha_sid"})["value"];          # 隐藏的验证码input输入框,服务器生成的验证码的ID,唯一序列
    captchaToken = bsObj.find("input", {"name":"captcha_token"})["value"];      # 隐藏的验证码input输入框,服务器生成的验证码的token,过期时间
    
    captchaUrl = "http://pythonscraping.com" + imageLocation;                   # 验证码图片的绝对地址
    urlretrieve(captchaUrl, "captcha.jpg");                                     # 保存验证码图片到本地
    cleanImage("captcha.jpg");                                                  # 图片二值化
    p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE);       
    p.wait();                                                                   # 等待识别过程..
    f = open("captcha.txt", "r");                                               # 将识别结果存入临时文件
    
    # 清理识别结果中的空格和换行符
    captchaResponse = f.read().replace(" ", "").replace("\n", "");              # 清理识别结果
    print("验证码识别结果: " + captchaResponse);
    if len(captchaResponse) == 5:                                               # 长度为5位的验证
        params = {"captcha_token":captchaToken,
                   "captcha_sid":captchaSid,
                   "form_id":"comment_node_page_form", 
                   "form_build_id": formBuildId,
                   "captcha_response":captchaResponse, 
                   "name":"Ryan Mitchell",
                   "subject": "I come to seek the Grail",
                   "comment_body[und][0][value]":"...and I am definitely not a bot"}; # 构建传递参数
        
        r = requests.post("http://www.pythonscraping.com/comment/reply/10",data=params); #表单提交
        responseObj = BeautifulSoup(r.text);                                    # 读取响应
        if responseObj.find("div", {"class":"messages"}) is not None:
            print(responseObj.find("div", {"class":"messages"}).get_text());    # 获得关键信息
    else:
        print("验证码登录失败...")
