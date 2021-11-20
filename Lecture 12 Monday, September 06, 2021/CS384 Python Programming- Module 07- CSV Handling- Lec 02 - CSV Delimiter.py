import csv
import os
os.system('cls')
# os.system('clear')


with open('people_hash.csv', 'r') as file:
    reader = csv.reader(file, delimiter='#')
    print(reader)
    for row in reader:
        print(row)
