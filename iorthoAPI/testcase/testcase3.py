import unittest
from ddt import ddt,data,unpack
from iorthoAPI.common.sendRequest import *
from iorthoAPI.common.readExcel import *
from iorthoAPI.common.createSession import *
from time import sleep
from iorthoAPI.common.assertions import Assert_result
from iorthoAPI.common.fun import *


testData = readExcel(os.path.join(get_fileBasePath(),'data','apitest.xlsx'),SheetName='assistant')
# print(testData)

@ddt
class Test3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s=getCookie()

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*testData)
    def test_assistant_api(self,data):
        print(data)
        re = sendRequests(self.s,data)
        # print(re.json())
        Assert_result().assert_result(data,re)
        sleep(0.5)


if __name__ == '__main__':

    unittest.main()