from selenium.webdriver.common.by import By
import time
from Base_Action.base import BaseAction
from Base_Action.get_Params import getParams
#data=getParams('D:\软件\py_code\AutoDT-UI\Page_Elements\Menu.yml')
data=getParams('D:\软件\pycode\AutoDT-UI\Page_Elements\Menu.yml')
dic=data[0]

class MenuPage:
    def __init__(self):
        self.driver = BaseAction.setDriver()
    def meunbutton(self):
        try:
            meunbuttonElement=BaseAction.findElement(self.driver,By.XPATH,dic['menu_button_xpath'])
        except Exception as e:
            print('获取【菜单】按钮元素失败！')
            raise e
        else:
            return  meunbuttonElement.click()

    def personalbutton(self):
        try:
            personalbuttonElement=BaseAction.findElement(self.driver,By.XPATH,dic['personal_link_xpath'])
        except Exception as e:
            print('获取【个人信息】按钮元素失败')
            raise e
        else:
            return personalbuttonElement.click()

    def websitebutton(self):
        try:
            websitebuttonElement=BaseAction.findElement(self.driver,By.XPATH,dic['website_link_xpath'])
        except Exception as e:
            print('获取【访问官网】按钮元素失败')
            raise e
        else:
            return websitebuttonElement.click()

    def feedbackbutton(self):
        try:
            feedbackbuttonElement=BaseAction.findElement(self.driver,By.XPATH,dic['feedback_link_xpath'])
        except Exception as e:
            print('获取【意见反馈】按钮元素失败')
            raise e
        else:
            return feedbackbuttonElement.click()

    def forumbutton(self):
        try:
            forumbuttonElement = BaseAction.findElement(self.driver, By.XPATH, dic['forum_link_xpath'])
        except Exception as e:
            print('获取【讨论区】按钮元素失败')
            raise e
        else:
            return forumbuttonElement.click()