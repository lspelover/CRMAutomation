# coding=UTF-8

'''
Created on 2019年5月31日

@author: lushipeng
'''
import xlrd
import os

class GetValues():
    file_dir = os.path.dirname(os.path.abspath("."))+"\\..\\..\\..\\resources\\TestContent.xlsx"
    file_content = xlrd.open_workbook(file_dir)
    def getTestConfigValue(self,nrow,ncol):
        TestConfiguration = self.file_content.sheet_by_name("TestConfiguration")
        return TestConfiguration.cell(nrow-1,ncol-1).value
    
    def getTestDataValue(self,nrow,ncol):
        TestData = self.file_content.sheet_by_name("TestData")
        return TestData.cell(nrow-1,ncol-1).value
       
    def getPageElementValue(self,nrow,ncol):
        PageElement = self.file_content.sheet_by_name("PageElement")
        return PageElement.cell(nrow-1,ncol-1).value



