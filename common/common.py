# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:06:35 2015

@author: muou
"""
import sys,os

#"12 34" -> [0x12, 0x34]   
def str2hex(hexstr):
    hexstr = hexstr.strip().replace(' ', '')
    l_hex = []
    if len(hexstr) % 2 != 0:
        return l_hex
    for i in range(0, len(hexstr), 2):
        l_hex.append(int(hexstr[i:i+2], 16))
        
    return l_hex
    
#[0x12, 0x34] -> "1234"  
def hex2str(l_hex):
    l_hexstr = map(lambda x:'{:02x}'.format(x), l_hex)    
    return ''.join(l_hexstr)
    
#获取脚本文件的当前路径
def get_file_dir():
    #获取脚本路径
    path = sys.path[0]
    if os.path.isdir(path):
         return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
        
def find_file(pattern='.pys', base=".", circle=False):  
    '''''查找给定文件夹下面所有 '''  
    if base == ".":  
        base = os.getcwd()  
    print "base:", base
          
    file_list = []  
    cur_list = os.listdir(base)  
    for item in cur_list:              
        full_path = os.path.join(base, item)                 
        # 获取文件名
        if os.path.isfile(full_path):  
            if full_path.endswith(pattern):  
                file_list.append(full_path)  
        else:
            if (True == circle):  
                file_list += find_file(pattern, full_path, circle)  
                
    return file_list
    
def make_sum(l_data):
    #return reduce(lambda x,y: x+y, l_data)
    return sum(l_data)

#low byte hight byte   
#0x2B1A 
def crc16(data):
    crc=0xFFFF #65535
    for j in data:
        crc=crc^j
        #print("crc=%x"%crc)
        for i in range(8):
            if (crc & 1)==1:
                crc =crc >> 1
                crc =crc ^ 0xA001 #40961 多项式
            else:
                crc=crc>>1
    return crc
 
#[01, 02, 03, 04] -> ['a1', '2b']   
def crc16_str(data):
    crc=0xFFFF #65535
    for j in data:
        crc=crc^j
        #print("crc=%x"%crc)
        for i in range(8):
            if (crc & 1)==1:
                crc =crc >> 1
                crc =crc ^ 0xA001 #40961 多项式
            else:
                crc=crc>>1
    low = (crc & 0x00FF)
    high = (crc & 0xFF00) >> 8
    l_crc = ['{:02x}'.format(low), '{:02x}'.format(high)]
    return l_crc
    
#[01, 02, 03, 04] -> [0xa1, 0x2b]    
def crc16_hex(data):
    crc=0xFFFF #65535
    for j in data:
        crc=crc^j
        #print("crc=%x"%crc)
        for i in range(8):
            if (crc & 1)==1:
                crc =crc >> 1
                crc =crc ^ 0xA001 #40961 多项式
            else:
                crc=crc>>1
    low = (crc & 0x00FF)
    high = (crc & 0xFF00) >> 8
    l_crc = [low, high]
    return l_crc
    
if __name__ == '__main__':
    print make_sum([1,2,3,4])
    #print hex(crc16([1,2,3,4]))
    a = crc16_str([1,2,3,4])
    print a
    print crc16_hex([1,2,3,4])
    
    