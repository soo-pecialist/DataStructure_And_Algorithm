#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 22:31:06 2018

@author: Soo Hyeon Kim
"""

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):        
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                print(a_list)

def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                exchanges = True
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                print(a_list)
        pass_num -= 1


### [Test1] - bubble_sort
#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#print(a_list)
#bubble_sort(a_list)
#print(a_list)
#print()
#
### [Test2] - short_bubble_sort
#a_list=[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
##a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#print(a_list)
#short_bubble_sort(a_list)
#print(a_list)

                