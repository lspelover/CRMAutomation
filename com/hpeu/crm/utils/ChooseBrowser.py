# coding=UTF-8
'''
Created on 2019年5月31日

@author: lush
'''

from selenium import webdriver

class ChooseBrowser():
    
    def getBrowserDriver(self,BrowserType):
        if BrowserType == "IE":
            driver = webdriver.Ie()
        elif BrowserType == "Chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
            
        return driver