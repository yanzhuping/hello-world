import os
from time import sleep
import random,string
import re
from driver.driver import browser
from selenium.common.exceptions import NoSuchElementException
import types

# dict={
#  "createTime": "select createTime from opm_doctor where crmUserCode='D202009180002'",
#  "modifyTime": "select modifyTime from opm_doctor where crmUserCode='D202009180002'"
# }
#
# for k,v in dict.items():
#     if k == 'createTime':
#       print(v)
#       types.DictType

# def getValueFromComplexDict(dic,json_key,default=None):
    # if not isinstance(dic,dict) or not isinstance(dic, list):
    #     return default
    #
    # def _dealDict(dic):
    #     for k,v in dic.items():
    #         if k == json_key:
    #             return v
    #         else:
    #             if isinstance(v, dict):
    #                 ret_value = getValueFromComplexDict(v, json_key, default=None)
    #                 if ret_value is not default:
    #                     return ret_value
    #             if isinstance(v, list):
    #                 for xv in v:
    #                     if isinstance(xv, dict):
    #                         ret = getValueFromComplexDict(xv, json_key, default=None)
    #                         if ret is not default:
    #                             return ret
    #
    # def _dealList(lis):
    #     for li in lis:
    #         if isinstance(li,str):
    #             pass
    #         if
    # if isinstance(dic , dict):
    #     for k,v in dic.items():
    #         if k == json_key:
    #             return v
    #         else:
    #             if isinstance(v , dict):
    #                 ret = getValueFromComplexDict(v, json_key,default=None)
    #                 if ret is not default:
    #                     return ret
    #             if isinstance(v , list):
    #                 for xv in v:
    #                     if isinstance(xv , dict):
    #                         ret = getValueFromComplexDict(xv, json_key, default=None)
    #                         if ret is not default:
    #                             return ret


# def list_all_dict_1(dict_a,json_key,default=None):
#
#     if isinstance(dict_a, dict):
#         for x in range(len(dict_a)):
#             temp_key = list(dict_a.keys())[x]
#             temp_value = dict_a[temp_key]
#             if temp_key == json_key:
#                 # print(temp_value)
#                 return temp_value
#
#             else:
#                 list_all_dict_1(temp_value,json_key)
#
#
#     elif isinstance(dict_a,list):
#         for list_value in dict_a:
#             list_all_dict_1(list_value,json_key)
#
#     elif isinstance(dict_a,str):
#         pass
#
#     # return default

def list_all_dict_1(dict_a,json_key):
    temp_value_r = None
    if isinstance(dict_a, dict):
        for key in dict_a.keys():
            temp_value = dict_a[key]
            if key == json_key:
                # global temp_value_r
                temp_value_r= temp_value
                break
            else:
                temp_value_r = list_all_dict_1(temp_value,json_key)
    elif isinstance(dict_a,list):
        for list_value in dict_a:
            temp_value_r = list_all_dict_1(list_value,json_key)

    elif isinstance(dict_a,(str,int)):
        pass
    return temp_value_r

if __name__ == '__main__':

    a={
     "caseId": 0,
     "crmCaseCode": "C01001355172",
     "bucketId": 2,
     "oriZip": 1,
     "imgList": [{"attName":"微信图片_20190902092200.jpg",
                  "imgKey":"pic/photo/1602296054987_5e0f1bd8afad6439b4b2267710c92dbc.jpg",
                  "oriMd5":"5e0f1bd8afad6439b4b2267710c92dbc","zipMd5":"5e0f1bd8afad6439b4b2267710c92dbc",
                  "imageInfo":{"ImageWidth":{"value":"720"},"ImageHeight":{"value":"600"}}}]
    }

    check_sql_s={
        "createTime": "select createTime from opm_doctor where crmUserCode='D202009180002'",
        "modifyTime": "select modifyTime from opm_doctor where crmUserCode='D202009180002'"
    }

    b=list_all_dict_1(a, 'imageInfo')
    print(b)
    print(type(b))

