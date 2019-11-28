#爬取贴吧java吧的信息


from lxml import html
etree=html.etree
import requests

class JavaTieba():
    '''爬取java吧中的一些图片'''
    def __init__(self):
        self.teibaName="java"
        self.beginPage=1
        self.endPage=3
        self.baseurl="http://tieba.baidu.com/f?"    #这是网站的地址
        self.header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.fileName=1

    def tiebaUrl(self):
        self.loadPage(self.baseurl)

    def loadPage(self,url):
        for page in range(self.beginPage,self.endPage+1):
            pn=(page-1)*50
            param={"kw":self.teibaName,"pn":pn}
            data=requests.get(url,params=param,headers=self.header).text
            html=etree.HTML(data)
            links=html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
            # print(links)
            for link in links:
                url1="http://tieba.baidu.com"+link #这是条目的地址
                # print(url1)
                self.loadphoto(url1)

    def loadphoto(self,url1):
        data1 = requests.get(url1,headers=self.header).text
        # print(data1)
        html1 = etree.HTML(data1)
        photolinks = html1.xpath('//img[@class="BDE_Image"]/@src')
        # print(photolinks)
        for photolink in photolinks:
            self.writeImage(photolink)

    def writeImage(self,url3):
        data2=requests.get(url3,headers=self.header).content
        print("正在下载第"+str(self.fileName)+"张")
        f=open(r"C:\Users\Administrator\Desktop\tiebajava\\"+str(self.fileName)+".jpg","wb")
        f.write(data2)
        f.close()
        self.fileName=self.fileName+1

if __name__ == '__main__':
    spider=JavaTieba()
    spider.tiebaUrl()



