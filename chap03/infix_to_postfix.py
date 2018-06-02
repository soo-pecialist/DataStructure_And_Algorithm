#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 00:52:13 2018

@author: Soo Hyeon Kim
"""
import Stack

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack.Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(' :
            op_stack.push(token)
        elif token == ')' :
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                  (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
        
        
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
        
    return " ".join(postfix_list)
    
##[TEST]
print("A * B + C * D -> {}".format(infix_to_postfix("A * B + C * D"))) 
print("( A + B ) * C - ( D - E ) * ( F + G ) -> {}".format(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )")))
print("( A + B ) * ( C + D ) -> {}".format(infix_to_postfix("( A + B ) * ( C + D )")))
print("( A + B ) * C -> {}".format(infix_to_postfix("( A + B ) * C")))
print("A + B * C -> {}".format(infix_to_postfix("A + B * C")))