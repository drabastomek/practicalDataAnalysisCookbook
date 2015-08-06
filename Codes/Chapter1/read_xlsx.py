import pandas as pd

# name of files to read from
r_filenameXLSX = '../../Data/Chapter1/realEstate_trans.xlsx'
w_filenameXLSX = '../../Data/Chapter1/realEstate_trans.xlsx'

# sheet name(s)
sheets = ['Sacramento']

# open the Excel file
xlsx_file = pd.ExcelFile(r_filenameXLSX)

# read the contents
xlsx_read = {
    sheetName: xlsx_file.parse(sheetName)
        for sheetName in sheets
}

# print the first 10 records for Sacramento
print(xlsx_read['Sacramento'].head(10))

# write to Excel
xlsx_read['Sacramento'] \
    .to_excel(w_filenameXLSX, 'Sacramento', index=False)