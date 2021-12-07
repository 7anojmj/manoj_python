import csv
import os
os.system('cls')
# os.system('clear')

with open('people_write.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Country', 'Profession'])
    writer.writerow(['Dravid', 'India', 'Cricketer'])
    writer.writerow(['Abraham Lincoln', 'USA', 'President'])
