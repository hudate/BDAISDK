#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests


class BDTOKEN(object):

    def __init__(self, AK, SK):
        self.__AK = AK
        self.__SK = SK

    def get_token(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?'
        data = {"grant_type": 'client_credentials', 'client_id': self.__AK, "client_secret": self.__SK}
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        res = self.bd_request(url=host, data=data, header=headers)
        content = json.loads(res.content.decode('utf-8'))
        if res.status_code == 200:
            token = content['access_token']
            return token

    def bd_request(self, url, data, header={"Content-Type": "application/x-www-form-urlencoded"}):
        print(data)
        while 1:
            q_times = 1
            try:
                res = requests.post(url=url, data=data, headers=header)
                return res
            except Exception as e:
                print("请求错误， 错误原因：%s" % e)
                q_times += 1
                if q_times > 5:
                    print("本次请求失败！请稍后再试！")
                    break
                print("第%s次请求中......" % q_times)


