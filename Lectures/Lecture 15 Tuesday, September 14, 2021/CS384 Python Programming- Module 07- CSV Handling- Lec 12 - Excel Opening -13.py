from openpyxl.chart import BarChart, Reference
from openpyxl import Workbook
# Adding Chart to Excel File


wb = Workbook()
sheet = wb.active

# Let's create some sample student data
rows = [
    ["Serial_no", "Roll no", "Marks"],
    [1, "1901CB53", 75],
    [2, "1901CB07", 60],
    [3, "1901CB23", 43],
    [4, "1901EE27", 97],
    [5, "1901CB54", 63],
    [6, "1901CB55", 54],
    [7, "1901ME21", 86],
]

for i in rows:
    sheet.append(i)

chart = BarChart()
values = Reference(worksheet=sheet,
                   min_row=1,
                   max_row=8,
                   min_col=2,
                   max_col=3)

chart.add_data(values, titles_from_data=True)
sheet.add_chart(chart, "E2")

wb.save("student_chart.xlsx")
