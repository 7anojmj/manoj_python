from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

data = (
    (11, 48, 50),
    (81, 30, 82),
    (20, 51, 72),
    (21, 14, 60),
    (28, 41, 49),
    (74, 65, 53),
    ("Peter", 'Andrew', 45.63)
)

for i in data:
    sheet.append(i)
wb.save('appending_values.xlsx')
