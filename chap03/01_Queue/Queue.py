#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 18:55:49 2018

@author: Soo Hyeon Kim
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def __repr__(self):
        return 'Queue: {}'.format(self.items)
    
    def __str__(self):
        return 'Queue: {}'.format(self.items)
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
## [TEST]
#q = Queue()
#q.enqueue('hello')
#q.enqueue('dog')
#q.enqueue(3)
#q.dequeue()
        