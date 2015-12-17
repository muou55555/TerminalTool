#!/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:52:00 2015

@author: muou
"""
__version__ = '1.0.0'
import os
import ConfigParser
class Pycfg(ConfigParser.ConfigParser):
    
    def get_int(self, section, key, default):
        try:
            value = self.getint(section, key)
        except:
            value = default
        return value            
   
    def get_str(self, section, key, default):
        try:
            value = self.get(section, key)
        except:
            value = default
        return value         
        
#if __name__ == '__main__':
#    cfg = Pycfg()
#    print os.getcwd()
#    fp = open("../cfg.ini")
#    cfg.readfp(fp)
#    print cfg.get("TELNET", "IP")
#    print cfg.get_str("TELNET", "PORT", 1)
#    fp.close()
