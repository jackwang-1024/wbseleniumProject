import openpyxl


class ReadExcel:

    @staticmethod
    def read_excel(casePath):
        # wb = openpyxl.load_workbook(r"C:\learning\python\wbseleniumProject\testdata\新建 XLSX 工作表.xlsx")
        wb = openpyxl.load_workbook(casePath)
        sheet = wb['Sheet1']
        all_values = list(sheet.values)
        case_list = []
        case_steps = []
        # case_num = 1
        for i in range(1,3):
            case_steps.clear()
            for row in all_values:
                if type(row[0]) == int and row[0] == i and row[1] > 0:
                    case_steps.append(row)

            case_list.append(case_steps.copy())
        return case_list
