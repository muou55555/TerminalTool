# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:27:55 2015

@author: muou
"""
import time, os, datetime
from common import common
from helper.pylog import Pylog
from helper.pycfg import Pycfg
from communication.pytelnet import Pytelnet

log = Pylog()

def singleton(cls, *args, **kw):  
    instances = {}  
    def _singleton():  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton  
 
@singleton  
class AppTelnet(object):
    """
        Args: do_connect -> True: connect server now!
    """
    def __init__(self, do_connet = False):
        self.do_connet = do_connet  
        self.IP = "192.168.1.48"
        self.readini()
        self.t = Pytelnet(self.IP)
        self.con = None
        if self.do_connet:
            self.connect()   
            
    def readini(self):
        cfgfile = "cfg.ini"
        SEC = "TELNET"
        KEY = "IP"
        cfg = Pycfg()
        fp = open(cfgfile)
        cfg.readfp(fp)
        self.IP = cfg.get_str(SEC, KEY, "192.168.1.48")     
        fp.close()
       
    def connect(self):
        if self.con is not None:
            log.info("Connect had been OK!")
            return self.con
            
        print "Connect " + self.IP + "..."
        self.con = self.t.connect()
        log.debug("id(self.con) = %d" % id(self.con))
        if self.con is None:
            log.result("Connect Fail")
        else:
            log.result("Connect OK!")
            
    def close(self):
        if self.con is None:
            log.info("Connect has been closed")
            return
        self.t.close(self.con)
        self.con = None
        log.result("Close telnet OK!")
    
        
    def run_cmd(self, cmd = None, is_print = True):
        #print self.do_connet   
        if self.con is None:
            print "Warning: Please connect server firstly..."
            return
        #print "id(t) = ", id(self.t)
        #print "id(con) = ", id(self.con)
        if cmd is None:
            cmd = raw_input("Input cmd:")
            if len(cmd) == 0:
                return
            if is_print == True:
                print "Run cmd: ", cmd
            cmd += "\n"
            pass
        else:
            pass         
        
        output = self.t.run(self.con, cmd)
        if is_print == True:
            print "Cmd Return:"
            print output
        return output
        
    def running_cmd(self):
        #print self.do_connet   
        if self.con is None:
            print "Warning: Please connect server firstly..."
            return
        while True:
            cmd = raw_input("Input cmd:")
            if len(cmd) == 0:
                return
            cmd += "\n"
            #print "Run cmd: ", cmd
            output = self.t.run(self.con, cmd)
            print "Cmd Return:"
            print output
            
    def run_pys(self, logfile = "pys.log"):
        DEL = '@'
        total = 0
        f_log = open(logfile, 'w')
        f_log.write("run time:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
        f_log.write("-------------------------------\n")
        filelist = common.find_file()
        for fl in filelist:
            print "Run filename: ", os.path.split(fl)[1]
            f = open(fl, "r")
            f.seek(0)
            i = 0
            errcnt = 0
            for each_line in f.readlines():
                if len(each_line.strip()) <= 0:
                    continue
                i += 1
                l_line = each_line.strip().split(DEL, 2)                
                retcode = ""
                retstr = "OK"
                if len(l_line) > 1 :
                    retcode = l_line[0].strip()
                    cmd = l_line[1].strip() 
                else:
                    cmd = l_line[0].strip()
                result = self.run_cmd(cmd+"\n", False)
                if retcode != "" and result.find(retcode) == -1:
                    retstr = "FAIL"
                    errcnt += 1
                print "[%s][%03d][%s]: %s\n" % (os.path.split(fl)[1], i, retstr, cmd)
                f_log.write("[%s][%03d][%s]: %s\n" % (os.path.split(fl)[1], i, retstr, cmd))
                f_log.write(result + "\n\n")
            f.close()
            total += i
        log.result("total = %d fail = %d" % (total, errcnt)) 
        f_log.write("-------------------------------\n")
        f_log.write("total = %d fail = %d\n" % (total, errcnt))    
        f_log.close()            
                
    def check_rtc(self):
        s = ["0", "1"]
        for i in range(2):
            output = self.run_cmd("hwclock -r\n", False)
            if output is None:
                print "Maybe not connect server!"
                return None
            if output.find("seconds") == -1:
                print "Check rtc fail"
                return False
            l = output.split("\n")
            for str in l:
                if str.find("seconds") != -1:
                    s[i] = str
                    #print s[i]
                    break
            time.sleep(1.5)
                
        if s[0] == s[1]:
            log.result("Rtc Error!")
            return False
        else:
            log.result("Rtc OK")
            return True
            
    def kill_process(self, name = "concentrator"):
        #ps -e | grep concentrator | grep -v grep | awk '{print $1}' | sed 's,^,kill -9 ,g' | sh
        cmd = "ps -e | grep " + name + " | grep -v grep | awk '{print $1}' | sed 's,^,kill -9 ,g' | sh"
        result = self.run_cmd(cmd+"\n", False)
        if result is None:
            return
        print result
        log.result("Kill concentrator OK")
        
    def check_app_status(self, name = "concentrator"):
        cmd = "ps -e | grep " + name + " | grep -v grep"
        result = self.run_cmd(cmd+"\n", False)
        if result is None:
            return
        #print result
        if result.find("./" + name) == -1:
            log.result("Application ERROR")
        else:
            log.result("Application OK")         
            
    def check_db(self):
        cmd = "ls -l /mnt/Nand1/conDb_V2.db  | awk '{print $5}'"
        result = self.run_cmd(cmd+"\n", False)
        if result is None:
            return
        #print result
        if result.find("No such file") != -1:
            log.result("DB ERROR - Not found db file!")
        r_l = result.splitlines()
        size = 0
        for l in r_l:
            if l.isdigit() == True:
                size = int(l)
        if (size < 295936):
            log.result("DB ERROR - file size: %d error!" % size)
            return
        log.result("DB OK") 
        
    def device_status(self):
        print "Checking device status..."
        self.check_app_status()
        self.check_rtc()  
        self.check_db()
        print "Check device finish"
        
    def init_db(self):
        result = self.run_cmd("cp -f database.bak /mnt/Nand1/conDb_V2.db\n", False)
        if result is None:
            return
        if result.find("overwrite") != -1:
            result = self.run_cmd("y\n", False)
        if result.find("No such file") != -1:
             log.result("Not found database.bak. Please upload it!") 
             return            
        log.result("Init db OK")       
        
        
#if __name__ == '__main__':
#    a = AppTelnet()
#    a.test_g()
#    print id(a)
#    b = AppTelnet()
#    b.test_g()
#    print id(b)
        
        
        
        
        