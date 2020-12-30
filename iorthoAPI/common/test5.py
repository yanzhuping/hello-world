
import os
# dict={}
# dict['name']='yanzhuping'
# print(dict)


# 抽取接口的返回值存储到全局变量字典中


# file_path=os.path.dirname(__file__)
#
# base_dir=os.path.dirname(file_path)
# base_dir = str(base_dir)
# # 对路径的字符串进行替换
# base_dir = base_dir.replace('\\', '/')
#
# file_path=os.path.join(base_dir,'data',dir)
#
# a={}
# a['num1']='yan'
# a['num1']='yan'
#
# print(a)

# #
# selector=".pic-1-4"
# se=selector.split(".")[1]
# print(se)

a='//label[@for="overbiteTwo1" and text()="伸长前牙"]/following-sibling::input'
b=a.find('following-sibling')
print(b)