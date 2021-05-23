import requests
import re
import threading
import urllib3
import xlwt
from time import sleep
import urllib.request
from urllib.request import URLError
import urllib.request

# 临时存放url的列表，作为待爬列表，通过队列遍历
tmplist = []
# 深度字典
depthDict = {}
# 存放爬取到的所有url
urlList = []
# 线程列表
tlist = []

def getHtml(url):
    '''
    获取网页源代码
    :param url:
    :return:
    '''
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    urllib3.disable_warnings()
    res = requests.get(url, headers=header,verify=False,timeout=20)
    text = res.text
    return text

def getPageUrl(url, html=None):
    '''
    获取指定页面的所有url
    :param url:
    :param html:
    :return:
    '''
    ulists = []
    if html == None:
        html = getHtml(url)
    # PATTERN_URl = "<a.*href=\"(https?://.*?)[\"|\'].*"
    # PATTERN_URl = '<a.*?(href=".*?").*?'
    PATTERN_URl = '<a.*?href="(.*?)".*?'
    uList = re.findall(PATTERN_URl, html)

    for ulist_1 in uList:
        if ulist_1.find("http")>-1 or ulist_1.find("http")>-1:
            ##判断host，过滤非iortho的地址
            protocol, s1 = urllib.request.splittype(ulist_1)
            host, s2 = urllib.request.splithost(s1)
            host, port = urllib.request.splitport(host)
            ###
            if host in ['iortho.angelalign.com','www.angelalign.com']:
                ulists.append(ulist_1)
        else:
            #有些href后面的值未带host，进行拼接
            protocol, s1 = urllib.request.splittype(url)
            host, s2 = urllib.request.splithost(s1)
            host, port = urllib.request.splitport(host)
            # print(host)
            # print(protocol)
            if ulist_1.startswith("/"):
                ulist_1=protocol+"://"+host+ulist_1

            else:
                ulist_1 = protocol + "://" + host + "/"+ulist_1
            ulists.append(ulist_1)

    # print("ulist",ulists)
    return ulists

def getSonPageUrl(url):
    '''
    获取子链接页面的所有链接
    :param url:
    :return:
    '''
    subList = getPageUrl(url)
    for u in subList:
        if u not in depthDict:
            depthDict[u] = depthDict[url] + 1
            tmplist.append(u)

def getUrls(depth):
    '''
    当还有待爬网页或者还有运行中的线程一直运行，直到达到指定层次
    :param depth:
    :return:
    '''
    while ((len(tmplist) > 0) or (threading.activeCount() > 1)):
        while len(tmplist) == 0:
            continue
        url = tmplist.pop(0)
        if url not in urlList:
            urlList.append(url)
        print(threading.activeCount(),"\t" * depthDict[url], "#%d:%s" % (depthDict[url], url))
        if depthDict[url] < depth:
            t = threading.Thread(target=getSonPageUrl, args=(url,))
            tlist.append(t)
            t.start()
            sleep(1)
    print(urlList)
    print(len(urlList))

def writeToExcel():
    '''
    写入excel
    :return:
    '''
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('url')
    a=0
    for urlList_1 in urlList:
        worksheet.write(a, 0, label=urlList_1)
        a=a+1

    workbook.save('url.xls')


startUrl = 'https://www.angelalign.com'

if __name__ == '__main__':

    depthDict[startUrl] = 0
    tmplist.append(startUrl)
    getUrls(5)
    writeToExcel()
