"""
Design an algorithm to figure out if someone has won a game of tic-tac-toe
"""

class Position:
	def __init__(self, row, col):
		self.row = row
		self.col = col


# Generator iterator to loop over the board with given incrementals
def position_iterator(position, rowInc, colInc, size):
	curr_position = Position(position.row - rowInc, position.col - colInc)

	while curr_position.row + rowInc < size and curr_position.col + colInc < size:
		curr_position = Position(curr_position.row + rowInc, curr_position.col + colInc)
		yield curr_position


def has_won_iterate(board, iterator):
	position, rowInc, colInc, size = iterator
	player = board[position.row][position.col]

	for new_pos in position_iterator(position, rowInc, colInc, size):
		player_new_pos = board[new_pos.row][new_pos.col]
		if player != player_new_pos:
			return None
	return player	


def has_won(board):
	if not board or len(board) != len(board[0]): return None

	size = len(board)
	instructions = []

	# Create horizontal, vertial iterators
	for i in range(size):
		instructions.append((Position(0, i), 1, 0, size))
		instructions.append((Position(i, 0), 0, 1, size))

	# Create diagonal iterators
	instructions.append((Position(0, 0), 1, 1, size))
	instructions.append((Position(0, size - 1), 1, -1, size))

	# Run iterators on board
	for iterator in instructions:
		winner = has_won_iterate(board, iterator)
		if winner:
			return winner
	return None


board = [
	[1, 1, 2, 1],
	[2, 1, 2, 0],
	[2, 0, 2, 1],
	[2, 1, 2, 1]
]

player = has_won(board)
print (player)