# coding=UTF-8
'''
Created on 2019年5月31日

@author: lush
'''

from com.hpeu.crm.utils.GetValues import GetValues
from time import sleep

class TestInit():
    
    getValue = GetValues()
          
    def login(self,driver):
        username_xpath=self.getValue.getPageElementValue("XPATH", "LoginPage_LoginNameBox")
        username=self.getValue.getTestDataValue("TestData", "UserName")
        password_xpath=self.getValue.getPageElementValue("XPATH", "LoginPage_PasswordBox")
        password=self.getValue.getTestDataValue("TestData", "PassWord")
        loginbtn_xpath=self.getValue.getPageElementValue("XPATH", "LoginPage_LoginButton")
        
        driver.find_element_by_xpath(username_xpath).send_keys(username)
        driver.find_element_by_xpath(password_xpath).send_keys(password)
        driver.find_element_by_xpath(loginbtn_xpath).click()
        driver.implicitly_wait(5)
        sleep(3)

    
    def logOff(self,driver):
        logoffbtn_xpath = self.getValue.getPageElementValue("XPATH", "HomePage_LogOffOption")
        driver.find_element_by_xpath(logoffbtn_xpath).click()
        driver.implicitly_wait(5)
        sleep(3)

    def closeCurrentTab(self,driver):
        driver.close()
        
    def closeCurrentBrowser(self,driver):
        driver.quit()



