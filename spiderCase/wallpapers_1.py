#第一页比较特殊 http://www.netbian.com/meinv/index.htm  ，如果写成index_1,，会导致404，所以后续需要特别处理第一页
# http://www.netbian.com/meinv/index_2.htm

import re
import requests
import time

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
photo_urls=[]
page=int(input("请输入需要爬取的页数:"))

for i in range(1,page+1):
    if i==1:
        base_url = "http://www.netbian.com/meinv/index.htm"
    else:
        base_url="http://www.netbian.com/meinv/index_"+str(i)+".htm"
    html=requests.get(base_url,headers=header).content.decode('gb18030','ignore')

    pat=r'<img src="(.*?)" alt'
    result=re.findall(pat,html)
    photo_urls.extend(result)

for i in range(0,len(photo_urls)):
    photo_url=photo_urls[i]
    data=requests.get(photo_url,headers=header).content

    print("正在下载第"+str(i+1)+"张")
    f=open(r"C:\Users\Administrator\Desktop\tupian\{}.jpg".format(i+1),"wb")
    f.write(data)

    time.sleep(0.5)

print("下载结束")