#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:23:38 2018

@author: KimSooHyeon
"""
def gcd(m,n):
    while m % n != 0:
        m, n = n, (m%n)
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def __str__ (self):
        common = gcd(self.num, self.den)
        return str(self.num//common) + "/" + str(self.den//common)
    
    def show(self):
        common = gcd(self.num, self.den)
        print(str(self.num//common) + "/" + str(self.den//common))    
## Numerical operation
    def __add__(self, other):
        new_num = self.num* other.den + self.den*other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
    
    def __sub__(self, other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
        
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

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
