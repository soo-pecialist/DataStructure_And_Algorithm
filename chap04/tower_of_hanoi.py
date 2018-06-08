#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:25:03 2018

@author: Soo Hyeon Kim
"""
def move_tower(height, pole1, pole2, pole3):
    if height >= 1:
        # move height-1 disks to pole3 tempolarily
        move_tower(height-1, pole1, pole3, pole2) 
        # move bottom largest disk
        move_disk(pole1, pole2) 
        # move height-11 disks back to pole2
        move_tower(height-1, pole3, pole2, pole1) 
    
def move_disk(p1, p2):
    print("moving disk from", p1, "to", p2)

def tower_of_hanoi(h):
    move_tower(h, "A", "B", "C")
    
tower_of_hanoi(3)
    