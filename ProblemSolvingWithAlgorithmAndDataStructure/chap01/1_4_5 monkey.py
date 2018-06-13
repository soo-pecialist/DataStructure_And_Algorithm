#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 18:25:06 2018

@author: KimSooHyeon

This program is to find most similar sentence created by a monkey.
Target sentence is of Shakespeare: "methinks it is like a weasel"

The program(find_the_best()) executes 1000 times of random_sentence_generator
and evaluate_score(). 

It returns highest score sentence 
"""

import numpy as np
import string

def random_sentence_generator():
    length = 27
    sentence = ''
    for _ in range(length):
        sentence = sentence \
                    + str(np.random.choice(list((string.ascii_lowercase + ' '))))
    
    return sentence

def evaluate_score(generated, target):
    score = 0
    for x,y in zip(generated, target):
        if x == y:
            score += 1.0
    return score / len(target)


def find_the_best(target, rep=1000):
    best = ''
    best_score = 0
    for i in range(rep):
        random_sentence = random_sentence_generator()
        score = evaluate_score(random_sentence, target)
        if score > best_score:
            best = random_sentence
    
    return best