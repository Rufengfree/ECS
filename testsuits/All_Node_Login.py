#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

# coding=utf-8
import configparser
import unittest
import xlrd
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.login_page import Loginpage


class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()



    def test_login_ecs(self):
        logger = Logger(logger="BasePage").getlog()
        loginpage = Loginpage(self.driver)
        # 这里更改文件路径和名字
        excel = xlrd.open_workbook("D:\\RUFENG\\ECS\\config\\data.xlsx")
        # 指定要读取的sheet
        sheet = excel.sheet_by_name("user_info")

        # 打开Excel对应的sheet页
        sheet = loginpage.open_excel('D:\\RUFENG\\ECS\\config\\data.xlsx','user_info')

        # 读取Sheet页行内容
        nr = sheet.nrows

        for i in range(1, nr):
            rv = sheet.row_values(i)
            node,username, password = rv[0],rv[1], rv[2]
            loginpage.type_login_info(username,password)
            self.driver.find_element_by_id('submit').click()

            def checked():
                if '易打单' == loginpage.get_page_title():
                    self.assertTrue(True)
                    loginpage.skin01_logout()
                    logger.info("%a 节点登录成功" % node)
                elif '易打单 订单管理' == loginpage.get_page_title():
                    self.assertTrue(True)
                    self.driver.find_element_by_xpath('//*[@id="g_header"]/div[1]/div/a[2]/span/span').click()
                    logger.info(" %a节点登录成功" % node)
                else:
                    loginpage.get_windows_img()
                    self.assertTrue(False)

            try:
                if loginpage.is_element_exist('//*[@id="forget_pwd"]') == True:    # 跳过修改密码直接登录
                    self.driver.find_element_by_xpath('//*[@id="forget_pwd"]').click()
                    checked()
                elif loginpage.is_element_exist('//*[@id="forget_pwd"]') == False:
                    checked()


            except BaseException as e:
                self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()