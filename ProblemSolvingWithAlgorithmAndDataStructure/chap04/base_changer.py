#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 23:20:44 2018

@author: Soo Hyeon Kim
"""

def base_changer(n, base):
    assert type(n) == int and type(base) == int, "Input must be INTEGER"
    assert base <= 16, "Please set base up to 16"

    convert_string = "01234567890ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return base_changer(n//base, base) + convert_string[n % base]
    
## [Test]
#print(base_changer(1453, 16)) # '50C'
#print(base_changer(10, 2)) # '1010
#print(base_changer(182730, 12)) # '898A6'
#print(base_changer(268920, 2)) # '1000001101001111000'
    