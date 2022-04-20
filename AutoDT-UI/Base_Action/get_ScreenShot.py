
import time
from Base_Action.base import BaseAction
from Base_Action.utils import Utils
import os
def getScreenShot():
    driver = BaseAction.setDriver()
    file_time= time.strftime("%Y-%m-%d", time.localtime(time.time()))
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    file_path = os.path.join(Utils.picture_path, f'{file_time}')  #创建当前目录
    if os.path.exists(file_path):
        try:
            path = file_path +'\\'+ picture_time +'.png'
            picture_url = driver.get_screenshot_as_file(path)
            print("%s：截图成功！！！" % picture_url)
        except BaseException as msg:
            print(msg)
        else:
            return picture_url
    else:
        os.mkdir(file_path)
        try:
            path = file_path +'\\'+ picture_time +'.png'
            picture_url = driver.get_screenshot_as_file(path)
            print("%s：截图成功！！！" % picture_url)
        except BaseException as msg:
            print(msg)
        else:
            return picture_url