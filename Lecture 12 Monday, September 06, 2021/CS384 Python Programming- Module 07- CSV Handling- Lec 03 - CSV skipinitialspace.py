import csv
import os
os.system('cls')
# os.system('clear')

with open('people_spaces.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=False)  # Both
    for row in reader:
        print(row)


print("Now setting skipinitialspace as True ")
with open('people_spaces.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)  # Both
    for row in reader:
        print(row)
