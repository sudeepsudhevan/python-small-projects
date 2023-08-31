import pandas
import datetime as dt
from random import randint
import smtplib

MY_EMAIL = "YOUR_EMAIL@gmail.com"
PASSWORD = "YOUR PASSWORD"

now = dt.datetime.now()
today = (now.month, now.day)  # A tuple

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# print(birth_day_dict) key:value

if today in birthday_dict:
    birthday_person = birthday_dict[today]  # value of birthday person from birthday_dict (value = dict["key"])
    # print(birthday_person)
    letter_index = randint(1, 3)

    with open(f"letter_templates/letter_{letter_index}.txt") as letter_file:
        content = letter_file.read()
        # print(content)
        name = birthday_person["name"]
        new_content = content.replace("[NAME]", name)

    # print(new_content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday {name}!\n\n{new_content}")



