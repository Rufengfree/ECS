#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: rufeng

import unittest
import time
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.login_page import Loginpage
from pageobjects.order_create_page import Ordercreate
from pageobjects.order_page import OrderPage


class Addtemplate(unittest.TestCase):
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

    def test_add_template(self):
        logger = Logger(logger="BasePage").getlog()
        companyname = '顺丰'

        #初始化登录界面，并登录
        loginpage = Loginpage(self.driver)
        loginpage.type_login_info('12830222909', '1qaz2wsx')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        # 切换frame
        frame1 = self.driver.find_element_by_id('container-i')
        self.driver.switch_to_frame(frame1)
        # 页面初始化
        orderpage = OrderPage(self.driver)
        # 如果模板已经存在就判断用例失败,然后直接退出
        if orderpage.is_element_exist('//span[text()="顺丰热敏180mm"]'):
            self.assertFalse(True)
        # 如果模板不存在就添加模板
        else:
            # 点击新增模板按钮
            orderpage.click_add_template()
            time.sleep(2)
        # 点击物流公司下拉框
            orderpage.click_Logistics_company()
            time.sleep(3)
        # 选择物流公司
            self.driver.find_element_by_xpath('//li[text()="%s"]'%companyname).click()
        # 选择要添加的模板
            orderpage.click_templete()
        # 选择运费付款方式
            orderpage.click_paytype()
            time.sleep(2)
        # 点击添加按钮
            orderpage.click_add()
            time.sleep(2)
        # 点击添加完成的确定按钮
            orderpage.click_button()
        # 关掉添加模板的弹框
            orderpage.template_close()
            time.sleep(2)

        # 判断模板是否添加成功
            try:
                if orderpage.is_element_exist('//span[text()="顺丰热敏180mm"]'):
                    self.assertTrue(True)
                    logger.info("新添加模板名称存在，模板添加成功")
                else:
                    orderpage.get_windows_img()
                    self.assertTrue(False)
            except BaseException as e:
                self.assertTrue(False)

        # 跳出frame
        self.driver.switch_to.default_content()
        # 退出登录
        loginpage.skin01_logout()
        time.sleep(3)

if __name__=='__main__':
    unittest.main()
