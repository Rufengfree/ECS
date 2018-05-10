#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

# coding=utf-8

import unittest
import time

from framework import logger
from framework.browser_engine import BrowserEngine
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


    def login(self,username,password):

        loginpage = Loginpage(self.driver)
        loginpage.type_username('username')
        loginpage.type_password('password')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        loginpage.get_windows_img()
        loginpage.get_page_title()
    """
                这里一定要test开通，把测试逻辑代码封装到一个test开头的方法里。
                :return:
                """
    def test_login_ecs(self):
        self.login('ecs0314','1qaz2wsx')
        try:
            if '易打单' == self.get_page_title():
                 self.assertTrue(True)
                loginpage.skin01_logout()
            elif '易打单 订单管理' == self.get_page_title():
                self.assertTrue(True)
                self.driver.find_element_by_xpath('//*[@id="g_header"]/div[1]/div/a[2]/span/span').click()
            else:
                self.get_windows_img()
                self.assertTrue(False)
        except BaseException as e:
            self.assertTrue(False)

    # def test_login_ecs2(self):
    #    loginpage = Loginpage(self.driver)
    #    loginpage.type_username('110140029')
    #   loginpage.type_password('1qaz2wsx')
    # self.driver.find_element_by_id('submit').click()
    #  time.sleep(2)
    # loginpage.get_windows_img()
    #


if __name__ == '__main__':
    unittest.main()