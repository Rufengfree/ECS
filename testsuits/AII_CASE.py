#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: rufeng
import HTMLTestRunner
import unittest

from common.report import report
from testsuits.All_Node_Login import LoginCase
from testsuits.Order_Create import Createorder
from testsuits.printandsend import Printsend

suite = unittest.TestSuite()
suite.addTest(LoginCase('test_login_ecs'))
suite.addTest(Createorder('test_order_create'))
suite.addTest(Printsend('test_print_and_send'))


if __name__ == '__main__':
    # 执行用例
    #runner = unittest.TextTestRunner()
    #runner.run(suite)

    # 实例化测试报告
    re = report()
    report_title = 'All_node_login'
    fp = re.report_exist_statu(report_title)
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"全节点登录测试", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
    fp.close()