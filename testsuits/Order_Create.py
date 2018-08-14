#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import Loginpage
from pageobjects.order_create_page import Ordercreate

class Createorder(unittest.TestCase):
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

    def test_order_create(self):

        # 初始化登录界面，并登录
        loginpage = Loginpage(self.driver)
        sheet=loginpage.open_excel('D:\\RUFENG\\ECS\\config\\data.xlsx','user_info')
        nr = sheet.nrows
        for i in range(1, 2):
            rv = sheet.row_values(i)
            username, password = rv[1], rv[2]
            loginpage.login(username,password) # 登录
            ordercreate = Ordercreate(self.driver)
            ordermsg = ordercreate.open_excel('D:\\RUFENG\\ECS\\config\\data.xlsx','ordermsg').row_values(1) # 读取订单数据
            ordercreate.skin01_order_create(ordermsg) # 新建订单
            # 跳出frame
            self.driver.switch_to.default_content()
            # 退出登录
            loginpage.skin01_logout()


if __name__=='__main__':
    unittest.main()
