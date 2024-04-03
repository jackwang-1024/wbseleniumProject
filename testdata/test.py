import os

import xlrd


def ExcelRead():
    # current_path = os.getcwd()
    current_path = "C:\learning\python\wbseleniumProject"
    file = os.path.join(current_path, "testdata\\UI测试用例.xls")
    # file = path + r"\\" + ""
    print(file)
    datafile = xlrd.open_workbook(file)  # 打开Excel
    sheet = datafile.sheet_by_name("Sheet1")  # 按Sheet页名称打开Sheet
    # 获得列表行数
    rows = sheet.nrows
    print(rows)
    # 获得列表列数
    cols = sheet.ncols
    print(cols)

    # 将列头存储到list
    # listTitle = sheet.row_values(0)

    # 获得某列的索引
    # listTitle.index('tenantName')

    # 将数据存储到list
    i = 1
    dictCases = {}
    caseSteps = []
    while i < rows:
        case_no = sheet.cell_value(i, 1)

        if len(case_no) > 0:
            if len(caseSteps) > 0:
                dictCases[0][1]
            caseSteps.clear()
            caseSteps.append(sheet.row_values(i))
            # dictCases[sheet.cell_value(i, 1)] =

        caseSteps.append(sheet.row_values(i))
        # sheet.cell()
        i = i + 1
    # print(listData)
    # print(sheet.cell_value(1,0))
    # a = sheet.col_values(1)
    # a.remove('用例编号')
    # b = list(filter(lambda x: x != "", a))
    # print(b)

if __name__ == '__main__':
    ExcelRead()