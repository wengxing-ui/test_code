'''
Created on Aug 8, 2019
@author: liliang
'''
import os
import time



class MyClass():
    '''
    classdocs
    '''

    def __init__(self):
        pass

    def open_file(self):
        tempfile = os.path.abspath("") + "\\1.html"
        tem = open(tempfile, mode='r', encoding='utf-8').read()
        return tem

    def write_file(self, file, test_data, version, passnum, faillnum, errornum, lasttime, all_data):
        file = file.replace("&test_data", test_data)
        file = file.replace("&version", version)
        file = file.replace('&pass', passnum)
        file = file.replace('&fail', faillnum)
        file = file.replace('&error', errornum)
        file = file.replace('&lasttime', lasttime)
        content = ''
        for i in range(0, len(all_data)):
            if all_data[i]["name"] == "粉丝":
                content += "<tr height=40 bgcolor='red'>"
                content += "<td width='7%%' >%s</d>" % str(all_data[i]["name"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["age"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["sex"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["school"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["work"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["address"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["sex1"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["school2"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["work3"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["address4"])
                content += "</tr>"
            else:

                content += "<tr height=40 bgcolor='bisque'>"
                content += "<td width='7%%' >%s</d>" % str(all_data[i]["name"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["age"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["sex"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["school"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["work"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["address"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["sex1"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["school2"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["work3"])
                content += "<td width='7%%'>%s</d>" % str(all_data[i]["address4"])
                content += "</tr>"

        #         for result in all_data:
        #             content+="<tr height=40>"
        #             content+="<td width='7%%'>%s</d>" %str(result[0])
        #             content+="<td width='7%%'>%s</d>" %str(result[1])
        #             content+="<td width='7%%'>%s</d>" %str(result[2])
        #             content+="<td width='7%%'>%s</d>" %result[3]
        #             content+="<td width='7%%'>%s</d>" %result[4]
        #             content+="<td width='7%%'>%s</d>" %result[5]
        #             content+="<td width='7%%'>%s</d>" %result[6]
        #             content+="<td width='7%%'>%s</d>" %result[7]
        #             content+="<td width='7%%'>%s</d>" %result[8]
        #             content+="<td width='7%%'>%s</d>" %result[9]
        #             content+="</tr>"
        file = file.replace('&test_result', content)
        file_folder = os.path.abspath("") + "\\1"
        file_name = file_folder
        report_file = open(file_name, mode="w+", encoding='utf-8')
        report_file.write(file)
        report_file.close()

    def get_datetime(self):
        now_time = time.strftime("%Y_%M_%d_%H:%M:%S", time.localtime())
        return now_time


if __name__ == '__main__':
    my = MyClass()
    file = my.open_file()
    all_data = [
        {"name": "Tom", "age": 23, "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小学2", "work3": "学生", "address4": "上海"},
        {"name": "数据", "age": "13", "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小3学", "work3": "学生", "address4": "上海"},
        {"name": "粉丝", "age": "13", "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小学4", "work3": "学生", "address4": "上海"},
        {"name": "阿道夫", "age": "13", "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小fs学", "work3": "学生", "address4": "上海"},
        {"name": "二娃", "age": "13", "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小学fa", "work3": "学生", "address4": "上海"},
        {"name": "我确认", "age": "13", "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小学", "work3": "学生", "address4": "上海"},
        {"name": "特务", "age": "13", "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小学fa", "work3": "学生", "address4": "上海"},
        {"name": "突然", "age": "13", "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小学ddd", "work3": "学生", "address4": "上海"},
        {"name": "圈儿", "age": "13", "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小asss学", "work3": "学生", "address4": "上海"},
        {"name": "让他", "age": "13", "sex": "男", "school": "希望小学", "work": "学生", "address": "上海", "sex1": "男",
         "school2": "希望小学fdsaa", "work3": "学生", "address4": "上海"},
    ]
    my.write_file(file, "2019_07_08_03:07:59", "1.3.0", "90", "7", "key error", "2019_07_08_03:07:59", all_data)
