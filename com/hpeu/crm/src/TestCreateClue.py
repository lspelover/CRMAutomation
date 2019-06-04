# coding=UTF-8
'''
Created on 2019年6月1日

@author: lushipeng
'''
from com.hpeu.crm.src.TestInit import TestInit
from com.hpeu.crm.utils.GetScreenShots import GetScreenshots
from com.hpeu.crm.utils.GetValues import GetValues
from com.hpeu.crm.utils.Init import Init
import unittest
from time import sleep

class TestCreateClue(unittest.TestCase):
    
    def setUp(self):
        self.getValue = GetValues()
        self.myDriver = Init().openLoginPage()
        self.getScreenshot = GetScreenshots(self.myDriver)
        self.testInit = TestInit(self.myDriver)
        self.testInit.login()

    def testCreateClue(self):
        createclueoption_linktext = self.getValue.getPageElementValue(3, 11)
        self.myDriver.find_element_by_link_text(createclueoption_linktext).click()
        sleep(3)
        self.getScreenshot.getScreenshot("CreateCluePage")
        
        #input clue information
        comname_id=self.getValue.getPageElementValue(3, 5)
        comname=self.getValue.getTestDataValue(5, 2)
        self.myDriver.find_element_by_id(comname_id).send_keys(comname)
        
        contactname_id=self.getValue.getPageElementValue(4, 5)
        contactname=self.getValue.getTestDataValue(6, 2)
        self.myDriver.find_element_by_id(contactname_id).send_keys(contactname)
        
        saltname_xpath=self.getValue.getPageElementValue(7, 2)
        saltnameselection_xpath=self.getValue.getPageElementValue(8, 2)
        self.myDriver.find_element_by_xpath(saltname_xpath).click()        
        self.myDriver.find_element_by_xpath(saltnameselection_xpath).click()
        
        mobile_id=self.getValue.getPageElementValue(5,5)
        mobile=self.getValue.getTestDataValue(7, 2)
        self.myDriver.find_element_by_id(mobile_id).send_keys(mobile)
        
        email_xpath=self.getValue.getPageElementValue(9, 2)
        email=self.getValue.getTestDataValue(8, 2)
        self.myDriver.find_element_by_xpath(email_xpath).send_keys(email)

        #click save button
        savebtn_xpath=self.getValue.getPageElementValue(10, 2)
        self.myDriver.find_element_by_xpath(savebtn_xpath).click()

        self.myDriver.implicitly_wait(5)
        sleep(3)
        self.getScreenshot.getScreenshot("CreateClueResult")
        createclueresult=self.getValue.getTestDataValue(5, 5)
        assert createclueresult in self.myDriver.page_source
        
    def tearDown(self):
        self.testInit.logOff()
        self.testInit.closeCurrentBrowser()

if __name__ == "__main__":
    suites = unittest.TestSuite()
    suites.addTest(TestCreateClue("testCreateClue"))
    Runner = unittest.TextTestRunner()
    Runner.run(suites)
