# coding=UTF-8
'''
Created on 2019年5月31日

@author: lush
'''
import os
from com.hpeu.crm.utils.GetCurrentTime import getTime

class GetScreenshots():
    def __init__(self,object):
        self.myDriver = object
    
    def getScreenshot(self,name):
        file_dir = os.path.dirname(os.path.abspath("__file__"))+"\\..\\..\\..\\..\\screenshots\\"
        
        #date_dir = time.strftime("%Y%m%d",time.localtime(time.time()))
        date_dir=getTime().getCurrentDate()
        file_dir = file_dir + date_dir+"\\"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        else:
            pass
        
        #file_name = file_dir + name + time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+".png"
        file_name = file_dir + name + getTime().getCurrentTime()+".png"
        self.myDriver.get_screenshot_as_file(file_name)
        
        
    