from selenium.webdriver.support.select import Select
from woniu_test.getelements.Pom import getElement
from woniu_test.utils.tool import Tools

#动作封装，方便调用
class actionRepo:

    def open(self,br,url):
        self.ge=getElement(br)#实例化 创建浏览器对象
        self.wd = self.ge.wd#对象调用属性
        self.wd.get(url)#传入网址打开woniusales

    #点击
    def click_button(self,rect,str=''):
        how,what=Tools.get_rect(rect)
        ele=self.ge.Get_element(how,what)#检查

        if ele=='Not Found':
            print('元素不存在')
        else:
            ele.click()
    #发送消息
    def type_string(self,rect,string):
        how, what = Tools.get_rect(rect)
        ele = self.ge.Get_element(how, what)
        if ele=='Not Found':
            print('元素不存在')
        else:
            ele.send_keys(string)
    #下拉框
    def choose_option(self,rect,type,value):
        how, what = Tools.get_rect(rect)
        sel=Select(self.ge.Get_element(how, what))
        if type=='index':
            sel.select_by_index(value)
        if type=='value':
            sel.select_by_value(value)
        if type=='visible':
            sel.select_by_visible_text(value)
    #修改属性
    def set_date(self,rect,date):
        how, what = Tools.get_rect(rect)
        js=''
        if how=='id':
            js=f"document.getElementById({what}).removeAttribute(\"readonly\")"

        if how=='class':
            js=f"document.getElementsByClassName({what})[0].removeAttribute(\"readonly\")"

        if how=='tag':
            js=f"document.getElementsByTagName({what})[0].removeAttribute(\"readonly\")"

        if how=='name':
            js=f"document.getElementsByName({what})[0].removeAttribute(\"readonly\")"
        self.wd.execute_script(js)

        ele=self.ge.Get_element(how,what)
        if ele=='Not Found':
            print('元素不存在')
        else:
            ele.send_keys(date)

    def update_file(self,rect,str):

        self.type_string(rect,str)

    #警告框操作
    def do_alert(self,type,string=''):
        ele=self.ge.wd.switch_to.alert
        if type=='accept':
            ele.accept()
        if type=='dismiss':
            ele.dismiss()
        if type=='enter':
            ele.send_keys(string)
            ele.accept()
    #切换窗口
    def change_window(self,index=-1):
        #新窗口的句柄在handles中索引为-1
        li=self.ge.wd.window_handles
        self.ge.wd.switch_to.window(li[index])

        #第二种方式
        # handle=self.ge.wd.current_window_handle
        # handles=self.ge.wd.window_handles
        # for i in handles:
        #     if handle != i:
        #         self.ge.wd.switch_to.window(i)

    # def get_rect(self,rect):
    #     how,what=rect.split('=',1)
    #     return how,what

    def choose_frame(self,rect):
        how,what=Tools.get_rect(rect)
        els=self.ge.wd.Get_element(how,what)
        self.ge.wd.switch_to.frame(els)
        if els=='Not Found':
            print('元素不存在')
        else:
            self.ge.wd.switch_to.frame(els)