from openpyxl import load_workbook

workbook = load_workbook(filename='new_excel.xlsx')
sheet = workbook.active

print(sheet['A1'].value)
print(sheet['B1'].value)
print(sheet['C2'].value)
print(sheet['D1'].value)


