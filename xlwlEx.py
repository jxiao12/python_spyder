import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("sheet_1")
for i in range(1, 10):
    for j in range(1, i + 1):
        worksheet.write(i - 1, j - 1, i * j)
workbook.save("Example.xls")