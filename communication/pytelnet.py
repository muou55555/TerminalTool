# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:11:23 2015

@author: user
"""
import time,os
import telnetlib

TELNET_TIMEOUT = 5
TELNET_READ_TIMEOUT = 2

#def singleton(cls, *args, **kw):  
#    instances = {}  
#    def _singleton():  
#        if cls not in instances:  
#            instances[cls] = cls(*args, **kw)  
#        return instances[cls]  
#    return _singleton  
# 
#@singleton 

class Pytelnet(object):
    
    def __init__(self, ip="192.168.1.48", port=23, user="root", pwd="Internet", endstr="[root@(none) concentrator]$"):
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd
        self.endstr = endstr
        self.con = None
    
    def __str__(self):
        return self.ip + "," + self.user + "," + self.pwd + "," + self.endstr
    
    def connect(self):
        # Logging into device
        #if self.con is not None:
        #    return self.con
        self.con = telnetlib.Telnet(self.ip, self.port, TELNET_TIMEOUT)        
        
        self.con.read_until("Username:", TELNET_READ_TIMEOUT)
        self.con.write(self.user + "\n")
        self.con.read_until("Password:", TELNET_READ_TIMEOUT)
        self.con.write(self.pwd + "\n")
        time.sleep(1)
        self.con.read_very_eager()
        return self.con
    
    def run(self, connect, cmd):
        if connect is None:
            print "Error: connect is None\n"
            return
        connect.write(cmd)
        time.sleep(1)
         # Test for reading command output
         #output = connection.read_very_eager()
        output = connect.read_until(self.endstr, TELNET_READ_TIMEOUT)
        #print "again:" + connect.read_until(self.endstr, 1)
        return output
        #print output
        #print "finish run cmd"
        
    def close(self, connect):
        self.con = None
        if connect is None:
            print "Connect has been closed\n"
            return
        connect.close()
        

         
         