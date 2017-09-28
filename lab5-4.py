# -*- coding: utf-8 -*- 

import math

a, b, c = input('Kvadratne rivnyanna vyglyady ax^2 + bx + c = 0 \n\n enter A, B, C :').split(' ')

a1 = int(a)
b1 = int(b)
c1 = int(c)

def descr():
    descr_value = sqrt((b*b) - 4*a*c)
    return descr_value


def x1():
    x1_value = (-b + descr_value)/2*a
    return x1_value

def x1():
    x1_value = (-b - descr_value)/2*a
    return x2_value

print('koreni rivnyanna is: ' + x1_value + ' ' + x2_value)
