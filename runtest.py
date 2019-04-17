"""
    Created By       : PyCharm
    File Name        : RunTest
    Author           : wangzhenpeng
    Change Activity  : 2019/3/27 9:08 PM
    Description      : 项目入口
"""
import unittest
import time

from common import HTMLTestRunner


class RunTest:
    def __int__(self):
        pass;

    def create_test_suite(self): # 加载测试用例
        test_suites = unittest.TestSuite()
        # 匹配/test_cases目录下的所有*Tests.py的python文件，并从中匹配出要跑的测试用例
        discover_suites = unittest.defaultTestLoader.discover('./test_cases', pattern='*Tests.py', top_level_dir=None)
        for discover_suite in discover_suites: # 合并不同的文件下的测试用例
            test_suites.addTests(discover_suite)
        return test_suites # 返回测试用例的集合

if __name__ == '__main__':
    run_test = RunTest() # 创建实例
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) # 时间格式
    filename = "./reports/" + now + "_result.html" # 测试报告的文件名
    fp = open(filename, 'wb') # 打开文件（创建文件）返回的是一个流

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：',verbosity=2) # 构造测试TestRunner
    runner.run(run_test.create_test_suite()) # 跑测试用例

    fp.close() # 关闭文件流，必须否则文件为空  生成测试报告