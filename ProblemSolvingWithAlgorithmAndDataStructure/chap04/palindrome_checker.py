#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:59:47 2018

@author: Soo Hyeon Kim
"""

import re

def palindrome_checker(text):
    
    assert type(text) == str, "Input must be STRING"
    
    text = text.lower()
    text = re.sub("[^A-Za-z]", "", text)
    
    if len(text) <= 1: ## base case
        return True
    else:
        return (text[0] == text[-1]) and palindrome_checker(text[1:-1])

    
## [TEST]
#print("kayak: {}".format(palindrome_checker("kayak")))
#print("aibohphobia: {}".format(palindrome_checker("aibohphobia")))
#print("Live not on evil: {}".format(palindrome_checker("Live not on evil")))
#print("Reviled did I live, said I, as evil I did deliver: {}".format(\
#      palindrome_checker("Reviled did I live, said I, as evil I did deliver")))
#print("Kanakanak – a town in Alaska: {}".format(\
#      palindrome_checker("Kanakanak – a town in Alaska")))
#print("Go hang a salami; I’m a lasagna hog.: {}".format(\
#      palindrome_checker("Go hang a salami; I’m a lasagna hog.")))
#print("Able was I ere I saw Elba: {}".format(\
#      palindrome_checker("Able was I ere I saw Elba")))
#print("Wassamassaw – a town in South Dakota: {}".format(\
#      palindrome_checker("Wassamassaw – a town in South Dakota")))