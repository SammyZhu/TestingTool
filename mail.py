import smtplib
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# send mails
mail_host = "xxx.com"  # 设置服务器
sender = 'mfg.test@deckers.com'
receiver = 'sammy.zhu@deckers.com'

home = "/Applications/apache-jmeter-5.1.1/report/png/"
with open(home + 'report.html') as f:
    mail_body = f.read()

text = MIMEText(mail_body, 'html', 'utf-8')

message = MIMEMultipart('mixed')
message['From'] = formataddr(["mfg.test@deckers.com", sender])
message['To'] = formataddr(["Digital scrum team", receiver])
message['Subject'] = "Performance Test Report"
message.attach(text)
att1 = MIMEImage(open(home + 'RT_Thread.png', 'rb').read())
att1.add_header('Content-ID', 'RT_Thread')
message.attach(att1)
att2 = MIMEImage(open(home + 'RT_Time.png', 'rb').read())
att2.add_header('Content-ID', 'RT_Time')
message.attach(att2)
att3 = MIMEImage(open(home + 'TPS_Thread.png', 'rb').read())
att3.add_header('Content-ID', 'TPS_Thread')
message.attach(att3)
att4 = MIMEImage(open(home + 'TPS_Time.png', 'rb').read())
att4.add_header('Content-ID', 'TPS_Time')
message.attach(att4)
att5 = MIMEImage(open(home + 'PerfMon.png', 'rb').read())
att5.add_header('Content-ID', 'PerfMon')
message.attach(att5)

try:
    server = smtplib.SMTP()
    server.connect(mail_host)
    server.sendmail(sender, receiver, message.as_string())
    print("Send mail succefully")
except smtplib.SMTPException:
    print("Fail to send mail")
