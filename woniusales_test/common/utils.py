import csv,time
from faker import Faker
import os
class Utils:
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目路径
    case_path = os.path.join(base_path, 'case')  # 用例所在路径
    driver_path = os.path.join(base_path, 'driver')  # 浏览器驱动所在路径
    report_path = os.path.join(base_path, 'report')  # 测试报告所在路径
    data_path = os.path.join(base_path,'data')    # 测试数据文件所在路径
    @classmethod
    def get_time(cls):
        return time.strftime('%Y-%m-%d',time.localtime())
    @classmethod
    def get_data(cls, file):
        with open(file,encoding='utf8') as f:
            return list(csv.reader(f))
    @classmethod
    def get_phone(cls):
        return Faker(locale='zh_CN').phone_number()
    @classmethod
    def get_date(cls):
        """获取随机日期"""
        return Faker(locale='zh_CN').date()
    @classmethod
    def get_name(cls):
        return Faker(locale='zh_CN').name()
    @classmethod
    #根据测试结果 去修改demo文件，另存为report，替换其中表格的值,demo文件本身就是一个规范的表格
    #导入柱状图即get_chart产生的html作为内框架放进去
    #就是完整的测试报告
    def get_report(cls,t,v,dur,tester,total,p,fail,s,r,demo,file):
        """
        根据实际测试结果生成测试报告
        :param v: 版本
        :param t: 测试日期
        :param dur: 测试耗时
        :param tester: 测试人员
        :param total: 用例总数
        :param p: 通过数
        :param fail: 失败数
        :param s: 跳过数
        :param r: 通过率
        :param demo: 报告模板
        :param file: 测试报告
        :return:
        """
        html = None
        with open(demo,encoding='utf8') as f:
            html = f.read()  # 读取demo文件的内容
            html = html.replace('&version',v)  # 替换&version
            html = html.replace('&date',t)   # 替换&date
            html = html.replace('&duration',dur)
            html = html.replace('&tester',tester)
            html = html.replace('&total',total)
            html = html.replace('&pass',p)
            html = html.replace('&fail',fail)
            html = html.replace('&skip',s)
            html = html.replace('&rate',r)
        with open(file,'w',encoding='utf8') as f:
            #将修改完的demo文件，重新写入一个报告中
            f.write(html)
if __name__ == '__main__':
    print(Utils.base_path)
    print(Utils.get_time())

