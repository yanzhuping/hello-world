import unittest

class Assert_result(unittest.TestCase):
    def assert_result(self,data,re):

        if data["expect_result"] == '':
            pass
        else:
            expect_result = eval(data["expect_result"].split(":")[1])
            try:
                self.assertEqual(re.json()["status"], expect_result, "返回错误,实际结果是%s" % re.json()["status"])
            except:
                self.assertEqual(re.json()["state"], expect_result, "返回错误,实际结果是%s" % re.json()["state"])

        if data["expect_msg"] == '':
            pass
        else:
            expect_msg = eval(data["expect_msg"].split(":")[1])
            self.assertEqual(re.json()["msg"], expect_msg, "返回错误,实际结果是%s"%re.json()["msg"])

        if data["errorCode"] == '':
            pass
        else:
            expect_msg = eval(data["errorCode"].split(":")[1])
            self.assertEqual(re.json()["errorCode"], expect_msg, "返回错误,实际结果是%s"%re.json()["errorCode"])

        self.assertEqual(re.status_code, int(data['expect_stacode']), "返回错误,实际结果是%s" % re.status_code)

