import xlrd

def readExcel(fileName,SheetName="Sheet1"):
    data = xlrd.open_workbook(fileName)
    table = data.sheet_by_name(SheetName)

    #获取总行数、总列数
    nrows = table.nrows  #行
    ncols = table.ncols  #列
    # print(nrows,ncols)
    keys=[]
    listApiData = []
    if nrows > 1:
        #获取第一行的内容，列表格式
        keys = table.row_values(0)
        # print(keys)

    #获取每一行的内容，列表格式
        for col in range(1,nrows):
             values = table.row_values(col)
             # print(values)
             # keys，values这两个列表一一对应来组合转换为字典
             # print(zip(keys, values))
             api_dict = dict(zip(keys, values)) #每一行都转换成一个字典
             if api_dict['is_run']!='1':
                 # print(api_dict)
                 listApiData.append(api_dict)

    else:
        print("表格未填写数据")
        return None
    # print(type(listApiData))
    return listApiData

if __name__ == '__main__':
    s = readExcel(r"D:\PrivateCode\hello-world\iorthoAPI\data\apitest.xlsx")
    print(s)


