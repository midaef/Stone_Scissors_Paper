
from ezprint import p
import random
import os


def cls():
	os.system('cls')


def game():
	p('===GAME FOR WINDOWS===')
	p('1-START GAME TWO PLAYERS')
	p('2-START GAME VS BOT')
	v = input('>>>')
	if v == '2':
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
	if v == '1':
		player1 = int(input('Input player 1>>>'))
		if player1 == 1:
			player1 = 'Stone'
		elif player1 == 2:
			player1 ='Scissors'
		else:
			player1 = 'Paper'

		player2 = int(input('Input player 2>>>'))
		if player2 == 1:
			p('Player 1 choose:' + str(player1))
			p('Player 2 choose: Paper')
			if player1 == 'Stone':
				p('drow')
			elif player1 == 'Scissors':
				p('Player 2 win')
			else:
				p('Player 1 win')
		elif player2 == 2:
			p('Player 1 choose:' + str(player1))
			p('Player 2 choose: Paper')
			if player1 == 'Stone':
				p('lose')
			elif player1 == 'Scissors':
				p('drow')
			else:
				p('win')
		elif player2 == 3:
			p('Player 1 choose:' + str(player1))
			p('Player 2 choose: Paper')
			if player1 == 'Stone':
				p('win')
			elif player1 == 'Scissors':
				p('lose')
			else:
				p('drow')

if __name__ == '__main__':
	cls()
	game()
