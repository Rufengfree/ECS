# coding=utf-8
from framework.base_page import BasePage
from framework.logger import Logger


class Loginpage(BasePage):

    username = 'id=>userName' #用户名
    password = 'id=>passWord' #密码
    loginbtn = 'id=>submit' #登录
    topNavBtn = 'x=>//*[@id="topNavBtn"]' #用户信息按钮
    skin01_logoutBtn = 'x=>//*[@id="logoutBtn"]/div/div[2]' #退出按钮
    logout = 'x=>//*[@id="g_header"]/div[1]/div/a[2]/span/span'
    generalLogin = 'x=>//*[@id="loginForm"]/ul[1]/li[2]/a'

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