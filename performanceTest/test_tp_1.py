from locust import HttpUser, TaskSet, task
from time import ctime
import re
import pymysql
from time import sleep

class AdminLoadTest(TaskSet):
    """
    创建压测类，需要继承TaskSet
    可以添加多个测试任务
    """
    # def login(self):
    #     """
    #     登录实例方法
    #     :return:
    #     """
    #     header = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    #
    #     base_url = 'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
    #     r = self.client.get(base_url, headers=header, verify=False)
    #
    #     strr = r.text
    #     pat1 = r'= {execution: "(.*?)", _eventId:'
    #     execution = re.findall(pat1, strr)
    #     par1 = {'username': 'yanry4548', 'password': '333333', 'execution': '%s' % execution[0], '_eventId': 'submit',
    #             'oginType': '0'}
    #     r1 = self.client.post( base_url, headers=header, data=par1, allow_redirects=False, verify=False)
    #
    #     location = r1.headers['Location']
    #     r2 = self.client.get(location, headers=header, allow_redirects=False, verify=False)
    #
    #     r3 = self.client.get(location, headers=header, allow_redirects=False, verify=False)
    #
    #     url = "https://opm-cas.sh-sit.eainc.com:8443/OPM/login/validatelogin"
    #     data = {}
    #     re4 = self.client.post(url, headers=header, data=data, verify=False)

    # def logout(self):
    #     """
    #     登出实例方法
    #     :return:
    #     """
    #     self.client.get("https://opm-cas.sh-sit.eainc.com:8443/cas/logout?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas")

    # def on_start(self):
    #     """
    #     当任何一个task调度执行之前,
    #     on_start实例方法会被调用
    #     先登录
    #     :return:
    #     """
    #     self.login()

    # def on_stop(self):
    #     """
    #     当任何一个task调度执行之后,
    #     on_stop实例方法会被调用
    #     后登出
    #     :return:
    #     """
    #     self.logout()

    @task
    def pressure_cx(self):
        """
        对投票查询接口压测
        :return:
        """
        self.client.post("/api/web/v1/iortho_forward_interface",
                        {"env": "debug","method": "get",
                         "path": "zmc/queryCaseList",
                         "data":'{"platform":2,"authKey":"9355558b-5ea0-5a58-8702-09797acd80ed"}'
                        }
                         )


class RunLoadTests(HttpUser):
    """
    创建运行压测类
    """
    tasks = [AdminLoadTest]
    min_wait = 3000
    max_wait = 6000
    host = "https://exp-test.angelalign.com"
