
from woniu_test.utils.tool import Tools

#判断用例是否通过
class allcases:


    def  get_page_element(self,how,what):#查找元素，得到实际结果act
        wd=Tools.dr
        ele=wd.find_element(how,what)
        msg=ele.text
        if msg:
            return '成功'
        else:
            return '失败'

    def should_equal(self,rect,exp):#对比预期结果exp判断是否通过用例
        how,what=Tools.get_rect(rect)
        act=self.get_page_element(how,what)#实际结果
        print(act)
        if act==exp:
             print('ok')
             return 'pass'

        else:
             print('ko')
             return 'fail'

    def should_contains(self,act,exp):#如有包含关系两个结果之间
        if exp in act or act in exp:
            return 'pass'
        else:
            return 'fail'


    def should_be_number(self,act):#如果实际结果为数字时得断言
        if act.isdigit():
            return 'pass'
        else:
            return 'fail'


