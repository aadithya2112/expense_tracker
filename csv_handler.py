import csv
from os.path import exists
import os


# create file expense.csv if does not exist
if not exists('expense.csv') or os.stat("expense.csv").st_size == 0:
    with open('expense.csv', 'w', newline='') as csvfile:
        fieldnames = ['Year', 'Month', 'Water', 'Phone', 'Electric', 'Groceries', 'Housing', 'Automotive', 'Tithes', 'Misc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def add_record(record):
    with open('expense.csv', 'a', newline='') as csvfile:
        print("Record in add_record: ", record)
        writer = csv.writer(csvfile)
        writer.writerow(record)

    

def view_records():
    with open('expense.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)


