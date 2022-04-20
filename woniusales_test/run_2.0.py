from woniusales_test.common.utils import Utils
from woniusales_test.common.open_browser import Open_browser
import sys,time
from woniusales_test.common.connect_db import ConDB
from woniusales_test.common.get_chart import echart
import random
# 执行测试
def main(data,version):
    """
    执行测试
    :param data: 测试数据
    :param version: 版本
    :return:
    """
    for i in data:
        if i[-1] == 'Y':
            ob = Open_browser(i[-2], 'http://localhost:8080/woniusales')  # 打开浏览器
            # 导入测试脚本
            __import__('woniusales_test.case.test_' + i[-4])
            mo = sys.modules['woniusales_test.case.test_' + i[-4]]  # 加载到内存
            try:
                cl = getattr(mo, i[-3])  # 获取测试脚本中的测试类
                obj = cl(ob.driver)  # 创建测试类的对象
                obj.test(i)  # 调用测试类中的测试方法
                # 将测试执行结果写入数据库
                sql = f'''insert into test_result(`browser`,`module`,`case`,`test_data`,`result`,`date`,`version`) 
                          values("{i[-2]}","{i[-4]}","{i[0]}","{i[1]}","{obj.result}","{Utils.get_time()}","{version}");'''
            except Exception as e:
                print(e)
            ob.driver.quit()
        else:
            sql = f'''insert into test_result(`browser`,`module`,`case`,`test_data`,`result`,`date`,`version`) 
                                  values("{i[-2]}","{i[-4]}","{i[0]}","{i[1]}","skip","{Utils.get_time()}","{version}");'''
        ConDB.dml(sql)  # 执行SQL，插入数据
    ConDB.commit()   # 提交事务
if __name__ == '__main__':
    # 连接数据库
    ConDB.con_db(host='localhost', passwd='123456', db='woniusales')
    # # 获取登录测试数据
    data = Utils.get_data(Utils.data_path + '/woniusales_testcase.csv')[1:]
    ################################################
    total = len(data)   # 用例总数
    version = '1.4'     # 版本
    d = Utils.get_time().split()[0]  # 测试日期
    tester = '张三'     # 测试人员
    ################################################
    start = time.time()
    main(data,version)  # 调用main函数，执行测试
    during = f'{time.time() - start:.2f}'  # 测试耗时
    ################################################
    # 获取测试结果
    sql = f'select count(*) from test_result where result="pass" and version="{version}"'
    p = ConDB.select_one(sql)[0]   # (4,)  # 用例通过数
    sql = f'select count(*) from test_result where result="fail" and version="{version}"'
    f = ConDB.select_one(sql)[0]   # (4,)  # 用例失败数
    skip = total-p-f    # 用例跳过数
    rate = f'{100*p/total:.2f}%'  # 通过率
    demo = Utils.report_path+'/demo.html'
    report = Utils.report_path+f'/{Utils.get_time()}.html'
    ################################################
    # 根据测试结果生成柱状图
    echart(version)
    ################################################
    # 根据实际测试结果，生成测试报告
    Utils.get_report(version,d,str(during),tester,str(total),str(p),str(f),str(skip),str(rate),demo,report)
    ################################################
    ConDB.close()    # 关闭数据库


