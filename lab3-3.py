# -*-coding: utf-8 -*-

import sys

weight, height = input('Input your weight and height: ').split(' ')\

height = float(height)/100

index = float(weight)/float(height*height)

print('Your weight index is: ' + str(index))

