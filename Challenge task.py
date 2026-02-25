# Create a brand new script called read_contacts.py. Using csv.DictReader, write a short script that opens contacts.csv, reads the rows, and prints out a nicely formatted string for each person. Instead of referencing the array with numbers, we can use DictReader to address against the dictionary element
import csv

with open("contacts.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old and lives in {row['city']}.")