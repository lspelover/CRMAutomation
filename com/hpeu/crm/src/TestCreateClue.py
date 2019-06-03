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
        self.getScreenshot = GetScreenshots(self.myDriver)
        self.myDriver = Init().openLoginPage()
        
        TestInit.login(self, self.myDriver)

    def testCreateClue(self):
        createclueoption_linktext = self.getValue.getPageElementValue("LINK_TEXT", "HomePage_CreateClueOption")
        self.myDriver.find_element_by_link_text(createclueoption_linktext).click()
        sleep(3)
        self.getScreenshot.getScreenshot("CreateCluePage")
        
    def tearDown(self):
        TestInit().logOff(self.myDriver)
        TestInit().closeCurrentTab(self.myDriver)

if __name__ == "__main__":
    suites = unittest.TestSuite()
    suites.addTest(TestCreateClue("testCreateClue"))
    Runner = unittest.TextTestRunner()
    Runner.run(suites)
