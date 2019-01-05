import xlrd
workbook = xlrd.open_workbook("Workbook1.xlsx")
#workbook = xlrd.open_workbook('try1.xls', encoding='cp1252')
worksheet = workbook.sheet_by_index(0)
print ("xx")
worksheet.cell(0, 0).value
print(' Detecting data '.center(80, '-'))
print("Rows : ",worksheet.nrows)
print("Columns : ",worksheet.ncols)


print(' Printing First name '.center(80, '-'))
#ranges = range(worksheet.nrows) + 1
for rows in range(1,worksheet.nrows):
	print (worksheet.cell_value(rows,0))
else:
	print(' Complete '.center(80, '-'))