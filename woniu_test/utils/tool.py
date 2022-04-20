from selenium import webdriver

#µ¥ÀýÄ£Ê½
class Tools:
    dr=''
    @classmethod
    def get_webdriver(cls,browser):
        if cls.dr=='':
            if browser=='ff' or browser=='firefox':
                cls.dr=webdriver.Firefox(executable_path='../drivers1/geckodriver.exe')
            elif browser == 'ch' or browser == 'chrom':
                cls.dr = webdriver.Firefox(executable_path='../drivers1/chromedriver.exe')

    @classmethod
    def get_rect(cls,rect):
        how,what=rect.split('=',1)
        return how,what