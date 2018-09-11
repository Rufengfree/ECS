# coding=utf-8
from framework.base_page import BasePage
from framework.logger import Logger
import selenium


class Loginpage(BasePage):

    username = 'id=>userName' #用户名
    password = 'id=>passWord' #密码
    loginbtn = 'x=>//*[@id="submit"]' #登录
    topNavBtn = 'x=>//*[@id="topNavBtn"]' #用户信息按钮
    skin01_logoutBtn = 'x=>//*[@id="logoutBtn"]/div/div[2]' #退出按钮
    logout = 'x=>//*[@id="g_header"]/div[1]/div/a[2]/span/span'
    generalLogin = 'x=>//*[@id="yddLogin"]'

    def type_username(self,text):
        self.type(self.username,text)
    def type_password(self,text):
        self.type(self.password,text)
    def click_loginbtn(self):   #点击登录按钮
        self.click(self.loginbtn)
    def skin01_logout(self):
        logger = Logger(logger="BasePage").getlog()
        try:
            self.mouse_suspension(self.topNavBtn)
            self.sleep(1)
            self.click(self.skin01_logoutBtn)
        except:
            pass
    def click_logout(self):
        self.click(self.logout)

    def type_login_info(self,username,password):
        self.click(self.generalLogin)
        self.type(self.username, username)
        self.type(self.password, password)

    def login(self,username,password):
        self.click(self.generalLogin)
        self.type(self.username, username)
        self.type(self.password, password)
        self.driver.find_element_by_id('submit').click()

        def checked():
            if '易打单' == self.get_page_title():
                print("账号%a 登录成功" % username)
            elif '易打单 订单管理' == self.get_page_title():
                print("账号%a 登录成功" % username)
            else:
                self.get_windows_img()
        try:
            if self.is_element_exist('//*[@id="forget_pwd"]') == True:  # 跳过修改密码直接登录
                self.driver.find_element_by_xpath('//*[@id="forget_pwd"]').click()
                checked()
            elif self.is_element_exist('//*[@id="forget_pwd"]') == False:
                checked()
        except BaseException as e:
            pass
