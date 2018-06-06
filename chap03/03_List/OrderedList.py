#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 21:59:25 2018

@author: Soo Hyeon Kim
"""

import Node

class OrderedList:
    # ascending order
    
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
            return 'OrderedList of size {}: \n{}'.format(len(entries), entries)
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
            return 'OrderedList of size {}: \n{}'.format(len(entries), entries)
        except Exception:
            return ''
        
    def is_empty(self):
        return self.head == None 
    
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
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() >= item:
                stop = True
            else: 
                previous = current
                current = current.get_next()
        
        temp = Node.Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
    
    def index(self, item):   
        if self.search(item):
            current = self.head
            found = False
            idx = 0

            while not found:
                if current.get_data() == item:
                    found = True
                else:
                    current = current.get_next()
                    idx += 1
            return idx
        else:
            print('None founded')
            return None
    
    def pop(self, pos = -1):  
        temp = None
        current = self.head

        if pos != -1: # index given
            previous = None
            
            if pos == 0: # 1st item
                temp = current # return item
                current = current.get_next()
            
            idx = 1
            previous = current
            current = previous.get_next()
            found = False
            
            while not found:
                if idx == pos:
                    temp = current # return item
                    previous.set_next(current.get_next())
                    found = True
                else:
                    idx += 1
                    previous = current
                    current = current.get_next()
        
        else: # if pos == -1: # index not given
            while current.get_next().get_next() != None:
                current = current.get_next()
            
            temp = current.get_next() # return item
            current.set_next(None)
        
        if temp: #not None
            return temp.get_data()
        else:
            return None
    
## [Test]
#import random
#test = OrderedList()
#random.seed(1225) # pick seed as you please
#for i in range(20):
#    ran = random.randint(-20, 20)
#    test.add(ran)
#    print("added {:3}".format(ran))
#print(test)
#print()
#print("size?", test.size())
#print()
#ran = random.randint(-20, 20)
#print("{} exists?".format(ran), test.search(ran))
#print()
#while not test.search(ran):
#    ran = random.randint(-20, 20)
#print("search {}: {}, index is {}".format(ran, test.search(ran), test.index(ran)))
#print("pop({}), popped item: {}".format(test.index(ran), test.pop(test.index(ran))))
#print(test)
#print()
#print("pop(), popped item: {}".format(test.pop()))
#print(test)