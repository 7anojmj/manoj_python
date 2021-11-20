import csv
import os
os.system('cls')
# os.system('clear')


with open('people_write.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Country', 'Profession'])
    writer.writerow(['Dravid', 'India', 'Cricketer'])
    writer.writerow(['Abraham Lincoln', 'USA', 'President'])

with open('players.csv', 'w', newline='') as file:
    header = ['name', 'country']
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerow({'name': 'Sachin', 'country': 'India'})
    writer.writerow({'name': 'Roger Federer', 'country': 'Switzerland'})
    writer.writerow({'country': 'India', 'name': 'MiraBai Chanu'})
    writer.writerow({'name': 'APJ Abdul Kalam'})
    writer.writerow({'country': 'India', })
