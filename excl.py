import pandas as pd
import openpyxl

book = openpyxl.load_workbook('都道府県.xlsx')
sheet=book['シート1']
for i in range(1,48):
    print(sheet.cell(row=i,column=1).value)

