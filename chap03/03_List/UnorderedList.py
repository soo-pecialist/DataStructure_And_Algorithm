#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 00:40:03 2018

@author: Soo Hyeon Kim
"""
import Node

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        try:
            entries = []
            entries.append(self.head.get_data())
            next_entry = self.head.get_next()
            while next_entry != None:
                entries.append(next_entry.get_data())
                next_entry = next_entry.get_next()
            return 'UnorderedList of size {}: \n{}'.format(len(entries), entries)
        except Exception:
            return ''
    
    def __str__(self):
        try:
            entries = []
            entries.append(self.head.get_data())
            next_entry = self.head.get_next()
            while next_entry != None:
                entries.append(next_entry.get_data())
                next_entry = next_entry.get_next()
            return 'UnorderedList of size {}: \n{}'.format(len(entries), entries)
        except Exception:
            return ''
        
    def is_empty(self):
        return self.head == None 
    
    def add(self, item):
        temp = Node.Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        result = None
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        result = current
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return result
    
## [TEST]
#import random
#test = UnorderedList()
#random.seed(19120) # pick seed arbitrarily
#for i in range(20):
#    ran = random.randint(-20, 20)
#    test.add(ran)
#    print("added {:3}".format(ran))
#print(test)    
#print("size?", test.size())
#ran = random.randint(-20, 20)
#while not test.search(ran): 
#    ran = random.randint(-20, 20)
#print("search {}:".format(ran), test.search(ran))
#print(test)
#removed = test.remove(ran)
#print("remove {}:".format(ran))
#print(test)
##print("removed entry: {}".format(removed))

    