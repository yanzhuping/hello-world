import requests
import logging
import re

def getCookie():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    logging.captureWarnings(True)
    base_url = 'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
    s=requests.session()
    r = s.get(base_url, headers=header, verify=False)
    strr = r.text
    pat1 = r'= {execution: "(.*?)", _eventId:'
    execution = re.findall(pat1, strr)
    par1 = {'username': 'yanry4548', 'password': '333333', 'execution': '%s' % execution[0], '_eventId': 'submit','oginType': '0'}
    r1 = s.request('POST',base_url, headers=header, data=par1, allow_redirects=False, verify=False)
    location = r1.headers['Location']
    r2 = s.request('GET',location, headers=header, allow_redirects=False, verify=False)
    result = r2.headers['Set-Cookie']
    # print(result)
    cookie = {'Cookies':result.split(';')[0]}
    # JSESSIONID=result.split(';')[0]
    # header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    #         'cookie': '%s'%JSESSIONID}
    # print(cookie)

    # jar = requests.cookies.RequestsCookieJar()  # 创建一个Cookie Jar对象
    # # jar.set('49BAC005-7D5B-4231-8CEA-1XXX39XEACD67', 'ckXXXX001')  # 向Cookie Jar对象中添加cookie值
    # jar.set('JSESSIONID', result.split(';')[0])
    # # jar.set('JSESSIONIDSSO', '9D49C76FDXXXXF5B0F294242B44A')
    # s.cookies.update(jar)  # 把cookies追加到Session中
    # print(s.cookies)

    r3 = s.request('GET', location, headers=header, allow_redirects=False, verify=False)
    # print('r3 headers: ', r3.headers)

    url = "https://opm-cas.sh-sit.eainc.com:8443/OPM/login/validatelogin"
    data = {}
    re4 = s.request('post', url, headers=header, data=data, verify=False)


    return s

# getCookie()