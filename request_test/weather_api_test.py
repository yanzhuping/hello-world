import requests
from urllib import parse


##传入的城市是中文，则需要进行编码
# data={"city_code":"101010100"}
# city=parse.urlencode(data).encode("utf-8")
city_code="101010100"
url="http://t.weather.sojson.com/api/weather/city/"
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

r=requests.get(url+city_code,headers=header)
print(r.text)
response_data=r.json()

print(response_data["data"]["forecast"][0]["date"])
print(response_data["data"]["forecast"][0]["high"])
print(response_data["data"]["forecast"][0]["low"])
print(response_data["data"]["forecast"][0]["type"])
