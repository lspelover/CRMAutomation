# coding=UTF-8
'''
Created on 2019年5月31日

@author: lush
'''

from com.hpeu.crm.utils.GetValues import GetValues
from time import sleep

class TestInit():
    
    getValue = GetValues()
    def __init__(self,object):
        self.driver = object
          
    def login(self):
        username_xpath=self.getValue.getPageElementValue(3, 2)
        username=self.getValue.getTestDataValue(3, 2)
        password_xpath=self.getValue.getPageElementValue(4, 2)
        password=self.getValue.getTestDataValue(4, 2)
        loginbtn_xpath=self.getValue.getPageElementValue(5, 2)
        
        self.driver.find_element_by_xpath(username_xpath).send_keys(username)
        self.driver.find_element_by_xpath(password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(loginbtn_xpath).click()
        self.driver.implicitly_wait(5)
        sleep(3)

    
    def logOff(self):
        logoffbtn_xpath = self.getValue.getPageElementValue(6, 2)
        self.driver.find_element_by_xpath(logoffbtn_xpath).click()
        self.driver.implicitly_wait(5)
        sleep(3)

    def closeCurrentTab(self):
        self.driver.close()
        
    def closeCurrentBrowser(self):
        self.driver.quit()



