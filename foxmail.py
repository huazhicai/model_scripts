"""Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。"""

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'caizhihua@lsrobot.vip' or input('From: ')
password = 'Listenrobot' or input('Password: ')
to_addr = ['936844218@qq.com'] or input('To: ')
smtp_server = 'smtp.exmail.qq.com' or input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


===============================================================================

# coding:utf-8
import smtplib
from email.mime.text import MIMEText

# 要发给谁
mailto_list = ["caizhihua@lsrobot.vip"]

# 设置服务器，用户名、口令以及邮箱的后缀
mail_host = "smtp.163.com"
mail_user = "huazhicai110@163.com"
mail_passwd = "huazhicai110"
mail_postfix = "163.com"

# 发送邮件
def send_mail(sub, content, to_list=mailto_list):
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ",".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_passwd)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False
