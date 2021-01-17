from iorthoAPI.common.createSession import *
import requests
import logging
from urllib.parse import urlencode
import json

s=requests.session()
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Cookie': "JSESSIONID=945D2A45F4E0C2A219C30B8E16B8EC6A"
}


# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
# logging.captureWarnings(True)
# base_url = 'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
# s=requests.Session()
# r = s.get(base_url, headers=header, verify=False)
# strr = r.text
# pat1 = r'= {execution: "(.*?)", _eventId:'
# execution = re.findall(pat1, strr)
# par1 = {'username': 'yanzp0857', 'password': '111111', 'execution': '%s' % execution[0], '_eventId': 'submit','oginType': '0'}
# r1 = s.request('POST',base_url, headers=header, data=par1, allow_redirects=False, verify=False)
# location = r1.headers['Location']
# r2 = s.request('GET',location, headers=header, allow_redirects=False, verify=False)
# result = r2.headers['Set-Cookie']
# cookie = {'Cookie':result.split(';')[0]}
# JSESSIONID=result.split(';')[0]
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
#         'Cookie': '%s'%JSESSIONID
#         }
# print(headers)


# url='https://opm-cas.sh-sit.eainc.com:8443/OPM/assistant/queryAssistantList'   #查询助理接口

url='https://opm-cas.sh-sit.eainc.com:8443/OPM/ec_account/queryDocInfo?docCode=D201811210001'

re=s.request('GET',url,headers=headers,verify=False)



print(re.json())