
from ezprint import p
import random
import os


def cls():
	os.system('cls')


def game():
	while True:
		cls()
		p('===GAME FOR WINDOWS=====')
		p('==Rock/Scissors/Paper===')
		p('1-START GAME VS BOT')
		p('2-START GAME TWO PLAYERS')
		p('3-EXIT')
		p('========================')
		v = input('>>>')
		try:
			v = int(v)
		except:
			p('Incorrect choose')
			return

		if int(v) < 1 or int(v) > 3:
			p('Incorrect choose')
			return

		v = str(v)

		if v == '1':
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

			player = input('>>>')

			try:
				player = int(player)
			except:
				p('Incorrect choose')
				return

			if player < 1 or player > 3:
				p('Incorrect choose')
				return

			if player == 1:
				p('Your choose: Stone')
				p('Bot choose: ' + str(app))
				if app == 'Stone':
					p('Drow')
				elif app == 'Scissors':
					p('Win')
				else:
					p('Lose')
			elif player == 2:
				p('Your choose: Scissors')
				p('Bot choose: ' + str(app))
				if app == 'Stone':
					p('Lose')
				elif app == 'Scissors':
					p('Drow')
				else:
					p('Win')
			elif player == 3:
				p('Your choose: Paper')
				p('Bot choose: ' + str(app))
				if app == 'Stone':
					p('Win')
				elif app == 'Scissors':
					p('Lose')
				else:
					p('Drow')
			input('Continue - click to ENTER ')

		if v == '2':
			p('1) Stone')
			p('2) Scissors')
			p('3) Paper')
			player1 = input('Player#1>>>')

			try:
				player1 = int(player1)
			except:
				p('Incorrect choose')
				return

			if player1 < 1 or player1 > 3:
				p('Incorrect choose')
				return

			if player1 == 1:
				player1 = 'Stone'
			elif player1 == 2:
				player1 ='Scissors'
			else:
				player1 = 'Paper'
			p('1) Stone')
			p('2) Scissors')
			p('3) Paper')
			cls()
			player2 = int(input('Player#2>>>'))
			if player2 == 1:
				p('Player 1 choose: ' + str(player1))
				p('Player 2 choose: Stone')
				if player1 == 'Stone':
					p('Drow')
				elif player1 == 'Scissors':
					p('Player 2 win')
				else:
					p('Player 1 win')
			elif player2 == 2:
				p('Player 1 choose: ' + str(player1))
				p('Player 2 choose: Scissors')
				if player1 == 'Stone':
					p('Player 1 win')
				elif player1 == 'Scissors':
					p('Drow')
				else:
					p('Player 2 win')
			elif player2 == 3:
				p('Player 1 choose: ' + str(player1))
				p('Player 2 choose: Paper')
				if player1 == 'Stone':
					p('Player 2 win')
				elif player1 == 'Scissors':
					p('Player 1 win')
				else:
					p('Drow')
			input('Continue - click to ENTER ')

		if v == '3':
			exit()


if __name__ == '__main__':
	cls()
	game()
