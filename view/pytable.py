#!/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:03:18 2015

@author: muou
"""
__version__ = '1.0.0'

class Pytable(object):
    
    def __init__(self, title, width, l_colslen, padding = " "):
        """ Initiaion table
        Args:
            title: Head content
            width: table width; equal sum(l_colslen)
            l_colslen: length of colomns. eg.[10, 20 ,30] indicates three colomns
            padding: data field left padding
        Returns:
            none
        """
        pass
    
        self.title = title
        self.width = width
        self.l_colslen = l_colslen
        self.prt_tbl_str = ""
        self.DIVIDE = "+"
        self.LINE = "-"
        self.HEADLINE = "="   
        self.EDGE = "|"
        self.PADDING = padding
        
    def print_line(self, n, c):
        for line in range(n):
            self.prt_tbl_str += c
            
    def print_title(self, n, title):
        self.print_line(n, self.HEADLINE)
        self.prt_tbl_str += "\n"
        self.prt_tbl_str += ("+" + title.center(n-2) + "+")
        #self.prt_tbl_str += title
        self.prt_tbl_str += "\n"
        self.print_line(n, self.HEADLINE)
        self.prt_tbl_str += "\n"
            
    def print_divide_line(self, l_fieldlen):
        for l in l_fieldlen:
            assert(isinstance(l, int))
            self.prt_tbl_str += self.DIVIDE
            self.print_line(l, self.LINE)
            #print "Value:",l
        self.prt_tbl_str += self.DIVIDE
        self.prt_tbl_str += "\n"
        
    def print_row_data(self, l_field):
        self.prt_tbl_str += self.EDGE
        col = 0
        for l in l_field:
            assert(isinstance(l, str))
            padding = self.PADDING + l
            self.prt_tbl_str +=  padding
            self.prt_tbl_str += (self.EDGE.rjust(self.l_colslen[col] - len(padding) + len(self.EDGE)))
            col += 1
        #data columns less than total columns
        while ((len(self.l_colslen) - col) > 0):
            padding = self.PADDING
            self.prt_tbl_str +=  padding
            self.prt_tbl_str += (self.EDGE.rjust(self.l_colslen[col] - len(padding) + len(self.EDGE)))
            col += 1
        
        self.prt_tbl_str += "\n"
            
        
    def print_table(self):
        self.print_title(self.width + len(self.l_colslen) + len(self.EDGE), self.title)
        self.print_divide_line(self.l_colslen)
        l_str = ["st", "stop", "pause"]
        self.print_row_data(l_str)
        self.print_divide_line(self.l_colslen)
        #pass
        
    def show(self):
        print self.prt_tbl_str
        
    def add_table_header(self):
        self.print_title(self.width + len(self.l_colslen) + len(self.EDGE), self.title)
        
    def add_row_data(self, l_data):
        assert(len(l_data) <= len(self.l_colslen))
        #self.print_divide_line(self.l_colslen)
        self.print_row_data(l_data)
        self.print_divide_line(self.l_colslen)
        
    def __str__(self):
        #self.print_table()
        return self.prt_tbl_str
 
'''       
if __name__ == '__main__':
    a = Pytable("Table Title", 60, [10, 20, 30])
    a.add_table_header()
    a.add_row_data(["1 - Home", "2 - Connect", "3 - Stop"])
    a.add_row_data(["4 - Home", "5 - Connect", "6 - Stop"])
    a.add_row_data(["7 - Home"])
    a.show()
'''
