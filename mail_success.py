import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("abc@gmail.com", "**********")


    # message
message_success = "Achieved your desired accuracy without tweeking . Congrats "


    # sending the mail
s.sendmail("abc@gmail.com", "xyz@gmail.com", message_success)


    # terminating the session
s.quit()
