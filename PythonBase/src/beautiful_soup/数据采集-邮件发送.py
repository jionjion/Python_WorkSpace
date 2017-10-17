import smtplib
from email.mime.text import MIMEText

if __name__ == "__main__":
    '''简单邮件发送'''
    msg = MIMEText("这是一封测试邮件");                                             # 构建邮件,主要内容                                     
    msg['Subject'] = "邮件主题";                                                  # 邮件主题
    msg['From'] = "1434501783@qq.com";                                          # 邮件发送人
    msg['To'] = "1434501783@qq.com"                                             # 邮件接收人
    s = smtplib.SMTP_SSL(host="smtp.qq.com", port=465);                         # 邮件SSL安全连接建立
    s.login("1434501783@qq.com", "lulyxaugngsfhhad");                           # 登录.用户名,口令
    s.sendmail(msg['From'],msg['To'],msg.as_string());                          # 发送邮件.发送人,接收人,其他参数
    s.quit();