from selenium.webdriver.common.by import By
import time
from Base_Action.base import BaseAction
from Base_Action.get_Params import getParams
from Base_Action.utils import Utils
#data=getParams('D:\py_code\AutoDT-UI\Page_Elements\Login.yml')
data=getParams(Utils.element_path+'\Login.yml')
dic=data[0]
#封装的页面的动作
class LoginPage:
    def __init__(self):
        self.driver = BaseAction.setDriver()
        #self.findElement = BaseAction.findElement()
    def inputemail(self, email):
        try:
            inputemailElement = BaseAction.findElement(self.driver,By.ID,dic['inputemail_id'])
        except Exception as e:
            print('获取【邮箱】输入框元素失败！')
            raise e
        else:
            return inputemailElement.send_keys(email)

    def inputpassword(self, password):
        try:
            inputpasswordElement = BaseAction.findElement(self.driver,By.ID,dic['inputpassword_id'])
        except Exception as e:
            print('获取【密码】输入框元素失败！')
            raise e
        else:
            return inputpasswordElement.send_keys(password)

    def loginbutton(self):
        try:
            loginbuttonElement=BaseAction.findElement(self.driver,By.ID,dic['loginbutton_id'])
        except Exception as e:
            print('获取【登录】按钮元素失败！')
            raise e
        else:
            return loginbuttonElement.click()


    #清除输入框
    def userNameInputClear(self):
        try:
            userNameInputClear = BaseAction.findElement(self.driver,By.ID, dic['inputemail_id'])
        except Exception as e:
            print('清除用户名输入框失败')
            raise e
        else:
            return userNameInputClear.clear()

    def passwordInputClear(self):
        try:
            passwordInputClear = BaseAction.findElement(self.driver,By.ID, dic['inputpassword_id'])
        except Exception as e:
            print('清除密码输入框失败')
            raise e
        else:
            return passwordInputClear.clear()

    def quitmenu(self):
        self.driver.refresh()
        try:
            #点击头像弹出菜单
            quitmenu = BaseAction.findElement(self.driver,By.XPATH,dic['quitmenu_xapth'])
        except Exception as e:
            print('获取菜单元素失败')
            raise
        else:
            return quitmenu.click()
    def quitbutton(self):
        try:
            quitbutton = BaseAction.findElement(self.driver,By.XPATH,dic['quitbutton_xpath'])
        except Exception as e:
            print('获取退出按钮元素失败')
            raise
        else:
            return quitbutton.click()

if __name__ == '__main__':
    print(data)