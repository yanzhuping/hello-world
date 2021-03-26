from Test_project.calculator import Math
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        J=Math(5,10)
        self.assertEqual(J.add(),12)


    def test_add1(self):
        J=Math(5,10)
        self.assertNotEqual(J.add(),12)


    def tearDown(self):
        print("test end")



if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestMath("test_add1"))  #先后顺序表示用例的执行顺序


    runner=unittest.TextTestRunner()
    runner.run(suite)