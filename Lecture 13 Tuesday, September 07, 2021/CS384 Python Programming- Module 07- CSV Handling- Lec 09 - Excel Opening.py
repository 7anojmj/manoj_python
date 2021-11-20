from openpyxl import Workbook
import time

wb = Workbook()
Sheet1 = wb.active

Sheet1['A1'] = 87
Sheet1['E5'] = "PYTHON EXCEL"
Sheet1['A2'] = "CS384"
Sheet1['A3'] = 41.80
Sheet1['A4'] = 10

now = time.strftime("%x")
Sheet1['A5'] = now

wb.save("sample_file.xlsx")
