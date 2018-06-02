#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:36:07 2018

@author: Soo Hyeon Kim
"""

import Stack

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    
    assert base > 1 and base <= 16, \
            "Base is between 2 to 16"
    
    rem_stack = Stack.Stack()
    
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base
        
    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
        
    return new_string

print("Decimal to {}-nary: {} -> {}".format(2, 25, base_converter(25,2)))
print("Decimal to {}-nary: {} -> {}".format(16, 250, base_converter(250,16)))
print("Decimal to {}-nary: {} -> {}".format(8, 2598, base_converter(2598,8)))