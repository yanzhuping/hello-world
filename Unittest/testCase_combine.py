from Test_project.calculator import Math
import unittest

class Test_StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        print("test start")

    def tearDown(self) -> None:
        print("test end")

class Testadd(Test_StartEnd):
    def test_add(self):
        j=Math(10,5)
        self.assertEqual(j.add(),15)

class Testsub(Test_StartEnd):
    def test_sub(self):
        i=Math(7,5)
        self.assertEqual(i.sub(),2)

if __name__ == '__main__':
    unittest.main()