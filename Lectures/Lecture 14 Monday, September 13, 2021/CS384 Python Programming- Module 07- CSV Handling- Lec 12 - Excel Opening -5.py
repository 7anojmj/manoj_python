from datetime import datetime
from openpyxl import load_workbook
# Load the workbook demo.xlsx
wb = load_workbook(r"demo.xlsx")

# Select the current active sheet
sheet = wb.active
now = datetime.now()
date_time = now.strftime("%d.%m.%Y")
sheet.title = date_time
wb.save("demo.xlsx")
