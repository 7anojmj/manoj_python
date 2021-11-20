import csv
import os
os.system('cls')
# os.system('clear')


f = open('people.csv', 'r')

with f:
    reader = csv.reader(f)  # list
    for row in reader:
        print(row[0], row[1], row[2])


print(" vs Dictionary reader")
f = open('people.csv', 'r')

with f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row['Name'], row['Country'], row['Profession'])
