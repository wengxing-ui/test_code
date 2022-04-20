from woniusales_test.common.open_browser import Open_browser
import time
class Test_Login:
    def __init__(self,driver):
        self.driver = driver
    def login(self,n,p,v):
        """
        登录
        :param n: 用户名
        :param p: 密码
        :param v: 验证码
        :return:
        """
        user = self.driver.find_element_by_id('username').send_keys(n)
        self.driver.find_element_by_id('password').send_keys(p)
        self.driver.find_element_by_id('verifycode').send_keys(v)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/form/div[6]/button').click()
        time.sleep(2)

    def test(self,data):
        d = data[1].split(',')   # 测试数据
        exp = data[2]            # 预期结果
        self.login(d[0],d[1],d[2])
        # 将登录成功与失败的用例分别做断言
        if '登录成功' in exp:
            # 获取登录成功后页面上的用户名/
            msg = self.driver.find_element_by_xpath('//*[@id="navbar"]/ul[2]/li[1]/a').text
            if exp.split('-')[1] in msg:
                if 'admin' in d[0]:  # 如果登录用户为管理员，查找是否存在批次管理功能
                    try:
                        self.driver.find_element_by_link_text('批次管理')
                    except Exception:
                        print('fail')
                        self.result = 'fail'
                print('pass')
                self.result = 'pass'
            else:
                print('fail')
                self.result = 'fail'
        else:
            # 获取登录失败的提示信息
            msg = self.driver.find_element_by_class_name('bootbox-body').text
            if exp.split('-')[1] in msg:
                print('pass')
                self.result = 'pass'
            else:
                print('fail')
                self.result = 'fail'
if __name__ == '__main__':
    ob = Open_browser('火狐','http://47.92.203.151:8080/woniusales')
    tl = Test_Login(ob.driver)
    tl.test(['输入有效用户信息，登录成功','admin,123456,0000','登录成功，显示-admin'])