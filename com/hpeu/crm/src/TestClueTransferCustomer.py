# coding=UTF-8
'''
Created on 2019年6月4日

@author: lush
'''
from com.hpeu.crm.utils.GetValues import GetValues
from com.hpeu.crm.utils.Init import Init
from com.hpeu.crm.utils.GetScreenShots import GetScreenshots
from com.hpeu.crm.src.TestInit import TestInit
import unittest
from time import sleep

class TestClueTransferCustomer(unittest.TestCase):
    
    def setUp(self):
        self.myDriver=Init().openLoginPage()
        self.getScreenshot=GetScreenshots(self.myDriver)
        self.getValue=GetValues()
        self.testInit=TestInit(self.myDriver)
        self.testInit.login()
        
    def testClueTransferCustomer(self):
        #Open View Clue Page
        viewclueoption=self.getValue.getPageElementValue(4, 11)
        self.myDriver.find_element_by_link_text(viewclueoption).click()
        self.myDriver.implicitly_wait(5)
        sleep(3)
        verifyviewcluepage=self.getValue.getTestDataValue(6, 5)
        assert verifyviewcluepage in self.myDriver.page_source
        
        #Click Transfer Option
        transferoption_xpath=self.getValue.getPageElementValue(16, 2)+self.getValue.getTestDataValue(5, 2)+self.getValue.getPageElementValue(17, 2)
        self.myDriver.find_element_by_xpath(transferoption_xpath).click()
        self.myDriver.implicitly_wait(5)
        sleep(3)

        
        #switch web windows
        handles = self.myDriver.window_handles
        self.myDriver.switch_to.window(handles[1])
        verifyaddcustomer=self.getValue.getTestDataValue(9, 5)
        assert verifyaddcustomer in self.myDriver.page_source
        self.getScreenshot.getScreenshot("AddCustomPage")
        
        #Input customer information
        customername_xpath=self.getValue.getPageElementValue(18, 2)
        customername=self.getValue.getTestDataValue(10, 2)
        self.myDriver.find_element_by_xpath(customername_xpath).send_keys(customername)
        
        comindustry_xpath=self.getValue.getPageElementValue(19, 2)
        self.myDriver.find_element_by_xpath(comindustry_xpath).click()
        
        customerorigin_xpath=self.getValue.getPageElementValue(20, 2)
        customeroriginselection_xpath=self.getValue.getPageElementValue(21, 2)
        self.myDriver.find_element_by_xpath(customerorigin_xpath).click()
        self.myDriver.find_element_by_xpath(customeroriginselection_xpath).click()
        
        companypro_xpath=self.getValue.getPageElementValue(22, 2)
        self.myDriver.find_element_by_xpath(companypro_xpath).click()
        
        contactname_xpath=self.getValue.getPageElementValue(23, 2)
        contactname=self.getValue.getTestDataValue(10, 2)
        self.myDriver.find_element_by_xpath(contactname_xpath).send_keys(contactname)
        
        numofemp_xpath=self.getValue.getPageElementValue(24, 2)
        numofempselection_xpath=self.getValue.getPageElementValue(25, 2)
        self.myDriver.find_element_by_xpath(numofemp_xpath).click()
        self.myDriver.find_element_by_xpath(numofempselection_xpath).click()
        
        createbusiness_xpath=self.getValue.getPageElementValue(26, 2)
        self.myDriver.find_element_by_xpath(createbusiness_xpath).click()
        
        savebtn_xpath=self.getValue.getPageElementValue(27, 2)
        self.myDriver.find_element_by_xpath(savebtn_xpath).click()
        
        self.myDriver.implicitly_wait(5)
        sleep(3)
        verifyaddcusresult = self.getValue.getTestDataValue(10, 5)
        assert verifyaddcusresult in self.myDriver.page_source
        self.getScreenshot.getScreenshot("AddCustomerResult")
        
        #backto previous window
        self.testInit.closeCurrentTab()
        self.myDriver.switch_to.window(handles[0])

    def tearDown(self):
        self.testInit.logOff()
        self.testInit.closeCurrentBrowser()

'''
if __name__ == "__main__":
    suites = unittest.TestSuite()
    suites.addTest(TestClueTransferCustomer("testClueTransferCustomer"))
    runner = unittest.TextTestRunner
    runner.run(suites)
'''         
    
 