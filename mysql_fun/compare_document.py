import xlrd
import xlwt
import os
import time
import codecs


def Txt_to_Excel(inputTxt,sheetName,start_row,start_col,outputExcel):
    fr = codecs.open(inputTxt,'r')  #读取txt的内容
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet(sheetName)

    line_number = 0#记录有多少行，相当于写入excel时的i，
    row_excel = start_row    #从某一行开始写入
    try:
        for line in fr :
            line_number +=1
            # row_excel +=1
            line = line.strip()
            line = line.split(' ')
            len_line = len(line)#list中每一行有多少个数，相当于写入excel中的j
            col_excel = start_col
            values=['调用方法','接口地址','身份']
            if row_excel == 0:
                for i in range(len(values)):
                    ws.write(0, i, values[i])
            elif row_excel !=0:
                for j in range(len_line):
                    print (line[j])
                    ws.write(row_excel,col_excel,line[j])
                    col_excel +=1
                    wb.save(outputExcel)
            row_excel += 1

    except:
       print ('写入失败！')
    print(os.path.dirname(os.path.abspath(__file__))+'\excel_result.xls')
    return os.path.dirname(os.path.abspath(__file__))+'\excel_result.xls'

def read_excel(ori_path,tar_path,sub_name):#
    success=0        #匹配一致数量
    fail=0           #匹配不一致数量
    origin_xls={} #存储源excel文件
    target_xls={} #比对的excel文件
    wb_ori=xlrd.open_workbook(ori_path) #打开原始文件
    wb_tar=xlrd.open_workbook(tar_path) #打开目标文件

    startime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())    #获取系统当前时间并格式化为格式
    print (startime,' 开始比对...')

    sheet_ori=wb_ori.sheet_by_name(sub_name)   #打开原始文件的目标sheet
    sheet_tar=wb_tar.sheet_by_name(sub_name)   #打开目标文件的目标sheet

    ori_num = 0
    tar_num = 0
    abnormals = []

    if sheet_ori.name==sheet_tar.name:
        #sheet表名
        if sheet_ori.name==sub_name:
        #先将数存入dictionary中dictionary(rows:list)
        #第一行存储表头
        #源表取一行数据与目标表全表进行比对如果表中存在主键可以用主键进行索引
        #数据从excel第2行开始
            for rows in range(0,sheet_ori.nrows):
                orign_list=sheet_ori.row_values(rows) #源表i行数据
                origin_xls[rows]=orign_list     #源表写入字典

            for rows in range(0, sheet_tar.nrows):
                target_list = sheet_tar.row_values(rows)  # 目标表i行数据
                target_xls[rows] = target_list  # 目标表写入字典


            if origin_xls[0]  == target_xls[0]:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 表头一致')
            num = len(origin_xls)    #原表的总行数
            print("源表总行数", num)
            num1 = len(target_xls)   #目标表的总行数
            print("目标表总行数:", num1)

            if num >= num1:
                for ori_num in origin_xls:    #遍历字典
                    print("ori_num:", ori_num)
                    flag='false'          #判断是否一致标志
                    for tar_num in target_xls:
                        if origin_xls[ori_num]==target_xls[tar_num]:
                            flag='true'
                            break              #如果匹配到结果退出循环
                    if flag=='true':           #匹配上结果输出后台日志
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 文件:', ori_path+' '+' row:%d is ok'%(ori_num+1))
                        success+=1
                    else:                      #匹配不上将源表中行记录写入txt
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 文件:', ori_path+' '+' row:%d is different'%(ori_num+1))
                        fail+=1
                        data=origin_xls[ori_num]
                        logstr='文件:', ori_path + ' ' + '【不一致】row<'+str(ori_num)+'>:'+str(data)
                        abnormals.append(logstr)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 【%s】比对结束'%sheet_ori.name)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 总记录数:%d条,一致:%d条,不一致:%d条'%(ori_num+1,success,fail))
                for abnormal in abnormals:
                    print(abnormal)
            else:
                for tar_num in target_xls:
                    flag = 'false'  # 判断是否一致标志
                    for ori_num in origin_xls:
                        if target_xls[tar_num] == origin_xls[ori_num]:
                            flag = 'true'
                            break  # 如果匹配到结果退出循环
                    if flag == 'true':  # 匹配上结果输出后台日志
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 文件: ', tar_path+' '+ ' row:%d is ok' % (tar_num + 1))
                        success += 1
                    else:  # 匹配不上将源表中行记录写入txt
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ ' 文件: ', tar_path+' ' + ' row:%d is different' % (
                                tar_num + 1))
                        fail += 1
                        data = target_xls[tar_num]
                        logstr = '【不一致】row<' + str(tar_num + 1) + '>:' + str(data)
                        abnormals.append(logstr)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 【%s】比对结束' % sheet_tar.name)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 总记录数:%d条,一致:%d条,不一致:%d条'%(tar_num + 1, success, fail))
                for abnormal in abnormals:
                    print(abnormal)


if __name__ == '__main__':

    # ori_path=r'C:\Users\Administrator\Desktop\api_list_3.xlsx'   #原表路径
    ori_path=r'C:\Users\Administrator\Desktop\ft_f_case.xls'   #原表路径
    sheetName = 'Sheet1'  # 需要写入excel中的Sheet2中，可以自己设定
    start_row = 0  # 从第x行开始写
    start_col = 0  # 从第x列开始写
    inputTxt = r'C:\Users\Administrator\Desktop\11.txt'  # 输入文件
    outputExcel = 'excel_result.xls'  # 输出excel文件
    tar_path=r'C:\Users\Administrator\Desktop\ft_f_case_1.xls' #目标表路径
    # tar_path=Txt_to_Excel(inputTxt,sheetName,start_row,start_col,outputExcel) #目标表路径
    time.sleep(4)


    read_excel(ori_path,tar_path,'ft_f_case')