#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:08:01 2018

@author: Soo Hyeon Kim
"""

import Queue

def hot_potato(name_list, num):
    sim_queue = Queue.Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        
        sim_queue.dequeue()
    
    return sim_queue.dequeue()

##[TEST]
names = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
print(names, hot_potato(names, 7))