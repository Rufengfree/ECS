#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import Loginpage
from pageobjects.order_create import Ordercreate
from  pageobjects.order_page import OrderPage

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
        loginpage.type_username('ECS0630')
        loginpage.type_password('1qaz2wsx')
        self.driver.find_element_by_id('submit').click()

        time.sleep(3)
        # 定义一个指定的订单
        add = '广东省深圳市福田区自动化测试地址'
        tem = '顺丰热敏210mm'
        # 切换到当前frame
        frame1 = self.driver.find_element_by_id('container-i')
        self.driver.switch_to_frame(frame1)
        time.sleep(3)

        # 页面实例化
        orderpage = OrderPage(self.driver)
        # 根据指定的收件地址选择订单
        self.driver.find_element_by_xpath('//span[text()="%s"]'%add).click()
        # 点击打印快递单
        orderpage.click_print()
        time.sleep(1)
        # 选择模板
        self.driver.find_element_by_xpath('//label[text()="%s"]'%tem).click()
        # 选择打印机
        orderpage.choose_printer('Microsoft XPS Document Writer')
        # 点击打印
        orderpage.click_print1()
        time.sleep(1)
        # 确定打印
        orderpage.yes_print()


        time.sleep(10)











if __name__=='__main__':
    unittest.main()
