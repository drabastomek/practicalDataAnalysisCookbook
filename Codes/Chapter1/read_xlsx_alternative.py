import openpyxl as oxl

# name of files to read from 
r_filenameXLSX = '../../Data/Chapter1/realEstate_trans.xlsx'

# open the Excel file
xlsx_wb = oxl.load_workbook(filename=r_filenameXLSX)

# names of all the sheets in the workbook
sheets = xlsx_wb.get_sheet_names()

# extract the 'Sacramento' worksheet
xlsx_ws = xlsx_wb[sheets[0]]

# the first row contains labels
labels = [cell.value for cell in xlsx_ws.rows[0]]

# extract the data and store in a list
# each element is a row from the Excel file
data = []
for row in xlsx_ws.rows[1:]:
    data.append([cell.value for cell in row])

# print the prices of the first 10 properties
print(
    [item[labels.index('price')] for item in data[0:10]]
)