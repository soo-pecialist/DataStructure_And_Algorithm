#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 00:32:28 2018

@author: Soo Hyeon Kim
"""

import turtle

def draw_tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_tree(branch_len - 15, t)
        t.left(40)
        draw_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)
        
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    draw_tree(100, t)
    my_win.exitonclick()

main()