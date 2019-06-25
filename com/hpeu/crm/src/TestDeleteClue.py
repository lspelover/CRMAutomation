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

class TestDeleteClue(unittest.TestCase):
    
    def setUp(self):
        self.myDriver=Init().openLoginPage()
        self.getScreenshot=GetScreenshots(self.myDriver)
        self.getValue=GetValues()
        self.testInit=TestInit(self.myDriver)
        self.testInit.login()
        
    def testDeleteClue(self):
        #Open View Clue Page
        viewclueoption=self.getValue.getPageElementValue(4, 11)
        self.myDriver.find_element_by_link_text(viewclueoption).click()
        self.myDriver.implicitly_wait(5)
        sleep(3)
        verifyviewcluepage=self.getValue.getTestDataValue(6, 5)
        assert verifyviewcluepage in self.myDriver.page_source
        
        if self.getValue.getTestDataValue(5, 2) not in self.myDriver.page_source:
            pass
        else:
            #click Delete option
            cluecheckbox_xpath=self.getValue.getPageElementValue(28, 2)+self.getValue.getTestDataValue(5, 2)+self.getValue.getPageElementValue(29, 2)
            self.myDriver.find_element_by_xpath(cluecheckbox_xpath).click()
            
            clueoption_xpath=self.getValue.getPageElementValue(30, 2)
            cluedelete_xpath=self.getValue.getPageElementValue(31, 2)
            self.myDriver.find_element_by_xpath(clueoption_xpath).click()
            self.myDriver.find_element_by_xpath(cluedelete_xpath).click()
        
            #accept delete
            current_handle=self.myDriver.current_window_handle
            
            self.myDriver.switch_to.alert.accept()
            self.myDriver.switch_to.window(current_handle)
            self.myDriver.implicitly_wait(5)
            sleep(3)
            verifycluedelete = self.getValue.getTestDataValue(11, 5)
            assert verifycluedelete in self.myDriver.page_source
            self.getScreenshot.getScreenshot("ClueDeleteResult")
    
    def tearDown(self):
        self.testInit.logOff()
        self.testInit.closeCurrentBrowser()
