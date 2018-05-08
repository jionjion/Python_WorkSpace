# -*- coding: utf-8 -*-
import requests
from PIL import Image
from numpy import *
from pylab import *
import pickle

# 下载验证码
def downloading_code():
    i = 1
    while i <= 1000:
        ir = requests.get("http://10.18.111.128/hls/imagecode")
        if ir.status_code == 200:
            code_file_name = "cs/" + "code_" + str(i) + '.jpg'
            open(code_file_name, 'wb').write(ir.content)
            print("生成验证码...", code_file_name)
        i = i+1

# 图片格式转换 -> .jpg
def convert_image_to_jpg():
    for infile in filelist:
        outfile = os.path.splitext(infile)[0] + ".jpg"
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print ("转换失败", infile)

# 显示图片和灰度
def show_gray():
    # 图片
    code_file = 'F:\PYTHON_WorkSpace\ArticleSpider\cs\code_2.jpg'
    # 灰度,读取图像到数组中,绘制图像要求多维数组结构
    im = array(Image.open(code_file).convert('L'))
    # 新建一个图像
    figure()
    # 不使用颜色信息
    gray()
    # 在原点的左上角显示轮廓图像
    contour(im, origin='image')
    axis('equal')
    axis('off')
    figure()
    # flatten()将多维度数组压制为单一维度数组
    hist(im.flatten(), 128)
    # 展示
    show()
    # 保存图片方法
    # image.save('temp.jpg')

# 缩放图片
def imresize(im,sz):
    # 创建数组,传入图片地址
    pil_im = Image.fromarray(uint8(im))
    # resize()缩放到指定比例
    return array(pil_im.resize(sz))


# 图片直方图均衡化
def histeq(im, nbr_bins=256):
    # 计算图像的直方图
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    # cumulative distribution function
    cdf = imhist.cumsum()
    # 归一化
    cdf = 255 * cdf / cdf[-1]
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf

# 实例,封装和解封任意对象到文件系统
def pickle_show():
    # 打开文件并保存,保存为pickle_show.pkl文件,以二进制文件格式保存
    with open('pickle_show.pkl', 'wb') as f:
        obj = "这是一个对象"
        pickle.dump(obj, f)

    # 打开文件并载入
    with open('pickle_show.pkl', 'rb') as f:
        obj = pickle.load(f)
        print(obj)

# 搞事情   读取->灰度->阈值->二值化->降噪->描线->录入->美滋滋
if __name__ == '__main__':
    pickle_show()