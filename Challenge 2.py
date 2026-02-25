#a REGEX pattern that validates a student ID format where the string must begin with exactly four letters, followed by exactly four numbers, and nothing else
import re

studentID = input("What's your student ID? ").strip()
if re.search(r"^[a-zA-Z]{4}\d{4}$", studentID):
 print("Valid")
else:
 print("Invalid")