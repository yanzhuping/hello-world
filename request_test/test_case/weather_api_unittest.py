import unittest
import requests
from urllib import parse
from time import sleep

class WeatherTest(unittest.TestCase):
    def setUp(self) -> None:
        self.url="http://t.weather.sojson.com/api/weather/city/"
        # self.proxies={"http":"http:localhost"}
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

    def test_weather_beijing(self):
        '''北京天气'''
        city_code="101010100"
        r=requests.get(self.url+city_code,headers=self.header)
        result=r.json()
        #断言
        self.assertEqual(result["status"],200)
        self.assertEqual(result["message"],"success感谢又拍云(upyun.com)提供CDN赞助")
        self.assertEqual(result["cityInfo"]["city"],"北京市")
        sleep(4)

    def test_weather_param_error(self):
        '''参数异常'''
        city_code = "10000000"
        r = requests.get(self.url + city_code, headers=self.header)
        result = r.json()
        # 断言
        self.assertEqual(result["message"], "Request resource not found.")
        sleep(4)

    def test_weather_no_param(self):
        '''参数缺失'''
        r = requests.get(self.url, headers=self.header)
        result = r.json()
        # 断言
        self.assertEqual(result["message"], "Request resource not found.")
        self.assertEqual(result["status"], 404)
        sleep(4)

if __name__ == '__main__':
    unittest.main()

