import unittest
from ddt import ddt,data,unpack
from iorthoAPI.common.sendRequest import *
from iorthoAPI.common.readExcel import *
from iorthoAPI.common.createSession import *
from time import sleep
from iorthoAPI.common.assertions import Assert_result
from iorthoAPI.common.fun import *


# SheetNameList=["assistant","personal_center","image"]
# testData=[]
# for SheetName in SheetNameList:
#     testData_1 = readExcel(r"D:\PrivateCode\hello-world\iorthoAPI\data\apitest.xlsx",SheetName=SheetName)
#     testData.extend(testData_1)
# # print(testData)

# testData = readExcel(r"D:\PrivateCode\hello-world\iorthoAPI\data\apitest.xlsx",SheetName="image")
testData = readExcel(os.path.join(get_fileBasePath(),'data','apitest.xlsx'),SheetName="image")
@ddt
class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s=getCookie()

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*testData)
    def test_image_api(self,data):
        print(data)
        re = sendRequests(self.s,data)
        # print(re.json())
        Assert_result().assert_result(data,re)
        sleep(0.5)


if __name__ == '__main__':

    unittest.main()