import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import json

base_url='http://httpbin.org'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

#各种请求类型
# r=requests.get(base_url+'/get')
# print(r.status_code)
#
# r=requests.post(base_url+'/post')
# print(r.status_code)
#
# r=requests.put(base_url+'/put')
# print(r.status_code)
#
# r=requests.delete(base_url+'/delete')
# print(r.status_code)

# param_data={'user':'zxw','password':'6666'}
# r=requests.get(base_url+'/get',params=param_data)
# print(r.url)
# print(r.status_code)


# form_data={'user':'zxw','password':'6666'}
# r=requests.post(base_url+'/post',headers=header,data=form_data)
# print(type(r))
# print(r.text)
# print(r.json())


#爬取知乎页面，如果不加请求头，将会请求失败
# r=requests.get('http://zhihu.com/explore',headers=header)
# print(r.text)


#设置cookies，超时设置
# cookie={'user':'51zxw'}
# r=requests.get(base_url+'/cookies',cookies=cookie,timeout=5)
# print(r.text)


#获取cookies
# r=requests.get('http://www.baidu.com')
# print(r.cookies)
# print(type(r.cookies))
# for key,value in r.cookies.items():
#     print(key+":"+value)

#post请求上传文件
# file={'file':open(r'C:\Users\admin\Desktop\photos\001.jpg','rb')}
# r=requests.post(base_url+'/post',files=file)
# print(r.text)

#session会话,接口依赖

#>>>错误的用法
# r=requests.get(base_url+'/cookies/set/yan/51zxw')
# print(r.text)
#
# r=requests.get(base_url+'/cookies')
# print(r.text)

#>>>正确的用法
# s=requests.Session()
#
# r=s.get(base_url+'/cookies/set/yan/51zxw')
# print(r.text)
#
# r=s.get(base_url+'/cookies')
# print(r.text)


#证书认证
# r=requests.get('https://www.12306.cn')
# # r=requests.get('https://www.12306.cn',verify=False)
# print(r.text)


#代理设置
# proxies={'http':'http://1.196.161.203'}
# r=requests.get(base_url+'/get',proxies=proxies)
# print(r.text)

#身份认证-basic-auth
# r=requests.get(base_url+'/basic-auth/yan/123456',auth=HTTPBasicAuth('yan','123456'))
# print(r.text)
# print(r.status_code)

#身份认证-basic-digesauth
# r=requests.get(base_url+'/digest-auth/auth/yan/123456',auth=HTTPDigestAuth('yan','123456'))
# print(r.text)
# print(r.status_code)

#流式请求
r=requests.get(base_url+'/stream/10',stream=True)
if r.encoding is None:
    r.encoding='utf-8'

print(type(r))

for line in r.iter_lines(decode_unicode=True):
    if line:
        data=json.loads(line)
        print(data)
        print(data['id'])