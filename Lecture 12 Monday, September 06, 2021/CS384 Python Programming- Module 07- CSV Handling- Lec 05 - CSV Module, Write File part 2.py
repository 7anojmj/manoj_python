import csv
import os
os.system('cls')
# os.system('clear')


csv_rowlist = [
    ['Name', 'Country', 'Profession'],
    ['Dravid', 'India', 'Cricketer'],
    ['Abraham Lincoln', 'USA', 'President']
]  # List of List
with open('people_write_multiple.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='#')
    writer.writerows(csv_rowlist)
