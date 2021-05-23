import unittest
from unittest import mock
from unittest.mock import patch

from mockTest.payApi import PayApi


class TestPayApi(unittest.TestCase):

    def setUp(self):
        self.pay = PayApi()

    @patch.object(PayApi, 'auth')
    def test_success(self, mock_auth):

        mock_auth.return_value = {'status_code':'200'}
        status = self.pay.pay('1000', '12345', '10000')
        self.assertEqual(status, '支付成功')

    @patch.object(PayApi, 'auth')
    def test_fail(self, mock_auth):
        mock_auth.return_value={'status_code':'500'}
        status = self.pay.pay('1000', '12345', '10000')
        self.assertEqual(status, '支付失败')

    @patch.object(PayApi, 'auth')
    def test_error(self, mock_auth):
        mock_auth.return_value={'status_code':'300'}
        status = self.pay.pay('1000', '12345', '10000')
        self.assertEqual(status, '未知错误')

    @patch.object(PayApi, 'auth')
    def test_exception(self, mock_auth):
        mock_auth.return_value='200'
        status = self.pay.pay('1000', '12345', '10000')
        self.assertEqual(status, 'Error, 服务器异常!')


if __name__ == '__main__':
    unittest.main()