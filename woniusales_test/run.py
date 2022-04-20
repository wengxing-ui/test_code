# 主程序文件，运行整个框架
from woniusales_test.case.test_login import Test_Login
from woniusales_test.case.test_add_customer import Test_Add_Customer
from woniusales_test.common.utils import Utils
from woniusales_test.common.open_browser import Open_browser

# 测试登录功能
# 获取登录测试数据
data = Utils.get_data(Utils.data_path+'/woniusales_login.csv')[1:]
for i in data:
    if i[-1] == 'Y':  # 如果标记为Y则执行该调用例
        ob = Open_browser(i[-2], 'http://47.92.203.151:8080/woniusales')  # 打开浏览器
        tl = Test_Login(ob.driver)
        tl.test(i)  # 执行测试
        tl.driver.quit()   # 关闭浏览器
# 获取新增会员测试数据
data = Utils.get_data(Utils.data_path+'/woniusales_add_customer.csv')[1:]
ob = Open_browser(i[-2], 'http://47.92.203.151:8080/woniusales')  # 打开浏览器
tl = Test_Login(ob.driver)
tl.login('admin','123456','0000')   # 登录
for i in data:
    if i[-1] == 'Y':  # 如果标记为Y则执行该调用例
        tac = Test_Add_Customer()
        tac.test(i)  # 执行测试
tl.driver.quit()   # 关闭浏览器
