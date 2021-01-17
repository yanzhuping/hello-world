import unittest

class Test1(unittest.TestCase):
    @classmethod #在Test1运行之前做的操作
    def setUpClass(cls) -> None:
        print("class module start test>>>>>>>>")
    @classmethod   #在Test1运行之后做的操作
    def tearDownClass(cls) -> None:
        print("class modlue end test>>>>>>>>")

    def setUp(self):  #在测试用例执行之前做操作
        print("Test1 start")
    # @unittest.skipIf(4>3,"skip test_c")    #如果条件为真，则跳过
    def test_c(self):
        print("test_c")
    # @unittest.skipUnless(0>1,"skip test_b")   #如果条件为假，则跳过
    def test_b(self):
        print("test_b")

    def tearDown(self):   #在测试用例执行之后做操作
        print("test end")

# @unittest.skip("skip Test2")  #直接跳过
class Test2(unittest.TestCase):

    def setUp(self):
        print("Test2 start")

    def test_d(self):
        print("test_d")
    @unittest.expectedFailure   #如设定运行失败
    def test_a(self):
       print("test_a")

    def tearDown(self):
        print("Test2 end!")

if __name__ == '__main__':
    unittest.main()


