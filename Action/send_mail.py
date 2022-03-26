import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Action.keyword_action import *

import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

def send_mail():
    mail_host = "smtp.mxhichina.com"  # 设置服务器
    mail_user = "taoxb@fingard.com"  # 用户名
    mail_pass = "txb_1985"  # 口令
    sender = 'taoxb@fingard.com'
    #receivers = ['taoxb@fingard.com','fanek@fingard.com','wangy@fingard.com','chenmy@fingard.com','zhangy@fingard.com','lancs@fingard.com','312639004@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers = ['taoxb@fingard.com','312639004@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("陶信波<taoxb@fingard.com>", 'utf-8')
    message['To'] = ','.join(receivers)
    subject = '自动化测试执行报告'
    message['Subject'] = Header(subject, 'utf-8')
    message["Accept-Language"]="zh-CN"
    message["Accept-Charset"]="ISO-8859-1,utf-8,gbk"
    # 邮件正文内容
    message.attach(MIMEText('最新执行的自动化测试报告，请参阅附件内容！', 'plain', 'utf-8'))


    try:
        # 构造附件0，传送Util目录下的AutoTestLog.log 文件
        att1 = MIMEText(open(parentDirPath + "\\Util\\AutoTestLog.log", 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="AutoTestLog.log"'
        message.attach(att1)
    except Exception as e:
        # 发生其他异常时，打印异常堆栈信息
        print("'Error:Util目录下的AutoTestLog.log 文件'可能不存在", e)
        logging.debug("'Error:Util目录下的AutoTestLog.log 文件'可能不存在" + str(e))

    try:
        # 构造附件1，传送TestScript目录下的AutoTestLog.log 文件
        att1 = MIMEText(open(parentDirPath + "\\TestScript\\AutoTestLog.log", 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="AutoTestLog.log"'
        message.attach(att1)
    except Exception as e:
        # 发生其他异常时，打印异常堆栈信息
        print("'Error:TestScript目录下的AutoTestLog.log 文件'可能不存在", e)
        logging.debug("'Error:TestScript目录下的AutoTestLog.log 文件'可能不存在" + str(e))


    #用函数‘zipDir’把目录下的报错截图文件夹 ScreenCapture 压缩成ScreenCapture.zip
    zipDir(parentDirPath + "\\ScreenCapture", parentDirPath + "\\" + "ScreenCapture.zip")

    # 构造附件2，传送目录下的报错截图压缩包 ScreenCapture.zip
    att2 = MIMEText(open(parentDirPath + "\\ScreenCapture.zip", 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="ScreenCapture.zip"'
    message.attach(att2)


    # 用函数‘zipDir’把目录下的用例文件夹 TestData 压缩成TestData.zip
    zipDir(parentDirPath + "\\TestData", parentDirPath + "\\" + "TestData.zip")

    # 构造附件3，传送目录下的报错截图压缩包 TestData.zip
    att3 = MIMEText(open(parentDirPath + "\\TestData.zip", 'rb').read(), 'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="TestData.zip"'
    message.attach(att3)


    try:
        smtpObj = smtplib.SMTP(mail_host)
        smtpObj.login(mail_user, mail_pass) # 登录邮箱
        smtpObj.sendmail(sender, receivers, message.as_string()) # 发送邮件
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)

if __name__ == "__main__":
    send_mail()