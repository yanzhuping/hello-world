from iorthoAPI.common.readExcel import *
from iorthoAPI.common.createSession import *
import json
import requests, string, random
from requests_toolbelt import MultipartEncoder
from iorthoAPI.common.global_vars import *
import os
from time import sleep
import urllib3
from crm_style.function import *
import traceback


def sendRequests(s,apiData):

    urllib3.disable_warnings()

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    try:
        print(global_vars)
        method = apiData["method"]
        url = apiData["url"]
        type = apiData["type"]
        files=apiData['files']
        is_global=apiData["is_global"]


        if apiData["params"] == "":
            par = None
        else:
            par = eval(apiData["params"])

        if apiData["body"] == "":
            body_data = None
        else:
            body_data = eval(apiData["body"])

        if type == "json":
            body = json.dumps(body_data)
        elif type == "form_data":
            body = MultipartEncoder(fields=body_data,boundary='------' + ''.join(random.sample(string.ascii_letters + string.digits, 32)))
            header['content-type'] = body.content_type
        else:
            body = body_data

        if files == "":
            files=None
        else:
            files=eval(apiData['files'])
            for key, value in files.items():
                file_path = os.path.dirname(__file__)
                base_dir = os.path.dirname(file_path)
                base_dir = str(base_dir)
                # 对路径的字符串进行替换
                base_dir = base_dir.replace('\\', '/')
                file_path = os.path.join(base_dir, 'data', value)

                files={key:(value,open(file_path,'rb'))}

        res = s.request(method=method,url=url,data=body,params=par,files=files,headers=header,verify=False,timeout=20)

        sleep(2)
        if is_global == "":
            pass
        else:
            is_global=eval(is_global)
            print(set_global(is_global, res.json()))
        return res

    except Exception as e:
        traceback_info = traceback.format_exc()
        print(traceback_info)
        print(e)

if __name__ == '__main__':

    s = getCookie()
    testData = readExcel(r'D:\work\auto-life\iorthoAPI\data\apitest.xlsx', "create_case")
    print(testData[21])
    response = sendRequests(s,testData[21])
    print(response.json())

    # print(response.text)
    # print(response.status_code)
    # print(response.json())