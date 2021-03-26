from calculator import *
from StartEnd import *

class Test_add(Setup_tearDown):
    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)
    def test_add1(self):
        j=Math(8,8)
        self.assertEqual(j.add(),16)