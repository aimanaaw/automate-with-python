import smtplib

# server name and port number
conn = smtplib.SMTP('smtp.gmail.com', 587)
# print(conn)

# ehlo function to start the connection
conn.ehlo()
# tls encryption
conn.starttls()
conn.login('email@gmail.com','password')
# With gmail you would need an application specific password
# Subject header is 3rd argument
conn.sendmail('sendfrom@gmail.com', 'sendto@gmail.com','Subject: So long... \n\n, \nSo long, and thanks for all the fish.\n\n')
# {} black dictionary means the email was sent
conn.quit()
# Disconnected from the smtp server