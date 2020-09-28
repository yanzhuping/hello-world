from iorthoAPI.common.createSession import *
import requests
import logging
import  time
from urllib.parse import urlencode
import json

# s=requests.session()
# # header = {
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
# #         'cache-control': "no-cache",
# #         'Cookie': "JSESSIONID=11D42A3A2227E3ACF07714B4094152B7",
# #        }

s=requests.session()
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        }
logging.captureWarnings(True)  #不报警告
base_url = 'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
r = s.get(base_url, headers=header, verify=False)
strr = r.text
pat1 = r'= {execution: "(.*?)", _eventId:'
execution = re.findall(pat1, strr)

par1 = {'username': 'yanzp0857', 'password': '111111', 'execution': execution[0], '_eventId': 'submit','oginType': '0'}
r1 = s.post(base_url, headers=header, data=par1, allow_redirects=False, verify=False)
location = r1.headers['Location']


r2 = s.request('GET',location, headers=header, allow_redirects=False, verify=False)
result = r2.headers['Set-Cookie']
location = r2.headers['Location']
cookie = {'Cookie':result.split(';')[0]}
JSESSIONID=result.split(';')[0]
# print(JSESSIONID)
# header['Cookie'] = JSESSIONID
# print(header)
# print(s)

r3  = s.request('GET', location, headers=header, allow_redirects=False, verify=False)
# print('r3 headers: ', r3.headers)


url="https://opm-cas.sh-sit.eainc.com:8443/OPM/login/validatelogin"
data={}
re1=s.request('post',url,headers=header,data=data,verify=False)


url="https://opm-cas.sh-sit.eainc.com:8443/OPM/assistant/deleteAssistant"
data={"accountId":"2677"}
re=s.request('DELETE',url,headers=header,params=data,verify=False)


# url="https://opm-cas.sh-sit.eainc.com:8443/OPM/assistant/addAssistant"
# data={"accountType":9,"crmOrgCode":"H201012070002","accountName":"python24"}
# re=s.request('post',url,headers=header,data=data,verify=False)


print(re.text)
print(re.status_code)
print(re.headers)
