# coding=utf-8
import xlrd
import sys
import inspect


class Excel(object):

    def __init__(self, excel_path, sheet_name):
        self.excel_file = xlrd.open_workbook(excel_path)
        self.sheet = self.excel_file.sheet_by_name(sheet_name)
        self.sheet_name = self.sheet.name
        self.rows = self.sheet.nrows
        self.cols = self.sheet.ncols

    """返回单元格,计数（0,0）表示第一行，第一列的单元格"""

    def get_sheet_data(self, row, col):
        test_data = self.sheet.cell(row, col).value

    """读取excel,并处理数据返回格式"""

    def read_excel(self):
        list = []
        for row in range(1, self.rows):
            lists = self.sheet.row_values(row)[:self.cols]
            list1 = []
            dict = {}
            for j in range(self.cols):
                list1.append(lists[j].encode('utf-8'))
            print(list1)

            dict['id'] = list1[0].decode('utf-8')
            dict['name'] = list1[1].decode('utf-8')
            dict['describe'] = list1[2].decode('utf-8')
            dict['method'] = list1[3].decode('utf-8')
            dict['url'] = list1[4].decode('utf-8')
            dict['params'] = list1[5].decode('utf-8')
            dict['body'] = list1[6].decode('utf-8')
            dict['type'] = list1[7].decode('utf-8')
            dict['expect_result'] = list1[8].decode('utf-8')
            dict['expect_msg'] = list1[9].decode('utf-8')
            dict['expect_stacode'] = list1[10].decode('utf-8')
            dict['errorCode'] = list1[11].decode('utf-8')
            dict['is_run'] = list1[12].decode('utf-8')

            # print(dict)
            # print dict
            list.append(dict)
        return list

    def get_test_data(self):
        array = self.read_excel()
        return array


if __name__ == "__main__":
    path = r"D:\PrivateCode\hello-world\iorthoAPI\data\apitest.xlsx"
    st_name = 'Sheet1'
    test_data = Excel(path, st_name).read_excel()
    print(test_data)