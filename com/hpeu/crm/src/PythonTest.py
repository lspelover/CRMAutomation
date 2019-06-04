# coding=UTF-8
'''
Created on 2019年6月3日

@author: lushipeng
'''
from com.hpeu.crm.utils.GetValues import GetValues

getValue = GetValues()
print(getValue.getPageElementValue(11, 2)+getValue.getTestDataValue(5, 2)+getValue.getPageElementValue(12, 2))
print(getValue.getPageElementValue(15, 2))
