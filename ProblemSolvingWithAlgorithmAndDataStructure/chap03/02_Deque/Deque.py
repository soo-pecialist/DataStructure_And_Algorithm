#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 00:22:43 2018

@author: Soo Hyeon Kim
"""

class Deque:
    def __init__(self):
        self.items = []
    
    def __repr__(self):
        return 'Deque: rear {} front'.format(self.items)
    
    def __str__(self):
        return 'Deque: rear {} front'.format(self.items)
    
    def is_empty(self):
        return self.items == []
    
    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0, item)
    
    def remove_front(self):
        popped, self.items = self.items[-1], self.items[:-1]
        return popped
    
    def remove_rear(self):
        popped, self.items = self.items[0], self.items[1:]
        return popped
    
    def size(self):
        return len(self.items)
    