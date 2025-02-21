from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet['A1'] = 'a'
sheet['A2'] = '10'
sheet['B1'] = 'b'
sheet['B2'] = '20'
sheet['C1'] = 'c'
sheet['C2'] = '30'
sheet['D3'] = 'D'

workbook.save(filename='new_excel.xlsx')


