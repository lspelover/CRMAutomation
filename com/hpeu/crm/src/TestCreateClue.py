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
        createclueoption_linktext = self.getValue.getPageElementValue("LINK_TEXT", "HomePage_CreateClueOption")
        self.myDriver.find_element_by_link_text(createclueoption_linktext).click()
        sleep(3)
        self.getScreenshot.getScreenshot("CreateCluePage")
        
        #input clue information
        comname_id=self.getValue.getPageElementValue("ID", "CreateCluePage_ComNameBox")
        comname=self.getValue.getTestDataValue("TestData", "CompanyName")
        self.myDriver.find_element_by_id(comname_id).send_keys(comname)
        
        contactname_id=self.getValue.getPageElementValue("ID", "CreateCluePage_ContactNameBox")
        contactname=self.getValue.getTestDataValue("TestData", "ContactName")
        self.myDriver.find_element_by_id(contactname_id).send_keys(contactname)
        
        saltname_xpath=self.getValue.getPageElementValue("XPATH", "CreateCluePage_SaltNameBox")
        saltnameselection_xpath=self.getValue.getPageElementValue("XPATH", "CreateCluePage_SaltNameSelection")
        self.myDriver.find_element_by_xpath(saltname_xpath).click()        
        self.myDriver.find_element_by_xpath(saltnameselection_xpath).click()
        
        mobile_id=self.getValue.getPageElementValue("ID", "CreateCluePage_MobileBox")
        mobile=self.getValue.getTestDataValue("TestData", "MobileNumber")
        self.myDriver.find_element_by_id(mobile_id).send_keys(mobile)
        
        email_xpath=self.getValue.getPageElementValue("XPATH", "CreateCluePage_EmailBox")
        email=self.getValue.getTestDataValue("TestData", "Email")
        self.myDriver.find_element_by_xpath(email_xpath).send_keys(email)

        #click save button
        savebtn_xpath=self.getValue.getPageElementValue("XPATH", "CreateCluePage_SaveButtion")
        self.myDriver.find_element_by_xpath(savebtn_xpath).click()

        self.myDriver.implicitly_wait(5)
        sleep(3)
        self.getScreenshot.getScreenshot("CreateClueResult")
        createclueresult=self.getValue.getTestDataValue("VerifyData", "CreateCluePageData")
        assert createclueresult in self.myDriver.page_source
        
    def tearDown(self):
        self.testInit.logOff()
        self.testInit.closeCurrentBrowser()

if __name__ == "__main__":
    suites = unittest.TestSuite()
    suites.addTest(TestCreateClue("testCreateClue"))
    Runner = unittest.TextTestRunner()
    Runner.run(suites)
