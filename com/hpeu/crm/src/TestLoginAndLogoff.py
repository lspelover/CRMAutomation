# coding=UTF-8
'''
Created on 2019年6月4日

@author: lushipeng
'''
from com.hpeu.crm.src.TestInit import TestInit
from com.hpeu.crm.utils.GetValues import GetValues
from com.hpeu.crm.utils.Init import Init
from com.hpeu.crm.utils.GetScreenShots import GetScreenshots
import unittest

class TestLoginAndLogoff(unittest.TestCase):
    def setUp(self):
        self.myDriver=Init().openLoginPage()
        self.getValue=GetValues()
        self.getScreenshot=GetScreenshots(self.myDriver)
        self.getScreenshot.getScreenshot("LoginPage")
        self.testInit=TestInit(self.myDriver)
        
    def testLoginAndLogOff(self):
        self.testInit.login()
        self.getScreenshot.getScreenshot("HomePage")
        
        self.testInit.logOff()
        self.getScreenshot.getScreenshot("LogOffPage")
        
    def tearDown(self):
        self.testInit.closeCurrentBrowser()

if __name__ == "__main__":
    suites = unittest.TestSuite()
    suites.addTest(TestLoginAndLogoff("testLoginAndLogOff"))
    Runner = unittest.TextTestRunner()
    Runner.run(suites)
    
        
        