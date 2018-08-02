#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

import unittest
import time
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.login_page import Loginpage
from pageobjects.order_create_page import Ordercreate
from  pageobjects.order_page import OrderPage

class Printsend(unittest.TestCase):

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





    def test_print_and_send(self):

        #  参数   ----------------------------------
        address = '张放1'
        tem = '顺丰热敏180mm'
        #   ----------------------------------------------
        logger = Logger(logger="BasePage").getlog()
        #初始化登录界面，并登录
        loginpage = Loginpage(self.driver)
        loginpage.type_username('12830222909')
        loginpage.type_password('1qaz2wsx')
        self.driver.find_element_by_id('submit').click()

        time.sleep(3)
        # 定义一个指定的订单

        # 切换到当前frame
        frame1 = self.driver.find_element_by_id('container-i')
        self.driver.switch_to_frame(frame1)
        time.sleep(3)

        # 页面实例化
        orderpage = OrderPage(self.driver)

        # 根据指定的收件地址选择订单
        self.driver.find_element_by_xpath('//td[text()="%s"]'%address).click()
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
        time.sleep(4)
        # 验证打印结果--------------------------------------------------------------------------------------------------
        row1 = orderpage.element_row('张放1')
        x = '//*[@id="tableDiv"]/table/tbody[2]/tr[%s]/td[1]/i'%row1    # 打印标志
        try:
            if orderpage.is_element_exist(x):
                self.assertTrue(True)
                logger.info('打印成功')
            else:
                self.assertTrue(False)
        except BaseException as e:
            self.assertTrue(False)
        # --------------------------------------------------------------------------------------------------------------
        orderpage.click_consignBtn()
        time.sleep(3)
        # 验证发货合计信息是否正确--------------------------------------------------------------------------------------
        info1 = orderpage.get_consignment_info()
        print(info1)
        try:
            if info1 == '发货合计：共1单':
                self.assertTrue(True)
                logger.info('选择一条订单进行发货')
            else:
                orderpage.get_windows_img()
                self.assertTrue(False)
        except BaseException as e:
            self.assertTrue(False)
        time.sleep(2)
        # 点击确定
        orderpage.click_qdConsign()
        time.sleep(4)
        # 验证发货结果
        info2 = orderpage.get_consignResult_info()
        try:
            if info2 == '共1单，成功1单，失败0单':
                self.assertTrue(True)
                logger.info('一条订单发货成功')
            else:
                orderpage.get_windows_img()
                self.assertTrue(False)
        except BaseException as e:
            self.assertTrue(False)

        # 关闭发货弹框
        orderpage.click_confirm_close()
        time.sleep(2)
        # 跳出frame
        self.driver.switch_to.default_content()
        # 退出登录
        loginpage.skin01_logout()
        time.sleep(3)

if __name__=='__main__':
    unittest.main()
