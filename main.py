
from ezprint import p
import random
import os


def cls():
	os.system('cls')


def game():
	p('===GAME FOR WINDOWS===')
	p('1) Stone')
	p('2) Scissors')
	p('3) Paper')

	app = random.randint(1,3)
	if app == 1:
		app = 'Stone'
	elif app == 2:
		app ='Scissors'
	else:
		app = 'Paper'

	player = int(input('>>>'))
	if player == 1:
		p('Your choose: Stone')
		p('Bot choose:' + str(app))
		if app == 'Stone':
			p('drow')
		elif app == 'Scissors':
			p('win')
		else:
			p('lose')
	elif player == 2:
		p('Your choose: Scissors')
		p('Bot choose:' + str(app))
		if app == 'Stone':
			p('lose')
		elif app == 'Scissors':
			p('drow')
		else:
			p('win')
	elif player == 3:
		p('Your choose: Paper')
		p('Bot choose:' + str(app))
		if app == 'Stone':
			p('win')
		elif app == 'Scissors':
			p('lose')
		else:
			p('drow')



if __name__ == '__main__':
	cls()
	game()
