import smtplib

MailServer = smtplib.SMTP("smtp.gmail.com",465)

MailServer.starttls()

MailServer.login("************@gmail.com","***********")

MailStatus = MailServer.sendmail("**********0@gmail.com","*******@gmail.com","Hi this is boo !")

if (MailStatus):
    print("Mail sent!")
else:
    print("Mail not sent ...")
