
from ezprint import p
import random
import time
import os


def win(isDrow = False, whowin = 'Player 1'):
	cls()
	p('Rock')
	time.sleep(0.5)
	p('Scissors')
	time.sleep(0.5)
	p('Paper')
	time.sleep(0.5)
	p('1')
	time.sleep(0.5)
	p('2')
	time.sleep(0.5)
	p('3')
	time.sleep(0.5)
	if isDrow:
		print('Drow')
	else:
		print(whowin  + ' win!')


def choose(inputtext = '>>>'):
	p('1) Stone')
	p('2) Scissors')
	p('3) Paper')

	c = input(inputtext)

	try:
		c = int(c)
	except:
		p('Incorrect choose')
		return choose(inputtext = inputtext)

	if c < 1 or c > 3:
		p('Incorrect choose')
		return choose(inputtext = inputtext)

	return c

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
			app = random.randint(1,3)
			if app == 1:
				app = 'Stone'
			elif app == 2:
				app ='Scissors'
			else:
				app = 'Paper'

			player = choose()

			if player == 1:
				p('Your choose: Stone')
				p('Bot choose: ' + str(app))
				if app == 'Stone':
					# p('Drow')
					win(isDrow = True)
				elif app == 'Scissors':
					win(whowin = 'Player')
				else:
					win(whowin = 'Bot')
			elif player == 2:
				p('Your choose: Scissors')
				p('Bot choose: ' + str(app))
				if app == 'Stone':
					win(whowin = 'Bot')
				elif app == 'Scissors':
					win(isDrow = True)
				else:
					win(whowin = 'Player')
			elif player == 3:
				p('Your choose: Paper')
				p('Bot choose: ' + str(app))
				if app == 'Stone':
					win(whowin = 'Player')
				elif app == 'Scissors':
					win(whowin = 'Bot')
				else:
					win(isDrow = True)
			input('Continue - click to ENTER ')

		if v == '2':
			cls()
			player1 = choose(inputtext = 'Player#1>>>')

			if player1 == 1:
				player1 = 'Stone'
			elif player1 == 2:
				player1 ='Scissors'
			else:
				player1 = 'Paper'

			cls()
			player2 = choose(inputtext = 'Player#2>>>')

			if player2 == 1:
				p('Player 1 choose: ' + str(player1))
				p('Player 2 choose: Stone')
				if player1 == 'Stone':
					win(isDrow = True)
				elif player1 == 'Scissors':
					win(whowin = 'Player 2')
				else:
					win(whowin = 'Player 1')
			elif player2 == 2:
				p('Player 1 choose: ' + str(player1))
				p('Player 2 choose: Scissors')
				if player1 == 'Stone':
					win(whowin = 'Player 1')
				elif player1 == 'Scissors':
					win(isDrow = True)
				else:
					win(whowin = 'Player 2')
			elif player2 == 3:
				p('Player 1 choose: ' + str(player1))
				p('Player 2 choose: Paper')
				if player1 == 'Stone':
					win(whowin = 'Player 2')
				elif player1 == 'Scissors':
					win(whowin = 'Player 1')
				else:
					win(isDrow = True)
			input('Continue - click to ENTER ')

		if v == '3':
			exit()


if __name__ == '__main__':
	cls()
	game()
