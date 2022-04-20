
from Base_Action.base import BaseAction
from POM.login_page import LoginPage
import time

class LoginAction(BaseAction):
    def __init__(self,url):
        self.url = url
        self.driver = BaseAction.setDriver()
        self.driver.get(url)
    def login(self, username, password):
        # 在登录页面输入用户名
        LoginPage().inputemail(username)
        print('在登录页面用户名输入框输入：{}'.format(username))
        # 在登录页面输入登录密码
        LoginPage().inputpassword(password)
        print('在登录页面密码输入框中输入：{}'.format(password))
        # 在登录页面点击登录按钮
        LoginPage().loginbutton()
        print('点击登录按钮')
        currUrl = self.driver.current_url  #点击登录后的网址
        return currUrl, self.driver
    def quitlogin(self):
        LoginPage().quitmenu()
        time.sleep(2)
        LoginPage().quitbutton()
        print('点击关闭按钮')


