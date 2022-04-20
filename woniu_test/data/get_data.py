from woniu_test.action.actions import actionRepo
from woniu_test.cases.testcase import allcases
from woniu_test.utils.tool import Tools
#读取数据，处理数据
class getData:

    def __init__(self):
        self.action=actionRepo()
        self.cases=allcases()

    def read_txt(self,path):
        with open(path,encoding="utf-8") as file:
            data_li=file.readlines()
            for i in data_li:
                self.do_test(i.strip().split(','))
    def read_excel(self):
        pass

    def read_csv(self):
        pass

    def get_from_db(self):
        pass

    def get_from_zentao(self):
        pass

    def do_test(self,li):       #执行测试用例
        if 'should' not in li[0]:
            getattr(self.action,li[0])(li[1],li[2])
        else:
            getattr(self.cases,li[0])(li[1],li[2])

if __name__ == '__main__':
    getData().read_txt('data1.txt')
    Tools.dr.quit()

