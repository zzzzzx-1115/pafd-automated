import email
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime

class Email(object):
    def __init__(self,email_host="smtp.163.com",email_user="furuoo@163.com",email_passwd="WJCLIFERGOIAXOOP"):
        self.email_host = email_host
        self.email_user = email_user
        self.email_passwd = email_passwd
        self.message = None
        self.smtpObj = smtplib.SMTP()


    def _construct_message(self,is_success:bool,content:str):
        self.message = MIMEText(content, 'plain', 'utf-8')
        self.message['From'] = Header("furuoo", 'utf-8')
        self.message['To'] =  Header("blli22", 'utf-8')
        dt = datetime.datetime.today().strftime('%m月%d日 ')
        if is_success:
            self.message['Subject'] = Header(dt+'平安复旦打卡成功提醒 ... ', 'utf-8')
        else:
            self.message['Subject'] = Header(dt+'!!! 失败提醒 ... ', 'utf-8')

    def sendemail(self,is_success:bool,content:str,receivers=['22210240022@m.fudan.edu.cn']):
        self._construct_message(is_success,content)
        try:
            self.smtpObj.connect(self.email_host,25)    # 25 为 SMTP 端口号
            self.smtpObj.login(self.email_user,self.email_passwd)

            self.smtpObj.sendmail(self.email_user, receivers, self.message.as_string())
            # print ("邮件发送成功")
            return True
        except smtplib.SMTPException:
            print ("Error: 无法发送邮件")
            return False


if __name__ == '__main__':
    email = Email()
    email.sendemail(True,'123456789')
