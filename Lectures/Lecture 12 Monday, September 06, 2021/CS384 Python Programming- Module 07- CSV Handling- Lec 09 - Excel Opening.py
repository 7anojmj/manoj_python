from openpyxl import Workbook
import time

wb = Workbook()
sheet = wb.active

sheet['A1'] = 87
sheet['A2'] = "Devansh"
sheet['A3'] = 41.80
sheet['A4'] = 10

now = time.strftime("%x")
sheet['A5'] = now

wb.save("sample_file.xlsx")
