# Rainbow CSV

import csv
import os
os.system('cls')
# os.system('clear')


with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row)
        print(type(row))
        for i in row:
            print(i)
