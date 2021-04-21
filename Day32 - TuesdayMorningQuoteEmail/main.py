import smtplib
import datetime as dt
import random
import pandas

# Parameters
my_email = "<somesourceemail>"
password = "<somepassword>"
target_email = "<somedestnemail>"
# # stmp donnection information differs based on email provider


# Get quote

with open("quotes.txt") as data_file:
    data = data_file.readlines()
    saying = random.choice(data)

# Check weekday
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    # SMTP has to match source email.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= target_email,
            msg=f"Subject:Tuesday Saying\n\n{saying}"
        )