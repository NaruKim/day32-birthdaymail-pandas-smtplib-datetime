import pandas
import smtplib
import datetime
import random

MAIL = ""
PASS = ""


def change_name(n):
    r = random.randint(1,3)
    with open(f"letter_templates/letter_{r}.txt") as letter_file:
        letter = letter_file.read()

    letter = letter.replace("[NAME]", f"{n}")
    return letter


def send_mail(n):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MAIL, PASS)
        connection.sendmail(
            from_addr=MAIL,
            to_addrs=n['email'],
            msg=f"subject:Happy Birthday\n\n{change_name(n['name'])}"
        )


def open_birthday_data():
    birthday = pandas.read_csv('birthdays.csv')
    birthday = birthday.to_dict(orient="records")
    return birthday
    #[{'name': 'Test', 'email': 'wolfthestrider@naver.com', 'year': 1961, 'month': 12, 'day': 21}]


def date_check(n):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if n['year']==year and n['month']==month and n['day']==day:
        return True
    else:
        return False


def ok():
    to = open_birthday_data()
    for i in to:
        if date_check(i):
            send_mail(i)

ok()





