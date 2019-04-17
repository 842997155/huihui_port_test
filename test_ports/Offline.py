"""
    Created By       : PyCharm
    File Name        : Offline
    Author           : wangzhenpeng
    Change Activity  : 2019/3/27 9:04 PM
    Description      : 要测试的线下门店的接口
"""

from common.HttpUtils import HttpUtils
from common.HttpUtils import HttpGet

# 要测试的接口
class Category:
    def __init__(self):
        self.httpUtils = HttpUtils()

    def query_category(self):
        """查询品类"""
        url = "http://baozhang.jd.com/xxmd/queryCategory"
        return self.httpUtils.do_get(url = url, params = None).json()

    def query_specification_by_category(self, categoryName):
        """根据品类查询规格"""
        url = "http://baozhang.jd.com/xxmd/querySpecificationByCategory/"
        params = {'categoryName':categoryName}
        return self.httpUtils.do_get(url = url, params = params).json()

class Token:
    """docstring for token"""
    def __init__(self):
        self.HttpGet = HttpGet()
    def access_token(self):
        url='https://api.weixin.qq.com/cgi-bin/token'
        payload = {'grant_type':'client_credential', 'appid': 'wx679491ed9d09d574','secret':'a0f5e8367d379aa5b7acbbc43f79f625'}
        return self.HttpGet.do_get(url=url,params=payload).status_code