"""
    Created By       : PyCharm
    File Name        : HttpUtils
    Author           : wangzhenpeng
    Change Activity  : 2019/3/27 9:02 PM
    Description      : http请求模块
"""

import requests


class HttpUtils:
    def __init__(self):
        self.headers = {'Cookie': 'application/json',
                        'Cookie': 'pt_key=AAJcj1TTADB0RVv7fH33l_P_zz0Rz8PYiD74OIp6V1TZwzYV-xDeiow1BkautQUQ5fEnk_9MEcY'}

    def do_get(self, url, params):
        return requests.get(url, headers=self.headers, params=params)


class HttpGet:
    """docstring for Httpget"""

    def __init__(self):
        pass

    def do_get(self, url, params):
        return requests.get(url, params)
