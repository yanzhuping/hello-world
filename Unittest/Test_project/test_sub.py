from calculator import *
from StartEnd import *

class Test_sub(Setup_tearDown):
    def test_sub(self):
        j=Math(5,3)
        self.assertEqual(j.sub(),2)
    def test_sub1(self):
        j=Math(8,8)
        self.assertEqual(j.sub(),0)