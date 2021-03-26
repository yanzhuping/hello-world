import unittest
from ddt import ddt,data,unpack
from iorthoAPI.common.sendRequest import *
from iorthoAPI.common.readExcel import *
from iorthoAPI.common.createSession import *
from time import sleep
from iorthoAPI.common.assertions import Assert_result
from iorthoAPI.common.fun import *


testData = readExcel(os.path.join(get_fileBasePath(),'data','apitest.xlsx'),SheetName='personal_center')
# print(testData)

@ddt
class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s=getCookie()

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*testData)
    def test_personal_center_api(self,data):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(data)
        res = sendRequests(self.s,data)
        # print(res.json())
        Assert_result().assert_result(data,res)

        sleep(0.5)


if __name__ == '__main__':

    unittest.main()