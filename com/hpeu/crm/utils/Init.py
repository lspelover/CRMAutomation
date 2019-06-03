# coding=UTF-8
'''
Created on 2019年6月1日

@author: lush

'''
from selenium import webdriver
from com.hpeu.crm.utils.GetValues import GetValues
from com.hpeu.crm.utils.ChooseBrowser import ChooseBrowser

class Init():
    getValue = GetValues()
    def openLoginPage(self):
        BrowserType =self.getValue.getTestConfigValue("BrowserType", "TestBrowser")
        SystemURL=self.getValue.getTestConfigValue("BrowserURL", "SystemURL")
        self.myDriver = ChooseBrowser.getBrowserDriver( self,BrowserType)
        self.myDriver.get(SystemURL)
        return self.myDriver