import pyautogui as pg
import numpy as np
import time
from solver import valid, print_board

board = []

i = 1
while True:
	print(f'Row {i}: ', end=' ')
	row = list(map(int, input()))
	board.append(row)
	if len(board) == 9:
		break
	print(f'Row {i} completed!')
	i += 1

time.sleep(3)

def display(board):
	final = []
	str_fin = []
	for i in range(9):
		final.append(board[i])

	for lists in final:
		for num in lists:
			str_fin.append(str(num))

	counter = []


	for num in str_fin:
		pg.press(num)
		pg.hotkey('right')
		counter.append(num)
		if len(counter) % 9 == 0:
			pg.hotkey('down')
			pg.hotkey('left')
			pg.hotkey('left')
			pg.hotkey('left')
			pg.hotkey('left')
			pg.hotkey('left')
			pg.hotkey('left')
			pg.hotkey('left')
			pg.hotkey('left')

	

def auto_solver():
	global board
	for y in range(9):
		for x in range(9):
			if board[y][x] == 0:
				for n in range(1, 10):
					if valid(board, n, (y, x)):
						board[y][x] = n
						auto_solver()
						board[y][x] = 0

				return

	display(board)

auto_solver()

