#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import Loginpage
from pageobjects.order_create_page import Ordercreate
from pageobjects.order_page import OrderPage


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

        companyname = '顺丰'

        #初始化登录界面，并登录
        loginpage = Loginpage(self.driver)
        loginpage.type_login_info('ECS0630', '1qaz2wsx')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        # 切换frame
        frame1 = self.driver.find_element_by_id('container-i')
        self.driver.switch_to_frame(frame1)
        # 页面初始化
        orderpage = OrderPage(self.driver)
        # 点击新增模板按钮
        orderpage.click_add()
        time.sleep(2)
        orderpage.click_Logistics_company()
        time.sleep(3)
        self.driver.find_element_by_xpath('//li[text()="%s"]'%companyname).click()


        time.sleep(5)



if __name__=='__main__':
    unittest.main()
