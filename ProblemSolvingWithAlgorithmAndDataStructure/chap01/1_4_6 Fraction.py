#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:23:38 2018

@author: Soo Hyeon Kim
"""
def gcd(m,n):
    while m % n != 0:
        m, n = n, (m%n)
    return n

# get numerator
# example: get_num(Fraction(15, 35))    
def get_num(self):
    return self.num

# get denominator
# example: get_den(Fraction(15, 35))    
def get_den(self):
    return self.den

class Fraction:
    def __init__(self, top, bottom):
        assert (type(top) == int) and (type(bottom) == int), \
        "You MUST use 'integer'"
        assert bottom != 0, "You are not allowed to set denominator to 0"
        
        common = gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common
         
    def __repr__(self):
        return 'Fraction {}/{}'.format(self.num, self.den)
    
    def __str__ (self):
        return str(self.num) + "/" + str(self.den)
    
    def show(self):
        print(str(self.num) + "/" + str(self.den))    

## Numerical operation
    def __add__(self, other):
        new_num = self.num* other.den + self.den*other.num
        new_den = self.den * other.den
        if new_num == 0:
            return 0
        return Fraction(new_num, new_den)
        
    def __sub__(self, other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den * other.den
        if new_num == 0:
            return 0
        return Fraction(new_num, new_den)
        
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        if new_num == 0:
            return 0
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        if new_num == 0:
            return 0
        if abs(new_num) == abs(new_den):
            return new_num // new_den
        if new_den == 0:
            raise AssertionError("You cannot divide by 0")
        return Fraction(new_num, new_den)

## Inequality operation
    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num
    
    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num != second_num
    
    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num > second_num
    
    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num >= second_num
    
    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num < second_num
    
    def __le__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num <= second_num


## Test
""" 
    f1 = 1/4, f2 = 2/3 f3 = 3/7, f4 = 1/4
    f1 = f4 < f3 < f2
    f1 + f3 = 19/28
    f2 - f4 = 5/12
    f2 * f3 = 2/7
    f3 / f2 = 9/14
"""
f1 = Fraction(1,4)
f2 = Fraction(2,3)
f3 = Fraction(15, 35)
f4 = Fraction(2,8)
print("[Test]")
print("f1: {0}, f2: {1}, f3: {2}, f4: {3}\n".format(f1, f2, f3, f4))
print("f1 + f3 = {}".format(f1+f3))
print("f2 - f4 = {}".format(f2-f4))
print("f2 * f3 = {}".format(f2*f3))
print("f3 / f2 = {}".format(f3/f2))
print()
print("f1 <= f4 ? {}".format(f1<=f4))
print("f1 >= f4 ? {}".format(f1<=f4))
print("f1 > f4  ? {}".format(f1>f4))
print("f1 < f2  ? {}".format(f1<f2))
print("f2 < f3  ? {}".format(f2<f3))
print("f2 > f3  ? {}".format(f2>f3))
print("f3 < f1  ? {}".format(f3<f1))
print()
print("-1/3 + 1/3 = {}".format(Fraction(-1,3) + Fraction(1,3)))
print("-1/3 - 1/3 = {}".format(Fraction(-1,3) - Fraction(1,3)))
print("-1/3 * 1/3 = {}".format(Fraction(1,-3) * Fraction(1,3)))
print("-1/3 / 1/3 = {}".format(Fraction(1,-3) / Fraction(1,3)))

