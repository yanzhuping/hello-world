import unittest
from iorthoAPI.common.global_vars import *
from jsonschema import validate
from crm_style.function import *
import datetime

class Assert_result(unittest.TestCase):
    '''
    校验返回的msg
    校验返回的错误码
    校验返回的状态码
    校验请求状态码
    校验返回数据的格式
    校验返回值中的某个值与数据库中的值一致
    ...未完待续
    '''
    def assert_result(self,data,res):

        #校验返回的status
        if data["expect_result"] == '':
            pass
        else:
            expect_result = eval(data["expect_result"].split(":")[1])
            try:
                self.assertEqual(res.json()["status"], expect_result, "返回错误,实际结果是%s" % res.json()["status"])
            except:
                self.assertEqual(res.json()["state"], expect_result, "返回错误,实际结果是%s" % res.json()["state"])

        #校验返回的msg
        if data["expect_msg"] == '':
            pass
        else:
            expect_msg = eval(data["expect_msg"].split(":")[1])
            self.assertEqual(res.json()["msg"], expect_msg, "返回错误,实际结果是%s"%res.json()["msg"])

        #校验返回的错误码
        if data["errorCode"] == '':
            pass
        else:
            expect_msg = eval(data["errorCode"].split(":")[1])
            self.assertEqual(res.json()["errorCode"], expect_msg, "返回错误,实际结果是%s"%res.json()["errorCode"])

        #校验stacode，如200,400......
        self.assertEqual(res.status_code, int(data['expect_stacode']), "返回错误,实际结果是%s" % res.status_code)

        #校验返回值的数据格式
        if data['schema']=="":
            pass
        else:
            schema=eval(data["schema"])
            validate(instance=res.json(),schema=schema)

        #校验数据库中查询的某个数据与接口返回的数据一致
        if data['check_sql_s'] == "":
            pass
        else:
            check_sql_s=eval(data['check_sql_s'])
            g_config={'host_1': '192.168.37.113','mysqluser_1': 'opm_sh_sit','mysqlpasswd_1': 'opm_sh_sit','dbname_1': 'opm_sh_sit'}
            selectdata=selectDataForAPItest(g_config,check_sql_s)

            print("数据库查询返回的字典:",selectdata)
            for key in selectdata.keys():
                #从数据库中查到的值
                value1=selectdata[key]
                print(type(value1))
                # value2是从接口的返回值拿到的指定键的值
                value2 = getValueFromComplexDict(res.json(), key)

                #处理时间类型的数据
                if isinstance(value1,datetime.datetime):
                    value1=value1.strftime("%Y-%m-%d %H:%M:%S")
                    print("value1:",value1)
                    value2 = value2.split('.')[0]
                    print("value2:",value2)

                self.assertEqual(value2, value1, "返回结果错误，实际结果是%s"%value1)


