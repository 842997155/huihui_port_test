"""
    Created By       : PyCharm
    File Name        : OfflineTests
    Author           : wangzhenpeng
    Change Activity  : 2019/3/27 9:07 PM
    Description      : 类目测试用例
"""
import unittest
import  paramunittest

from common import  common
from common.HttpUtils import HttpGet
accessToken_xls=common.get_xls("tokenCase.xlsx","gettoken")



@paramunittest.parametrized(*accessToken_xls)
class AccessToken(unittest.TestCase): # 继承测试父类unittest.TestCase
    def setParameters(self,case_name,url,appid,secret,result,code,expires_in):
        self.case_name=str(case_name)
        self.url=str(url)
        self.appid=str(appid)
        self.secret=str(secret)
        self.result=str(int(result))
        self.code=int(code)
        self.expires_in=int(expires_in)
    def description(self):
        """

        :return:
        """
        self.case_name

    def setUp(self):
        self.token = HttpGet()

    def test_AccessToken(self):
        payload = {'grant_type':'client_credential', 'appid': self.appid,'secret':self.secret}
        self.response=self.token.do_get(self.url,payload).json()
        #self.assertEqual(response['errcode'],40001)
        if self.result == '0':
            self.assertEqual(self.response['expires_in'], self.expires_in)
        if self.result == '1':
            print(self.response['errcode'])
            print(self.code)
            self.assertEqual(self.response['errcode'], self.code)

    def tearDown(self):
        self.token = None
   # def checkResult(self):
        #if self.result =='0':
            #self.assertEqual(self.response['expires_in'], self.expires_in)
        #if self.result == '1':
            #self.assertEqual(self.response['errcode'], self.code)

if __name__ == '__main__':
    #unittest.main()
    print(response)