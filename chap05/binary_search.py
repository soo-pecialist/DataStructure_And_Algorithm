#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:14:01 2018

@author: Soo Hyeon Kim
"""


def binary_search(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list)//2
        if a_list[midpoint] == item:
            return True
        else: 
            if item < a_list[midpoint]:
                return binary_search(a_list[:midpoint], item)
            else: 
                return binary_search(a_list[midpoint+1:], item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, 53]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))        