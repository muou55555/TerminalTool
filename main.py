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

from view.pymenu import Pymenu

def f_quit():
    c = raw_input("Quit? y or n :")
    if c.lower() == "y" :
        return True
    else:
        return False
        
def fun_test():
    print "fun_test() Run..."
    
def fun(s):
    print s      
     
if __name__ == '__main__':
     main_menu = Pymenu("Main Menu", [20, 20, 20], back_key = "q")
     main_menu.add_field("1", "Telnet", lambda:fun("Telnet"))
     main_menu.add_field("2", "Ftp", lambda:fun("Ftp"))
     main_menu.add_field("3", "Serial", lambda:fun("Serial"))
     main_menu.add_field("4", "SSH", fun_test)
     main_menu.add_field("5", "Mbus", lambda:fun("Mbus"))
     main_menu.add_field("6", "Settings", lambda:fun("Settings"))
     
     sub_menu = Pymenu("SubMenu", [20, 20, 20],  back_key = "0")
     sub_menu.add_field("a", "sub a", lambda:fun("sub a"))
     sub_menu.add_field("b", "sub b", None) 
     sub_menu.add_field("c", "sub c", None) 
     sub_menu.add_field("0", "Back", lambda:fun("Back"))
     
     main_menu.add_field("s", "Submenu", sub_menu.show)
     main_menu.add_field("q", "Quit", f_quit)

     main_menu.show()

