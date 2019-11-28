'''
网站地址
url=http://wallhaven.cc/toplist?page=1
https://wallhaven.cc/search?q=id%3A222&ref=fp&page=6
https://wallhaven.cc/search?q=id%3A222&ref=fp&page=5
图片的url
https://w.wallhaven.cc/full/13/wallhaven-13x79v.jpg
https://w.wallhaven.cc/full/dg/wallhaven-dge9ll.jpg
https://w.wallhaven.cc/full/ox/wallhaven-oxlo85.jpg

'''

import re
import requests
import time

page=int(input("请输入需要爬取的页数"))

photo = []  # 存储图片名的前两位
photo1 = []  # 存储图片名

for i in range(1,page):

    # url="http://wallhaven.cc/toplist?page="+str(i)
    url = "http://wallhaven.cc/search?q=id%3A222&ref=fp&page=" + str(i)
    html=requests.get(url)
    strr=html.text

    # print(strr)
    pat1=r'wallhaven.cc/small/(.*?)/'
    pat2=r'wallhaven.cc/wallpaper/fav/(.*?)"'
    photolist=re.findall(pat1,strr)
    photolist1=re.findall(pat2,strr)
    photo.extend(photolist)
    photo1.extend(photolist1)
    # print(photo,photo1)

for i in range(0,len(photo)):

    photourl="http://w.wallhaven.cc/full/"+photo[i]+"/wallhaven-"+photo1[i]+".jpg"
    photoname = "photo"+str(i)
    data = requests.get(photourl).content
    print("正在下载第", i + 1, "张")

    with open("C:\\Users\\Administrator\\Desktop\\tupian\\{}.jpg".format(photoname), "wb") as f:
        f.write(data)

    time.sleep(1)