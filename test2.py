import subprocess
import json
import pymysql
import requests
import logging
import re
import urllib3
import numpy as np
# def exam():
#     print("这是主进程")
#     ret, output = subprocess.getstatusoutput("print('这是子进程')")
#     print(ret)
#     print(output)
#     for line in output.split('\n'):
#         if line.startswith('return msg'):
#             shell_data = json.loads(line[10:])
#             print(shell_data)
#
#
# exam()

def selectDataForAPItest(g_config,check_sql_s):
    db = pymysql.Connect(
        host=g_config.get("host_1"), port=3306, user=g_config.get("mysqluser_1"),
        passwd=g_config.get("mysqlpasswd_1"), db=g_config.get("dbname_1"), charset='utf8')
    # 创建一个游标对象，执行数据操作
    cursor = db.cursor()
    selectdata = {}
    for key in check_sql_s.keys():
        print(key + ':' + check_sql_s[key])
        cursor.execute(check_sql_s[key])
        data= cursor.fetchone()
        key_value=data[0]
        selectdata[key]=key_value
    print(selectdata)
    db.close()

    return selectdata

def deleteDraft(g_config):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    logging.captureWarnings(True)
    base_url = 'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
    s = requests.session()
    r = s.get(base_url, headers=header, verify=False)
    strr = r.text
    pat1 = r'= {execution: "(.*?)", _eventId:'
    execution = re.findall(pat1, strr)
    par1 = {'username': 'qinmd8888', 'password': '111111', 'execution': '%s' % execution[0], '_eventId': 'submit',
            'oginType': '0'}
    r1 = s.request('POST', base_url, headers=header, data=par1, allow_redirects=False, verify=False)
    location = r1.headers['Location']
    r2 = s.request('GET', location, headers=header, allow_redirects=False, verify=False)
    result = r2.headers['Set-Cookie']
    cookie = {'Cookies': result.split(';')[0]}

    r3 = s.request('GET', location, headers=header, allow_redirects=False, verify=False)
    # print('r3 headers: ', r3.headers)

    url = "https://opm-cas.sh-sit.eainc.com:8443/OPM/login/validatelogin"
    data = {}
    re4 = s.request('post', url, headers=header, data=data, verify=False)

    db = pymysql.Connect(
        host=g_config.get("host_1"), port=3306, user=g_config.get("mysqluser_1"),
        passwd=g_config.get("mysqlpasswd_1"), db=g_config.get("dbname_1"), charset='utf8')
    cursor = db.cursor()

    sql = "select caseId from opm_case_base where patientName='单米西' and isDelete=0 and crmCaseCode is Null"
    cursor.execute(sql)
    input_name = cursor.fetchone()
    db.close()

    if input_name == '' or input_name is None:
        print("没有草稿")
        pass
    else:
        deleteUrl = 'https://opm-cas.sh-sit.eainc.com:8443/OPM/workbench/deleteDraftCase'
        params = {'draftId': input_name[0],'docCode':'D201812070002','orgCode':'H201704180001,H201012070025,H201012070801','phaseType':1}
        r5 = s.request('delete', deleteUrl, headers=header, params=params, data=data, verify=False)
        print(r5.json())



def rsmat(arbmat):
    """ Convert an arbitrary matrix to a simplest matrix """
    arbmat = arbmat.astype(float)
    row_number, column_number = arbmat.shape
    if row_number == 1:
        if arbmat[0, 0] != 0:
            return (arbmat/arbmat[0, 0])
        else:
            return arbmat
    else:
        rc_number = min(row_number, column_number)
        anarbmat = arbmat.copy()
        r = 0
        for n in range(rc_number):
            s_row = -1
            for i in arbmat[r:row_number, n]:
                s_row += 1
                if abs(i) > 1e-10:
                    anarbmat[r, :] = arbmat[s_row+r, :]
                    for j in range(r, row_number):
                        if j < s_row+r:
                            anarbmat[j+1, :] = arbmat[j, :]
                    arbmat = anarbmat.copy()
            if abs(anarbmat[r, n]) > 1e-10:
                anarbmat[r, :] = anarbmat[r, :] / anarbmat[r, n]
                for i in range(row_number):
                    if i != r:
                        anarbmat[i, :] -= \
                        anarbmat[i, n]*anarbmat[r, :]
            arbmat = anarbmat.copy()
            if abs(arbmat[r, n]) < 1e-10:
                r = r
            else:
                r = r + 1
        for m in range(column_number):
            if abs(arbmat[-1, m]) > 1e-10:
                arbmat[-1, :] = arbmat[-1, :]/arbmat[-1, m]
                for i in range(row_number-1):
                    arbmat[i, :] -= \
                    arbmat[i, m]*arbmat[-1, :]
                break
        return arbmat


if __name__ == '__main__':
    g_config={'host_1':'192.168.37.113','mysqluser_1':'opm_sh_sit','mysqlpasswd_1':'opm_sh_sit','dbname_1':'opm_sh_sit'}
#     check_sql_s={
# 	"createTime": "select createTime from opm_doctor where crmUserCode='D202009180002'",
# 	"modifyTime": "select modifyTime from opm_doctor where crmUserCode='D202009180002'"
# }
    deleteDraft(g_config)
    # selectDataForAPItest(g_config, check_sql_s)

    # # 测试一下
    # a = np.matrix([
    #     [1, 1, 0, -2, -6],
    #     [4, -1, -1, -1, 1],
    #     [3, -1, -1, 0, 3]])
    # a1 = rsmat(a)
    # print(a1)