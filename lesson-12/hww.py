######### 1 calculating age from birthdate

from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    months = (today.month - birth_date.month) % 12
    days = (today - birth_date.replace(year=today.year)).days
    return years, months, days

######### 2 calculating days until next birthday

def days_until_birthday(birthdate):
    today = datetime.today()
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    return (next_birthday - today).days

######### 3 meeting scheduler

def schedule_meeting(start_time, duration):
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end = start + duration
    return end.strftime("%Y-%m-%d %H:%M")

######### 4 timezone converter

import pytz

def convert_timezone(date_str, from_tz, to_tz):
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    local_time = from_zone.localize(datetime.strptime(date_str, "%Y-%m-%d %H:%M"))
    return local_time.astimezone(to_zone).strftime("%Y-%m-%d %H:%M %Z")

######### 5 countdown timer

import time

def countdown_timer(target_time):
    target = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
    while True:
        remaining = target - datetime.now()
        if remaining.total_seconds() <= 0:
            print("Time's up!")
            break
        print(f"Time remaining: {remaining}", end="\r")
        time.sleep(1)

######### 6 email validator

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

######### 7 phone number formatter

def format_phone_number(number):
    return f"({number[:3]}) {number[3:6]}-{number[6:]}"

######### 8 password strength checker

def check_password_strength(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

######### 9 word finder in text

def find_word_occurrences(text, word):
    return text.lower().split().count(word.lower())

######### 10 extracting dates from text

def extract_dates(text):
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    return re.findall(pattern, text)

#########test 

if __name__ == "__main__":
    print("Age Calculator:", calculate_age("2000-05-15"))
    print("Days Until Next Birthday:", days_until_birthday("2000-05-15"))
    print("Meeting Scheduler:", schedule_meeting("2024-03-27 14:30", timedelta(hours=2)))
    print("Timezone Converter:", convert_timezone("2024-03-27 14:30", "UTC", "US/Pacific"))
    countdown_timer("2024-03-27 14:35:00")
    print("Email Validator:", validate_email("test@example.com"))
    print("Phone Formatter:", format_phone_number("1234567890"))
    print("Password Strength:", check_password_strength("StrongP@ss1"))
    print("Word Finder:", find_word_occurrences("This is a test. Test again.", "test"))
    print("Date Extractor:", extract_dates("Today is 2024-03-27 and tomorrow is 2024-03-28."))
