import pytest
import time
#from get_path import getPath
#from send_mail import sendEmailAttached,sendEmailHtml

def runCase():
    currtime = time.strftime('%Y-%m-%d')
    filePath = 'D:\软件\pycode\AutoDT-UI\Report'
    reportName = filePath+f'/{currtime}.html'
    pytest.main(
        [
         '--setup-show', '-v', '-s',
         f'--html={reportName}',
         'Test_Case'
        ]
    )
    time.sleep(2)


    #sendEmailAttached()

if __name__ == '__main__':
    runCase()