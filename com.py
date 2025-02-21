from openpyxl import load_workbook

workbook = load_workbook(filename='new_excel.xlsx')
sheet = workbook.active

for row in sheet.iter_rows(min_row=1, max_row=4, min_col=1, max_col=4):
    print(row)

