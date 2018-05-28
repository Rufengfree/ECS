#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: rufeng
import HTMLTestRunner
import unittest

from common.report import report
from testsuits.All_Node_Login import LoginCase
from testsuits.Order_Create import Createorder
from testsuits.add_logistic_template import Addtemplate
from testsuits.printandsend import Printsend

suite = unittest.TestSuite()
# 所有节点登录
#suite.addTest(LoginCase('test_login_ecs'))
# 新建订单
suite.addTest(Createorder('test_order_create'))

# 打印发货
suite.addTest(Printsend('test_print_and_send'))
# 添加模板
#suite.addTest(Addtemplate('test_add_template'))


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