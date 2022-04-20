import pytest
from Business.loginAc import LoginAction
from POM.login_page import LoginPage
import time
from Base_Action.get_Params import getParams
from Base_Action.get_ScreenShot import getScreenShot
from Base_Action.connect_db import ConDB
from Base_Action.utils import Utils
'''
@pytest.fixture(scope='module',autouse=True)#登录界面的前置后置
def module():
    LoginAction(loginParams[0].url).login(username="1191873631@qq.com",password='wx18980322615')
    yield
    # 执行完模块所有测试用例后退出浏览器
    BaseAction.quiteDriver()
    time.sleep(1)
    # 执行完模块所有测试用例后退出登录
    BaseAction.setDriverNone()
    time.sleep(2)
'''
@pytest.fixture(autouse=True)
def clearInput():
    yield
    # 每条登录测试执行后清空用户名和密码输入框
    LoginPage().userNameInputClear()
    LoginPage().passwordInputClear()

#测试用例
#home  url=getParams('D:\pycode\AutoDT-UI\Params\login_Test_Params.yml')[1]['url']
#home  params=getParams('D:\pycode\AutoDT-UI\Params\login_Test_Params.yml')[2]

url=getParams(Utils.case_path+'\\url.yml')[0]['url']
params=getParams(Utils.case_path+'\\login_Test_Params.yml')
moudle=params[0]['module']

@pytest.mark.parametrize('username,password,testcase', argvalues=params[1])
def test_login(username,password,testcase):
    result ='pass'
    path = None
    A=LoginAction(url)
    runLogin = A.login(username,password)
    time.sleep(2)
    if username == 'UI_test@qq.com' and password == 'wx112233':
        print(f'使用正确的用户名{username}和密码{password}登录')
        excUrl='https://dt.mockplus.cn/app'
        try:
            assert runLogin[0] == excUrl
        except AssertionError as e:
            result='fail'
            path=getScreenShot()
            raise e
        else:
            A.quitlogin()
    elif username == '' and password != '':
        print('用户名为空，登录密码password:{}进行登录'.format(password))
        try:
            assert runLogin[0] == url
        except AssertionError as e:
            result = 'fail'
            path=getScreenShot()
            raise e
    elif username != '' and password == '':
        print('用户名username:{}，登录密码为空进行登录'.format(username))
        try:
            assert runLogin[0] == url

        except AssertionError as e:
            result = 'fail'
            path=getScreenShot()
            raise e
    elif username == '' and password == '':
        print('用户名为空，登录密码为空进行登录')
        try:
            assert runLogin[0] == url

        except AssertionError as e:
            result = 'fail'
            path=getScreenShot()
            raise e
    else:
        print('用用户名username:{}与密码password:{}进行登录'.format(username, password))
        try:
            assert runLogin[0] == url

        except AssertionError as e:
            result = 'fail'
            path=getScreenShot()
            raise e
    data=username+'+'+password
    ConDB.write_in(moudle,testcase,data,result,comment=path)  #中间有个time参数
    ConDB.close()