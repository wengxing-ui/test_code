from selenium import webdriver
from woniusales_test.common.utils import Utils
class Open_browser:
    def __init__(self,browser,url):
        self.browser = browser   # 浏览器名称
        self.url = url   # 访问的网址
        self.driver = None
        self.open()
    def open(self):
        """根据浏览器名称打开对应浏览器"""
        if self.browser.lower() in ('firefox','火狐'):
            self.driver = webdriver.Firefox(executable_path=Utils.driver_path+'/geckodriver.exe')
        elif self.browser.lower() in ('chrome','谷歌'):
            self.driver = webdriver.Chrome(executable_path=Utils.driver_path+'/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)

if __name__ == '__main__':
    ob = Open_browser('火狐','http://47.92.203.151:8000/Agileone/index.php')


