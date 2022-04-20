
#定位元素，异常处理

from woniu_test.utils.tool import Tools


class getElement:

    def __init__(self,br):
        Tools.get_webdriver(br)#生成浏览器对象赋给属性
        self.wd=Tools.dr#类名调用属性

    def Get_element(self,how,what):#定位元素，返回查找结果
        ele=self.is_element_present(how,what)
        return  ele
    def is_element_present(self,how,what):#异常处理查找元素，
        try:
            ele=self.wd.find_element(how, what)
        except:
            return 'Not Found'
        return ele

