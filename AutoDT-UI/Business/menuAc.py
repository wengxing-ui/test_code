
from Base_Action.base import BaseAction
from POM.menu import MenuPage
import time

class MenuAction(BaseAction):
    def __init__(self,url):
        self.url = url
        self.driver = BaseAction.setDriver()
        self.driver.get(url)
    def personal(self):
        MenuPage().meunbutton()
        MenuPage().personalbutton()
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        currUrl=self.driver.current_url
        self.driver.close()
        return currUrl,self.driver

    def website(self):
        MenuPage().meunbutton()
        MenuPage().websitebutton()
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        currUrl=self.driver.current_url
        self.driver.close()
        return currUrl,self.driver

    def feedback(self):
        MenuPage().meunbutton()
        MenuPage().feedbackbutton()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        currUrl = self.driver.current_url
        self.driver.close()
        return currUrl, self.driver

    def forum(self):
        MenuPage().meunbutton()
        MenuPage().forumbutton()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        currUrl = self.driver.current_url
        self.driver.close()
        return currUrl, self.driver

