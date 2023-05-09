import openpyxl

# load workbook and select sheet
workbook = openpyxl.load_workbook('excel_data.xlsx')
sheet = workbook.active

# read data from sheet
for row in sheet.iter_rows(min_row=2, values_only=True):
    fruit, product, price = row
    print(f"Name: {fruit}, Quantity: {product}, Price: {price}")
    
    
