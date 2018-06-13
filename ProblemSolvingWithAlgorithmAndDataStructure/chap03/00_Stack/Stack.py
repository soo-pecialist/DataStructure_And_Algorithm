#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:03:00 2018

@author: Soo Hyeon Kim
"""

class Stack:
    ## bottom - top
    def __init__(self):
        self.items = []
    
    def __repr__(self):
        return 'Stack: B{}T'.format(self.items)
    
    def __str__(self):
        return 'Stack: B{}T'.format(self.items)
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
##[TEST]
#s = Stack()
#print(s)
#s.push('Hello')
#print(s)
#s.push(5.2)
#print(s)
#s.push(8)
#print(s)
#s.pop()
#print(s)
#s.push(-99)
#print(s)