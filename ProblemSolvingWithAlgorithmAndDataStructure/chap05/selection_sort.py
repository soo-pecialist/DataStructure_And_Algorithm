#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 22:48:52 2018

@author: Soo Hyeon Kim
"""

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1): # every last pos
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location # keep track of it at each iteration
        
        a_list[pos_of_max], a_list[fill_slot] = \
                    a_list[fill_slot], a_list[pos_of_max]
    
## [TEST]
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(a_list)
selection_sort(a_list)
print(a_list)
