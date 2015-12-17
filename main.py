#!/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:01:14 2015

@author: muou
"""
__version__ = '1.0.0'
__author__ = 'muou'
__email__ = 'muou55555@163.com'
__url__ = 'https://github.com/muou55555/TerminalTool'
__description__ = __doc__

from helper.pylog import Pylog
from view.pymenu import Pymenu
from application.apptelnet import AppTelnet

def f_quit():
    c = raw_input("Quit? y or n :")
    if c.lower() == "y" :
        return True
    else:
        return False
        
def fun_test():
    print "fun_test() Run..."
    t = AppTelnet("192.168.1.46")
    t.test()
    
def fun(s):
    print s      
     
if __name__ == '__main__':
     #logging.basicConfig(level=logging.DEBUG, format='%(module)s %(levelname)s: %(message)s')
     log = Pylog(level=2)   
    
     main_menu = Pymenu("Main Menu", [20, 30, 30], back_key = "q")
     
     telnet_menu = Pymenu("Telnet Menu", [20, 30, 30],  back_key = "0")
     telnet_menu.add_field("1", "Connect",  lambda:AppTelnet().connect())
     telnet_menu.add_field("2", "Close", lambda:AppTelnet().close()) 
     telnet_menu.add_field("3", "Run One Commond", lambda:AppTelnet().run_cmd()) 
     telnet_menu.add_field("4", "Run Commond", lambda:AppTelnet().running_cmd()) 
     telnet_menu.add_field("5", "Run Script", lambda:AppTelnet().run_pys())
     telnet_menu.add_field("6", "Check Rtc", lambda:AppTelnet().check_rtc())  
     telnet_menu.add_field("7", "Kill App", lambda:AppTelnet().kill_process("concentrator")) 
     telnet_menu.add_field("8", "Device Status", lambda:AppTelnet().device_status()) 
     telnet_menu.add_field("9", "Init DB", lambda:AppTelnet().init_db()) 
     telnet_menu.add_field("0", "Back", lambda:fun("Back"))
     
     main_menu.add_field("1", "Telnet", telnet_menu.show)
     main_menu.add_field("2", "Ftp", lambda:AppTelnet().run_cmd("date\n"))
     main_menu.add_field("3", "Serial", lambda:fun("Serial"))
     main_menu.add_field("4", "SSH", fun_test)
     main_menu.add_field("5", "Mbus", lambda:fun("Mbus"))
     main_menu.add_field("6", "Settings", lambda:fun("Settings"))
     main_menu.add_field("q", "Quit", f_quit)

     main_menu.show()

