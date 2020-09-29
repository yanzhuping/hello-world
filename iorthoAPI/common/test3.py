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

par1 = {'username': 'yanry4548', 'password': '333333', 'execution': execution[0], '_eventId': 'submit','oginType': '0'}
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
data1={}
re1=s.request('post',url,headers=header,data=data1,verify=False)


####################################分隔线##########################################

# url="https://opm-cas.sh-sit.eainc.com:8443/OPM/fastTarget/submitFastTarget"
# data={"paramIn":'{"FTCaseCode":"","docCode":"D202009180002","docName":"严如玉","orgCode":"H201012070002","orgName":"深圳市儿童医院","patientName":"接口提交6","patientSex":1,"patientBirthdate":"1990-01-02","iprTooth":"0,0","extractionTooth":"","stlSource":"2","stlFileId":"","otherCaseId":248364}'}
# re=s.request('post',url,headers=header,data=data,verify=False)

url="https://opm-cas.sh-sit.eainc.com:8443/OPM/fastTarget/uploadAttachment"
params={"paramIn":'{"FTCaseId":0,"FTCaseCode":"","patientName":"rr","attType":"1","attId":-1,"attTag":"1"}'}
files={"stlFile":('test_stl_file_U.stl',open(r'C:\Users\Administrator\Desktop\document\all-files\STL\test_stl_file_U.stl','rb'))}
re=s.request('post',url,headers=header,params=params,files=files,verify=False,timeout=20)
stlId1=re.json()["attId"]




url="https://opm-cas.sh-sit.eainc.com:8443/OPM/fastTarget/uploadAttachment"
params={"paramIn":'{"FTCaseId":0,"FTCaseCode":"","patientName":"rr","attType":"1","attId":-1,"attTag":"2"}'}
files={"stlFile":('test_stl_file_L.stl',open(r'C:\Users\Administrator\Desktop\document\all-files\STL\test_stl_file_L.stl','rb'))}
re3=s.request('post',url,headers=header,params=params,files=files,verify=False,timeout=20)
stlId2=re3.json()["attId"]



url="https://opm-cas.sh-sit.eainc.com:8443/OPM/fastTarget/submitFastTarget"
data={"paramIn":'{"FTCaseCode":"","docCode":"D202009180002","docName":"严如玉","orgCode":"H201012070002","orgName":"深圳市儿童医院","patientName":"接口提交7","patientSex":1,"patientBirthdate":"1990-01-02","iprTooth":"0,0","extractionTooth":"","stlSource":"1","stlFileId":"%d,%d","otherCaseId":""}'%(stlId1,stlId2)}
re=s.request('post',url,headers=header,data=data,verify=False)


print(re.status_code)
print(re.text)
# print(re.headers)
