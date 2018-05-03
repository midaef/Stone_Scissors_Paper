
from ezprint import p
import random
import os


def cls():
	os.system('cls')


def game():
	p('===GAME FOR WINDOWS===')
	p('1)Stone')
	p('2)Scissors')
	p('3)Paper')

	player = input('>>>')
	if player == '1':
		p('Your choose: Stone')
	elif player == '2':
		p('Your choose: Scissors')
	else:
		p('Your choose: Paper')

	app = random.randint(1,3)
	app = str(app)
	if app == '1':
		p('Bot choose: Stone') 	
	elif app == '2':
		p('Bot choose: Scissors')
	elif app == '3':
		p('Bot choose: Paper')



if __name__ == '__main__':
	cls()
	game()
