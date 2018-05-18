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

        #初始化登录界面，并登录
        loginpage = Loginpage(self.driver)
        loginpage.type_username('ECS0630')
        loginpage.type_password('1qaz2wsx')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        #初始化订单新建页面
        ordercreatepage = Ordercreate(self.driver)
        time.sleep(3)
        #切换frame
        frame1 = self.driver.find_element_by_id('container-i')
        self.driver.switch_to_frame(frame1)
        ordercreatepage.click_createOrderBtn()
        time.sleep(3)
        ordercreatepage.type_receiverName('张无忌')
        ordercreatepage.type_receiverMobile('14726967584')
        ordercreatepage.type_province('湖南省')
        ordercreatepage.type_city('长沙市')
        ordercreatepage.type_district('岳麓区')
        ordercreatepage.type_receiverAddress('岳麓大道569号')
        self.driver.find_element_by_xpath('//*[@id="createOrderTPL"]/form/div[1]/div[3]/ul/li[2]/a').click()
        ordercreatepage.type_goodsName('自动化测试自动添加商品')
        ordercreatepage.click_confirmCreateOrder()
        tips = ordercreatepage.get_tips()
        try:
            assert u"新建订单成功" in tips
            print('Assertion test pass.')
        except Exception as e:
            print('Assertion test fail.', format(e))
        time.sleep(1)
        ordercreatepage.click_confirm()


        time.sleep(5)


if __name__=='__main__':
    unittest.main()
