import openpyxl

# load workbook and select sheet
workbook = openpyxl.load_workbook('excel_data2.xlsx')
sheet = workbook.active

# write data to sheet
data = [
    ('Apple', 10, 1.99),
    ('Banana', 20, 0.99),
    ('Cherry', 30, 2.99),
    ('Durian', 40, 3.99)
]

for row in data:
    sheet.append(row)

# save workbook
workbook.save('excel_data2.xlsx')
