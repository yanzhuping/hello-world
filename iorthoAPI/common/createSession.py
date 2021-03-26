import requests
import logging
import re
import urllib3

def getCookie():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    logging.captureWarnings(True)
    base_url = 'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
    s=requests.session()
    urllib3.disable_warnings()
    r = s.get(base_url, headers=header, verify=False)
    strr = r.text
    pat1 = r'= {execution: "(.*?)", _eventId:'
    execution = re.findall(pat1, strr)
    par1 = {'username': 'yanry4548', 'password': '333333', 'execution': '%s' % execution[0], '_eventId': 'submit','oginType': '0'}
    r1 = s.request('POST',base_url, headers=header, data=par1, allow_redirects=False, verify=False)
    location = r1.headers['Location']
    r2 = s.request('GET',location, headers=header, allow_redirects=False, verify=False)
    result = r2.headers['Set-Cookie']
    cookie = {'Cookies':result.split(';')[0]}

    r3 = s.request('GET', location, headers=header, allow_redirects=False, verify=False)
    # print('r3 headers: ', r3.headers)

    url = "https://opm-cas.sh-sit.eainc.com:8443/OPM/login/validatelogin"
    data = {}
    re4 = s.request('post', url, headers=header, data=data, verify=False)


    return s

# getCookie()