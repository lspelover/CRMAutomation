# coding=UTF-8

'''
Created on 2019年5月31日

@author: lushipeng
'''
import configparser
import os

class GetValues():
    getValue = configparser.ConfigParser()
    def getTestConfigValue(self,section,option):
        file_dir=os.path.dirname(os.path.abspath("."))+"\\..\\..\\..\\resources\\TestCofiguration.properties"
        self.getValue.read(file_dir, "UTF-8")
        return self.getValue.get(section, option)
    
    def getTestDataValue(self,section,option):
        file_dir=os.path.dirname(os.path.abspath("."))+"\\..\\..\\..\\resources\\TestData.properties"
        
        self.getValue.read(file_dir, "UTF-8")
        return self.getValue.get(section, option)
        
        
    def getPageElementValue(self,section,option):
        file_dir=os.path.dirname(os.path.abspath("."))+"\\..\\..\\..\\resources\\PageElement.properties"
        
        self.getValue.read(file_dir, "UTF-8")
        return self.getValue.get(section, option)

