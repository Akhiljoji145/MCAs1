import os
import openpyxl
folder="."
output_file='output.xlsx'
output_wb=openpyxl.Workbook()
output_sheet=output_wb.active
output_sheet.title = 'Certificate data'

cells = ['B1', 'B2', 'B3', 'B4']

for filename in os.listdir(folder):
    if filename.endswith('.xlsx'):
        file = os.path.join(folder, filename)
        workbook = openpyxl.load_workbook(file)
        values = [workbook.active[cell].value for cell in cells]

        output_sheet.append(values)

output_wb.save(output_file)