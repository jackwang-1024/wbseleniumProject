import openpyxl
import pytest

from keywords import library
from selenium.webdriver.common.by import By
from time import sleep
from tools.handle_excel import ReadExcel
from tools.handle_request import HandleRequest
# wb = openpyxl.load_workbook(r"C:\learning\python\wbseleniumProject\testdata\新建 XLSX 工作表.xlsx")
# sheet=wb['Sheet1']
# allvaules = list(sheet.values)
# handle_excel = handle_excel.ReadExcel()
allvaules= ReadExcel.read_excel("C:\\learning\\python\\wbseleniumProject\\testdata\\新建 XLSX 工作表.xlsx")

caselists = []
dict1={"id":By.ID,"name":By.NAME}

# library = library.Libray()
# for row in allvaules:
#     # print(row[0])
#     if type(row[0]) == int and row[1] > 0:
#         print(row[3])
#         print(row[4],row[5])
#         if "input" == row[3]:
#             getattr(library,row[3])((row[4],row[5]),row[6])
#         elif "click" == row[3]:
#             getattr(library, row[3])((row[4],row[5]))
#         elif "close" == row[3]:
#             getattr(library,row[3])
#         else:
#             getattr(library, row[3])(row[6])
#         sleep(2)
@pytest.mark.parametrize("case",allvaules)
def test_flow_case(case):
    resp = HandleRequest.run(case)