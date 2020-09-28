import requests
import logging
import re

def getCookie():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    logging.captureWarnings(True)
    base_url = 'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
    s=requests.Session()
    r = s.get(base_url, headers=header, verify=False)
    strr = r.text
    pat1 = r'= {execution: "(.*?)", _eventId:'
    execution = re.findall(pat1, strr)
    par1 = {'username': 'yanzp0857', 'password': '111111', 'execution': '%s' % execution[0], '_eventId': 'submit','oginType': '0'}
    r1 = s.request('POST',base_url, headers=header, data=par1, allow_redirects=False, verify=False)
    location = r1.headers['Location']
    print(location)
    r2 = s.request('GET',location, headers=header, allow_redirects=False, verify=False)
    result = r2.headers['Set-Cookie']

    result2=r2.request._cookies._cookies  #这是request中的cookie
    result3=r2.cookies._cookies  #这是response中的cookie
    print(result)
    print(result2)
    print(result3)
    # print(result)
    response_cookie = {'Cookie':result.split(';')[0]}

    JSESSIONID=result.split(';')[0]
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'cookie': '%s'%JSESSIONID}

    pat2=r"name='TGC', value='(.*?)',"
    TGC = re.findall(pat2, str(result2))[0]
    print(TGC)
    requests_cookie={'Cookie':'TGC=%s'%TGC}
    print(requests_cookie)
    s.headers.update(header)

    return s,header



getCookie()