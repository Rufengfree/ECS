#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

import time
import os
import HTMLTestRunner

#项目路劲
from framework.logger import Logger


class root_xpath():

    def get_root_path(self):
        root_path = r'D:\RUFENG\ECS'
        return root_path


#测试报告格式化
class report():


    logger = Logger(logger='report').getlog()

    def get_report_path(self):
        dir = r'D:\RUFENG\ECS'
        report_path = dir + '/test_report'
        return report_path

    def report_exist_statu(self,report_title):
        report_path = self.get_report_path()
        # 获取系统当前时间
        month = time.strftime("%m", time.localtime(time.time()))
        day = time.strftime("%d", time.localtime(time.time()))
        report_name = time.strftime("%H_%M_%S", time.localtime(time.time()))
        report_path = report_path + r'/' + month + '月' + r'/' + day+'日'
        report_statu = os.path.exists(report_path)
        # os.makedirs(report_path)
        if report_statu==False:
            os.makedirs(report_path)
        report_path = report_path + '/' +report_name + '-' +report_title+'.html'
        fp = open(report_path, "wb")
        self.logger.info('Report writing success !')
        return fp