import smtplib

MailServer = smtplib.SMTP("smtp.gmail.com",465)

MailServer.starttls()

MailStatus = MailServer.login("krishkalam2000@gmail.com","krishnapriyan123*")

MailServer.sendmail("krishkalam2000@gmail.com","krishkalam2000@gmail.com","Hi this is boo !")

if (MailStatus):
    print("Mail sent!")
else:
    print("Mail not sent ...")