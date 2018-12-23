import smtplib

#content = 'example email stuff here'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()
from_email = 'helloworld.sup13@gmail.com'
from_pwd = 'imfinehbu'
to_email = 'gkranthi.kiran.99@gmail.com'

content = "How's Girl?"

mail.login("helloworld.sup13@gmail.com","imfinehbu")

mail.sendmail("helloworld.sup13@gmail.com","gkranthi.kiran.99@gmail.com",content)

mail.quit()
