import datetime as dt
import random
import smtplib

MY_EMAIL = "YOUR_EMAIL@gmail.com"
PASSWORD = "YOUR_PASSWORD"

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

if day_of_week == 3:
    with open("quotes.txt") as file:
        list_of_quotes = file.readlines()
        random_quote = random.choice(list_of_quotes)
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="TO_EMAIL@yahoo.com",
                            msg=f"Subject:Thursday Quote\n\n{random_quote}")

# import smtplib
#
# my_email = ""
# password = "PASSWORD"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:  # connect with our smtp
#     connection.starttls()  # secure the connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="TO_ADDRESS_@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my gmail.")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#

