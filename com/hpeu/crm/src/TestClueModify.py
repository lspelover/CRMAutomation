# coding=UTF-8
'''
Created on 2019年6月4日

@author: lush
'''
from com.hpeu.crm.src.TestInit import TestInit
from com.hpeu.crm.utils.GetScreenShots import GetScreenshots
from com.hpeu.crm.utils.GetValues import GetValues
from com.hpeu.crm.utils.Init import Init
import unittest
from time import sleep
import datetime
from selenium.webdriver.common.keys import Keys

class TestClueModify(unittest.TestCase):
    
    def setUp(self):
        self.myDriver=Init().openLoginPage()
        self.getScreenshot=GetScreenshots(self.myDriver)
        self.getValue=GetValues()
        self.testInit=TestInit(self.myDriver)
        self.testInit.login()
        
    def testCludModify(self):
        #Open View Clue Page
        viewclueoption=self.getValue.getPageElementValue(4, 11)
        self.myDriver.find_element_by_link_text(viewclueoption).click()
        self.myDriver.implicitly_wait(5)
        sleep(3)
        verifyviewcluepage=self.getValue.getTestDataValue(6, 5)
        assert verifyviewcluepage in self.myDriver.page_source
        
        #click Modify option to goto modify page
        cludemodify_xpath=self.getValue.getPageElementValue(11, 2)+self.getValue.getTestDataValue(5, 2)+self.getValue.getPageElementValue(12, 2)
        self.myDriver.find_element_by_xpath(cludemodify_xpath).click()
        self.myDriver.implicitly_wait(5)
        sleep(3)
        verifycludmodifypage=self.getValue.getTestDataValue(7, 5)
        assert verifycludmodifypage in self.myDriver.page_source
        self.getScreenshot.getScreenshot("CludModifyPage")
        
        #Input Clue Modify - text information
        textarea_xpath=self.getValue.getPageElementValue(13, 2)
        textarea_content=self.getValue.getTestDataValue(9, 2)
        self.myDriver.find_element_by_xpath(textarea_xpath).clear()
        self.myDriver.find_element_by_xpath(textarea_xpath).send_keys(textarea_content)
        
        #Input Clue Modify - next contact time information
        Next_Step_Time=(datetime.datetime.now() + datetime.timedelta(days = +10)).strftime("%Y-%m-%d")
        nexttimebox_xpath=self.getValue.getPageElementValue(14, 2)
        self.myDriver.find_element_by_xpath(nexttimebox_xpath).clear()
        self.myDriver.find_element_by_xpath(nexttimebox_xpath).send_keys(Next_Step_Time)
        self.myDriver.find_element_by_xpath(nexttimebox_xpath).send_keys(Keys.ENTER)
        
        self.myDriver.implicitly_wait(5)
        sleep(3)
        self.getScreenshot.getScreenshot("CludeModifResult")
        verifycluemodifyresult=self.getValue.getTestDataValue(8, 5)
        assert verifycluemodifyresult in self.myDriver.page_source
        
        # Back to view clue page
        backbtn_xpath=self.getValue.getPageElementValue(15, 2)
        self.myDriver.find_element_by_xpath(backbtn_xpath).click()
        self.myDriver.implicitly_wait(5)
        sleep(3)
        
    def tearDown(self):
        self.testInit.logOff()
        self.testInit.closeCurrentBrowser()
 
'''  
if __name__ == "__main__":
    suites=unittest.TestSuite()
    suites.addTest(TestClueModify("testCludModify"))
    runner=unittest.TextTestRunner()
    runner.run(suites)
''' 
