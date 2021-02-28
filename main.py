import smtplib
import datetime
import random


EMAIL = ""
TO = ""
PASSWORD = ""


def send_quote():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=TO,
            msg=f"subject:Today is good day\n\n{quote}\n\nIf it is hostile, kill it",
        )

# # connection = smtplib.SMTP("smtp.gmail.com")
# # connection.close()

with open("quotes.txt") as quotes:
    quotes_lines = quotes.readlines()
    # print(quotes_lines[n])
    quote = random.choice(quotes_lines)


now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 0: #0 = Monday
    send_quote()

#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=3, day=24, hour=4)
# print(date_of_birth)




