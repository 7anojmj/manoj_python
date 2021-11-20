# Rainbow CSV

import csv
import os
os.system('cls')
# os.system('clear')


with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row, type(row))
        print("Name:", row[0])
        print("Profession:", row[-1])
        print("Name + Profession:", row[0]+"-"+row[-1])
