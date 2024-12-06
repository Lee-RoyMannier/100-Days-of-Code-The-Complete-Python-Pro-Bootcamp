##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = "XXXXX"
PASSWORD = "XXXXXX"

# Importation des csv des dates d'anniversaires
birthday_dates = pd.read_csv(
    "birthday/birthdays.csv")

birthday = {(b.month, b.day): [b.email, b["name"]]
            for (index, b) in birthday_dates.iterrows()}
models_letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
actual_date = dt.datetime(year=2024, month=6, day=22)
actual_date = (actual_date.month, actual_date.day)

birthday_person = birthday.get(actual_date, "not_today")
if birthday_person != "not_today":
    random_letter = random.choice(models_letter)
    try:
        with open(f"birthday/letter_templates/{random_letter}", "r") as letter:
            model = letter.readlines()
    except FileNotFoundError:
        print("Model non trouvé")
    else:
        for i in range(0, len(model)):
            if "[NAME]" in model[i]:
                model[i] = "".join(model[i].replace(
                    "[NAME]", birthday_person[1]))
            new_model = "".join(model)
        with smtplib.SMTP_SSL("smtp.gmail.com") as mail:
            mail.login(MY_EMAIL, PASSWORD)
            mail.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person[0],
                msg=f"Subject:Happy Birthday!! \n\n {new_model}"
            )
