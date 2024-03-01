import re

string = input("Enter a string: ")

def phone_check(string):
    pattern = r'^(?:\+7|8)\d{10}$'
    if re.match(pattern, string):
        return True
    else:
        return False

check = phone_check(string)
if check:
    print("It is a phone number.")
else:
    print("It is not a phone number.")
