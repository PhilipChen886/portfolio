# import excel
from openpyxl import load_workbook
#path = 'D:/python_projects2/test.xlsx'
wb = load_workbook('test.xlsx')
sheet = wb['Sheet1']

wb.save(filename = 'test.xlsx')         # Save file