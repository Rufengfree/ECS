# coding=utf-8
from framework.base_page import BasePage

class Loginpage(BasePage):
    username = 'id=>userName' #用户名
    password = 'id=>passWord' #密码
    loginbtn = 'id=>submit' #登录
    topNavBtn = 'id=>topNavBtn' #用户信息按钮
    logoutBtn = 'id=>logoutBtn' #退出按钮

    def type_username(self,text):
        self.type(self.username,text)
    def type_password(self,text):
        self.type(self.password,text)
    def click_loginbtn(self):
        self.click(self.loginbtn)
    def skin01_logout(self):
        try:
            self.mouse_suspension(self.topNavBtn)
            self.sleep(1)
            self.click(self.logoutBtn)
        except:
            pass