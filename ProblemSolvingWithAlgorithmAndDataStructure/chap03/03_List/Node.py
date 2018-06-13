#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 00:28:46 2018

@author: Soo Hyeon Kim
"""

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def __repr__(self):
        return 'Node: {}'.format(self.data)
    
    def __str__(self):
        return 'Node: {}'.format(self.data)
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next