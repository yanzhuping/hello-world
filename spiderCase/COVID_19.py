import requests
import time
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

#国内疫情
base_url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab0'

#国外疫情
base_url_f='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab4'

html=requests.get(base_url,headers=header).content.decode('utf8','ignore')
# html=requests.get(base_url,headers=header).text

print(html)
