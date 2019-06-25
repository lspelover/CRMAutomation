# coding=utf-8
'''
Created on 2019年6月25日

@author: lush
'''
import time

class getTime():
    def getCurrentTime(self):
        return  time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    def getCurrentDate(self):
        return time.strftime("%Y%m%d",time.localtime(time.time()))