# coding=UTF-8
'''
Created on 2019年6月4日

@author: lush
'''
from com.hpeu.crm.src.TestLoginAndLogoff import TestLoginAndLogoff
from com.hpeu.crm.src.TestCreateClue import TestCreateClue
from com.hpeu.crm.src.TestClueModify import TestClueModify
from com.hpeu.crm.src.TestClueTransferCustomer import TestClueTransferCustomer
from com.hpeu.crm.src.TestDeleteClue import TestDeleteClue
import unittest

if __name__ == "__main__":
    suites = unittest.TestSuite()
    suites.addTest(TestLoginAndLogoff("testLoginAndLogOff"))
    #suites.addTest(TestCreateClue("testCreateClue"))
    #suites.addTest(TestClueModify("testCludModify"))
    #suites.addTest(TestClueTransferCustomer("testClueTransferCustomer"))
    #suites.addTest(TestDeleteClue("testDeleteClue"))
    
    Runner=unittest.TextTestRunner()
    Runner.run(suites)
    
    
    