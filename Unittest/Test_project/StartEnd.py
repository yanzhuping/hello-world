import unittest

class Setup_tearDown(unittest.TestCase):
    def setUp(self) -> None:
        print("satr test")

    def tearDown(self) -> None:
        print("test end")
