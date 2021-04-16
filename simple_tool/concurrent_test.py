#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests, time, json, threading, random
from iorthoAPI.common.createSession import *


class Presstest(object):

    def __init__(self, press_url, account="yanry4548", password="333333"):
        self.press_url = press_url
        self.account = account
        self.password = password
        self.session = getCookie()

    def testinterface(self):
        '''压测接口'''
        data = {"crmUserCode": "D202009180002",
                "userName": "yanry4548",
                "oldPassWord": "333333",
                "newPassWord": "333333",
                "confirmPassWord": "333333"}
        global ERROR_NUM  #出错数
        try:
            html = self.session.post(self.press_url, data=data)
            print(html.text)
            if html.json().get('msg') != '成功':
                print(html.json())
                ERROR_NUM += 1
        except Exception as e:
            print(e)
            ERROR_NUM += 1

    def testonework(self):
        '''一次并发处理单个任务'''
        i = 0
        while i < ONE_WORKER_NUM:  #每个线程的循环次数
            i += 1
            self.testinterface()
        time.sleep(LOOP_SLEEP)  #每次请求的时间间隔

    def run(self):
        '''使用多线程进程并发测试'''
        t1 = time.time()
        Threads = []

        for i in range(THREAD_NUM): #线程数
            t = threading.Thread(target=self.testonework, name="T" + str(i))
            t.setDaemon(True)
            Threads.append(t)

        for t in Threads:
            t.start()
        for t in Threads:
            t.join()
        t2 = time.time()

        print("===============压测结果===================")
        print("URL:", self.press_url)
        print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
        print("总耗时(秒):", t2 - t1)
        print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
        print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
        print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    press_url = 'https://opm-cas.sh-sit.eainc.com:8443/OPM/doctor/updatePassWord'
    account = "yanry4548"
    password = "333333"

    THREAD_NUM = 3  # 并发线程总数
    ONE_WORKER_NUM = 5  # 每个线程的循环次数
    LOOP_SLEEP = 4 # 每次请求时间间隔(秒)
    ERROR_NUM = 0  # 出错数

    obj = Presstest(press_url=press_url, account=account, password=password)
    obj.run()