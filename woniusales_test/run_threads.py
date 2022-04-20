from woniusales_test.common.utils import Utils
from woniusales_test.common.open_browser import Open_browser
import sys
import threading
def main(data,browser):
    """
    测试主函数
    :param data: 读取到的所有测试数据
    :param browser: 浏览器名称
    :return:
    """
    for i in data:
        if i[-1] == 'Y':
            ob = Open_browser(browser, 'http://47.92.203.151:8080/woniusales')  # 打开浏览器
            # 导入测试脚本
            __import__('woniusales_test.case.test_' + i[-4])
            mo = sys.modules['woniusales_test.case.test_' + i[-4]]  # 加载到内存
            try:
                cl = getattr(mo, i[-3])  # 获取测试脚本中的测试类
                obj = cl(ob.driver)  # 创建测试类的对象
                print(f'{browser}--{i[0]}--',end='')
                obj.test(i)  # 调用测试类中的测试方法
            except Exception as e:
                print(e)
            ob.driver.quit()
if __name__ == '__main__':
    # 获取登录测试数据
    data = Utils.get_data(Utils.data_path + '/woniusales_testcase.csv')[1:]
    # 创建线程
    th1 = threading.Thread(target=main,args=(data,'火狐'))
    th2 = threading.Thread(target=main, args=(data, 'chrome'))
    th1.start()
    th2.start()


