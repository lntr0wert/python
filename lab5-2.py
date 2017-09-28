# -*-coding: utf-8 -*-

h, w = input('enter door parameters: ').split(' ')

h1 = int(h)
w1 = int(w)

a, b, c = input('enter the box parameters: ').split(' ')

a1 = int(a)
b1 = int(b)
c1 = int(c)

if a1 < h1 and b1 < w1:
	print('true')
elif b1 < h1 and a1 < w1:
	print('true')
elif b1 < h1 and c1 < w1:
	print('true')	
elif c1 < h1 and b1 < w1:
	print('true')
elif a1 < h1 and c1 < w1:
	print('true')
elif c1 < h1 and a1 < w1:
	print('true')
else:
	print('false')
