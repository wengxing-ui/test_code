from pyecharts import options as opts
from pyecharts.globals import ThemeType
import re
from pyecharts.charts import Bar
from woniusales_test.common.utils import Utils
from woniusales_test.common.connect_db import ConDB
def echart(version):
    #只需传入版本，数据从数据库查找。生成柱状图，并修改为居中显示
    ConDB.con_db(host='localhost', passwd='123456', db='woniusales')
    # 获取模块名称
    mo = []
    sql = f'select distinct module from test_result where version="{version}";'
    for i in ConDB.select_all(sql):
        mo.append(i[0])
    print(mo)
    # 获取每个模块的用例数
    case_num = []
    sql = f'select count(*) from test_result where version="{version}" group by module'
    for i in ConDB.select_all(sql):
        case_num.append(i[0])
    # 获取每个模块通过的用例数
    pass_num = []
    sql = f'select count(*) from test_result where result="pass" and version="{version}" group by module'
    for i in ConDB.select_all(sql):
        pass_num.append(i[0])
    # 获取每个模块失败的用例数
    fail_num = []
    sql = f'''
    select ifnull(mc.c,0)
    from test_result tr
    left join
    (select module,count(*) c from test_result where result="fail" and version="{version}" group by module)  mc
    on tr.module = mc.module
    group by tr.module;
    '''
    for i in ConDB.select_all(sql):
        fail_num.append(i[0])
    print(pass_num, fail_num)
    # 获取每个模块跳过的用例数
    skip_num = []
    sql = f'select count(*) from test_result where result="skip" and version="{version}" group by module'
    for i in ConDB.select_all(sql):
        skip_num.append(i[0])
    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    bar.add_xaxis(mo)   # X轴，模块名称
    bar.add_yaxis("用例数",case_num)
    bar.add_yaxis("通过数", pass_num)
    bar.add_yaxis("失败数", fail_num)
    bar.add_yaxis("跳过数", skip_num)
    bar.set_global_opts(title_opts=opts.TitleOpts())
    bar.render(Utils.report_path+'/WoniuSales测试统计.html')#生成测试报告存放在report中
    with open(Utils.report_path+'/WoniuSales测试统计.html') as f:
        s = f.read()
        #将整个html报告用字符串方式输出。方便修改
    with open(Utils.report_path+'/WoniuSales测试统计.html', 'w') as f:
        f.write(re.sub('width:900px; height:500px;','width:900px; height:500px;margin:auto;',s))
        #margin：auto用替换的方式修改html的属性 使其水平居中


if __name__ == '__main__':

    echart('1.1')