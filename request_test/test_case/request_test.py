import requests
import logging
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import json
import re

logging.captureWarnings(True)

base_url='https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

s=requests.session()
r=s.get(base_url,headers=header,verify=False)
strr=r.text
pat1=r'= {execution: "(.*?)", _eventId:'
execution=re.findall(pat1,strr)


par1={'username':'yanzp0857','password':'000000','execution':'%s'%execution[0],'_eventId':'submit','oginType':'0'}
r1=s.post(base_url,headers=header,data=par1,allow_redirects=False,verify=False)
# print(r1.content)
# print(r1.status_code)
# print(r1.headers['Location'])
location=r1.headers['Location']
r2=s.get(location,headers=header,allow_redirects=False,verify=False)

result=r2.headers['Set-Cookie']
cookie={'Cookies':result.split(';')[0]}
print(cookie)

par3={'caseId':0,'crmCaseCode':'C01001339297','bucketId':2,'oriZip':1,
      'imgList':'[{"attName":"0a031374d7d7c8272ff3ae624bb405c9.jpg","imgKey":"pic/photo/1595928087305_0a031374d7d7c8272ff3ae624bb405c9.jpg","oriMd5":"0a031374d7d7c8272ff3ae624bb405c9","zipMd5":"0a031374d7d7c8272ff3ae624bb405c9"}]'}
print(type(par3))
url='https://opm-cas.sh-sit.eainc.com:8443/OPM/image/uploadCloudImage'
r3=s.post(url,headers=header,data=par3,cookies=cookie,allow_redirects=False,verify=False)
print(r3.status_code)
print(type(r3.content.decode('utf8')))
print(r3.content.decode('utf8'))