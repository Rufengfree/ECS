# coding=utf-8
import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import Loginpage


class login(unittest.TestCase):
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
        """
        这里一定要test开通，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        loginpage = Loginpage(self.driver)
        loginpage.type_username('ecs1105')
        loginpage.type_password('1qaz2wsx')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        loginpage.get_windows_img()
        try:
            assert '易打单 | 批量打印' == loginpage.get_page_title()
            print('Test pass.')
        except Exception as e:
            print('Test fail.',format(e))
        loginpage.skin01_logout()

    def test_login_ecs2(self):
        loginpage = Loginpage(self.driver)
        loginpage.type_username('110140029')
        loginpage.type_password('1qaz2wsx')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        loginpage.get_windows_img()
if __name__=='__main__':
    unittest.main()