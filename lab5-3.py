# -*- coding: utf-8 -*- 
import random
import time

cases={
"8<*":"bot won",
"*8<":"human won",
"*#":"bot won",
"#*":"human won",
"8<#":"human won",
"#8<":"bot won",
"**":"draw",
"8<8<":"draw",
"##":"draw"
}

def reply():
	reply_vars=['*','8<','#']
	return reply_vars[random.randint(0,2)]
	
	
	
print('\n 8< scissors \n * rock \n # paper \n')

tryAgain=True;

while tryAgain:
	human_answer=input('enter your choose(8< or * or #) \n')
	bot_answer=reply()
	
	print('bot answer {} \n'.format(bot_answer))
	print(cases[human_answer+bot_answer])
	ask=input('try again? (y/n)')
	if ask == 'n':
		tryAgain = False
	
	
