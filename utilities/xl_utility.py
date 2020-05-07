import xlrd

def get_data_from_xl():
    data_file = xlrd.open_workbook("../student-data.xlsx")
    sheet = data_file.sheet_by_name("Sheet1")

    col_count = sheet.ncols
    row_count = sheet.nrows

    list =[]

    for i in range(1, row_count):
        for j in range(col_count):
            list.append(sheet.cell_value(i, j))
    print(list)
    return list
