import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
wb.get_sheet_names()
#print wb.get_sheet_names()

sheet = wb.get_sheet_by_name('Empty Sheet3')
print type(sheet)

print sheet.title

activesheet = wb.get_active_sheet()
print activesheet
