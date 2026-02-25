import re

number = input("What's your UK phone number? ").strip()
if re.match(r"07\d{9}", number):
    print("Valid")
else:
    print("Invalid")