#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 01:26:32 2018

@author: Soo Hyeon Kim
"""

import Deque

def pal_checker(a_string):
    char_deque = Deque.Deque()
    
    for ch in a_string:
        char_deque.add_rear(ch)
    
    still_equal = True
    
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False
            
    return still_equal

##[TEST}
print("sdkjfskf: {}".format(pal_checker("lsdkjfskf")))
print("radar: {}".format(pal_checker("radar")))