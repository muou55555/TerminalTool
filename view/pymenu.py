#!/bin/env python
# -*- coding: utf-8 -*-
"""
Created on  Dec 13 19:02:23 2015

@author: muou
"""
__version__ = '1.0.0'


from pytable import Pytable
import collections

class Pymenu:
    def __init__(self, title, l_colslen, padding = " ", back_key = "0"):
        self.back_key = back_key
        self.prekey = back_key 
        self.title = title
        self.l_colslen = l_colslen
        self.width = 0
        for w in l_colslen:
            self.width += w
        #Dictionary that remembers insertion order
        self.dict_fields = collections.OrderedDict()
        
    def add_field(self, key, name, f):
        assert(isinstance(key, str))
        assert(isinstance(name, str))
        self.dict_fields[key] = [name, f]

    def print_fields(self):
        #print self.dict_fields.items()
        for (k, v) in self.dict_fields.items():
            print "dict[%s] =" % k, v, v[1]()   
            
    def show(self):        
        while True:
            a = Pytable(self.title, self.width, self.l_colslen)
            a.add_table_header()
            l_data = []
            i = 0
            for (k, v) in self.dict_fields.items():    
               l_data.append("[" + k + "] - " + v[0])
               i += 1
               if (i % len(self.l_colslen) == 0 ):
                   a.add_row_data(l_data)
                   del l_data[:]
            if (len(l_data) > 0):
                a.add_row_data(l_data)
                del l_data[:]
                 
            a.show()
            
            key = raw_input("Select Key[%s]: " % (self.prekey))
            
            if len(key) == 0: #not press any key
                curkey = self.prekey
            else:
                curkey = key

            #Back key handle
            if curkey == self.back_key:
                self.prekey = curkey
                isquit = True
                if (self.dict_fields[curkey][1]) :
                    isquit = self.dict_fields[curkey][1]()
                if isquit == True or isquit == None:
                    return
                else:
                    continue
                return;      
                
            #not match any key   
            if (self.dict_fields.has_key(curkey) == False):
                continue

            self.prekey = curkey
            
            if (self.dict_fields[curkey][1]):
                self.dict_fields[curkey][1]()
            

def f_quit():
    c = raw_input("Quit? y or n :")
    if c.lower() == "y" :
        return True
    else:
        return False
        
def ff():
    print "ff() run..."
def f(s):
    print s   
'''        
if __name__ == '__main__':
     m = Pymenu("Main Menu", [20, 20, 20], back_key = "q")
     m.add_field("1", "start", lambda:f("start"))
     m.add_field("2", "stop", lambda:f("stop"))
     m.add_field("3", "key3", lambda:f("key3"))
     m.add_field("4", "key4", ff)
     m.add_field("5", "key5", lambda:f("key5"))
     m.add_field("6", "Submenu", lambda:f("Submenu"))
    
     
     m2 = Pymenu("Submenu", [20, 20, 20],  back_key = "0")
     m2.add_field("a", "sub a", lambda:f("sub a"))
     m2.add_field("b", "sub b", None) 
     m2.add_field("0", "Back", lambda:f("Back"))
      
     m.add_field("s", "submenu", m2.show)
     m.add_field("q", "Quit", f_quit)
     m.show()
'''

