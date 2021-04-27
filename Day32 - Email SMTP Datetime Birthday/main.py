import datetime as dt
import random
import pandas
import smtplib
##################### Normal Starting Project ######################
PLACEHOLDER = "[NAME]"
MY_EMAIL = "<someemail>"
PASSWORD = "<somepassword>"

data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
today = (now.month, now.day)

birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    birthday_email = birthday_person["email"]

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter_contents = letter_file.read()
        letter_contents = letter_contents.replace(PLACEHOLDER, birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_email,
                msg=f"Subject:Happy Birthday\n\n{letter_contents}"
            )


