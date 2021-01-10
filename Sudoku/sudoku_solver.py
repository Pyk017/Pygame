

def solve(board):
	if not find_empty(board):
		return True

	row, col = find_empty(board)

	for i in range(1, 10):
		if valid(board, i, (row, col)):
			board[row][col] = i

			if solve(board):
				return True

			board[row][col] = 0

	return False



def valid(board, num, pos):
	# check row
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	# check column
	for i in range(len(board[0])):
		if board[i][pos[1]] == num and pos[0] != i:
			return False


	# check mini square
	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 + 3):
			if board[i][j] == num and (i, j) != pos:
				return False

	return True



def print_board(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print('------------------------------------------')

		for j in range(len(board[0])):
			if j % 3 == 0:
				print(' | ', end=' ')

			if j == 8:
				print(f"{board[i][j]} |")
			else:
				print(f"{board[i][j]} ", end=' ') 



def find_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i, j)  # row, column

	return None


# print_board(board)
# solve(board)
# print('\n Solved Game \n')
# print_board(board)