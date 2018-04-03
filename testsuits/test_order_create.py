#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import Loginpage
from pageobjects.order_create import Ordercreate

class createorder(unittest.TestCase):
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

    def test_ordercreate(self):

        #初始化登录界面，并登录
        loginpage = Loginpage(self.driver)
        loginpage.type_username('ecs1105')
        loginpage.type_password('1qaz2wsx')
        self.driver.find_element_by_id('submit').click()
        time.sleep(4)
        #初始化订单新建页面
        ordercreatepage = Ordercreate(self.driver)
        ordercreatepage.click_createOrderBtn()
        time.sleep(3)
        ordercreatepage.type_receiverName('张无忌')
        ordercreatepage.type_receiverMobile('14726967584')
        ordercreatepage.type_province('湖南省')
        ordercreatepage.type_city('长沙市')
        ordercreatepage.type_district('岳麓区')
        ordercreatepage.type_receiverAddress('岳麓大道569号')
        ordercreatepage.type_goodsName('自动化测试自动添加商品')
        ordercreatepage.click_confirmCreateOrder()

if __name__=='__main__':
    unittest.main()
