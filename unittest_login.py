import unittest
import os
class EcshopLogin(unittest.TestCase):

    def test01_111(self):
        print('测试1')

    def test01_222(self):
        print('测试2')

    def test01_333(self):
        print('测试2')
if __name__ == '__main__':
    print('------------')
    suite = unittest.TestSuite()  #测试套件
    suite.addTest(EcshopLogin('test01_111'))
    suite.addTest(EcshopLogin('test01_222'))
    #testcase=[EcshopLogin("test01_111"),EcshopLogin("test01_222")]
    #加载一个用例集

    #testcase = unittest.defaultTestLoader.discover(start_dir=os.getcwd(),pattern='*.py')
    #使用默认加载器去发现用例的文件并执行


    #unittest.main(defaultTest='suite')
    unittest.TextTestRunner().run(suite)

