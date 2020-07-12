import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("abc@gmail.com", "*********")


    # message
message = "Your accuracy is less than 91% .Try again"


    # sending the mail
s.sendmail("abc@gmail.com", "xyz@gmail.com", message)


    # terminating the session
s.quit()
