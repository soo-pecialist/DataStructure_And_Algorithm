#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:19:59 2018

@author: Soo Hyeon Kim
"""

import Stack

def parentheses_checker(symbol_string):
    s = Stack.Stack()
    balanced = True
    index = 0
    
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else: # ')]}'
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False
    
def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)    
    
## [TEST]
print('((())):',parentheses_checker('((()))'))
print('(():', parentheses_checker('(()'))
print('{{([][])}()}: ', parentheses_checker('{{([][])}()}'))
print('[{()]:', parentheses_checker('[{()]'))
