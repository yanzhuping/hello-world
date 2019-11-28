import json
import re
import time
import html

import requests
import yaml

global appkey
global user


def __init__(self):
    global api_key, user_id
    with open('_config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.load(f)

    apikey = config.get('api_key')
    userId = config.get('user_id')
    api_key = apikey
    user_id = userId


'''
Aikf机器人接口
'''


def getResponseAikf(msg):
    t = str(int(round(time.time() * 1000)))
    url = "http://www.aikf.com/ask/getAnswer.htm?reqtype=1&tenantId=e1acc141f18a4f48922155ce2e178a7d&ques=" + msg + "&_=" + t
    response = requests.get(url).json()
    answer = response['text']['content']
    dr = re.compile(r'<[^>]+>', re.S)
    answer = dr.sub('', answer)
    print(answer)
    return html.unescape(answer)


'''
图灵机器人接口
'''


def getResponseTuling(msg):
    url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": "imageUrl"
            }
        },
        "userInfo": {
            "apiKey": api_key,
            "userId": user_id
        }
    }
    data = json.dumps(data)
    response = requests.post(url, data).json()
    return response['results'][0]['values']['text']
