from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction(object):
    _driver = None
    @classmethod
    def setDriver(cls):   #实现初始化浏览器操作，在接下来的测试用例模块中，每个测试模块测试前都需要调用该方法；
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(5)
        return cls._driver
    @classmethod
    def setDriverNone(cls):    #清空初始化后的浏览器数据，每个测试模块测试结束后都需要执行该方法
        if cls._driver:
            cls._driver = None
        return cls._driver
    @classmethod
    def quiteDriver(cls):     #进行关闭浏览器操作，每个测试模块测试结束后都需要调用，关闭浏览器；
        return cls.setDriver().quit()
    @classmethod
    def findElement(cls,driver,method,locator,outTime=30):   #定位页面元素的方法封装，此方法供接下来的POM文件夹中相关页面类调用实现对应的页面元素定位与操作
        try:
            print('[Info:Starting find the element "{}" by "{}"!]'.format(locator,method))
            element = WebDriverWait(driver, outTime).until(lambda x: x.find_element(method, locator))
        except Exception as e:
            raise e
        else:
            print('[Info:Had found the element "{}" by "{}"!]'.format(locator,method))
            return element