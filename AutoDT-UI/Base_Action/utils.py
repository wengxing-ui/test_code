import time
import os
class Utils:
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目路径
    element_path = os.path.join(base_path, 'Page_Elements')  # 测试数据文件所在路径
    case_path = os.path.join(base_path, 'Params')  # 用例所在路径
    picture_path=os.path.join(base_path, 'Picture') #图片存储路径
    report_path = os.path.join(base_path, 'report')  # 测试报告所在路径
    @classmethod
    def get_time(cls):
        return time.strftime('%Y-%m-%d', time.localtime())

if __name__ == '__main__':
    file_time= time.strftime("%Y-%m-%d", time.localtime(time.time()))
    file_path = os.path.join(Utils.picture_path, f'{file_time}')
    os.mkdir(file_path)