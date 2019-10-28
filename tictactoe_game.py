"""
random is a python library that can be used to generate a random number. 
You can use "import" to bring in other libraries, or functions from
other files.
"""
import random


def make_new_game_board():
	"""
	This function creates a new tic-tac-toe board. The board is actually 
	a list of nine elements - numbers, in this case - which represent the 
	nine spots on the board.
	"""
	game_board = []
	for number in range(1, 10):
		# the range() function produces a list of integers that starts at the first 
		# number specified and ends before second number specified. 
		# range(25, 20) would have 25, 26, 27, 28, and 29 in it.
		
		game_board.append(number)
		# append() is a list method that adds a new value to the end of a list

	return game_board

def show_game_board_for_python_2(game_board):
	"""
	This function takes a "game board" which is a nine-element list
	and it prints out three lines, referencing the nine indexes in the 
	list to display the items at that index (a number or an X/O). 

	I've had to comment out this function so the file will run in Python 3.
	"""
	"""
	print game_board[0], '|', game_board[1], '|', game_board[2]
	print '-'*10
	print game_board[3], '|', game_board[4], '|', game_board[5]
	print '-'*10
	print game_board[6], '|', game_board[7], '|', game_board[8]
	"""

def show_game_board_for_python_3(game_board):
	"""
	This function takes a "game board" which is a nine-element list
	and it prints out three lines, referencing the nine indexes in the 
	list to display the items at that index (a number or an X/O). 

	In Python 2.6, this returns a set for each line
	"""
	print (game_board[0], '|', game_board[1], '|', game_board[2])
	print ('-'*10)
	print (game_board[3], '|', game_board[4], '|', game_board[5])
	print ('-'*10)
	print (game_board[6], '|', game_board[7], '|', game_board[8])


def show_game_board_using_format(game_board):
        """
        This version of the show_game_board function works in Python 2.6:
        in Python 2.6, the previous function returns a set, so we would
        need to remove the parentheses around the print statement.
        """
        for row in [0, 1, 2]: #or range(0, 3)
            print("{first} | {second} | {third}".format(first=game_board[row*3], second=game_board[row*3+1], third=game_board[row*3+2]))
            if row < 2:
                    print("-"*9)        


def check_for_endstate(tictactoe_board):
	"""
	This function checks each win state option, one by one, and if 
	none of the "win conditions" are met, it counts how many spaces 
	on the board are filled. If not all of the space are filled, 
	the game continues: otherwise, the game is a draw. 

	The win state return statements will return the winning 
	symbol when a win is found.
	"""
	if tictactoe_board[0] == tictactoe_board[1] and tictactoe_board[0] == tictactoe_board[2]:
		return tictactoe_board[0]
	if tictactoe_board[3] == tictactoe_board[4] and tictactoe_board[3] == tictactoe_board[5]:
		return tictactoe_board[3]
	if tictactoe_board[6] == tictactoe_board[7] and tictactoe_board[6] == tictactoe_board[8]:
		return tictactoe_board[6]
	if tictactoe_board[0] == tictactoe_board[3] and tictactoe_board[0] == tictactoe_board[6]:
		return tictactoe_board[0]
	if tictactoe_board[1] == tictactoe_board[4] and tictactoe_board[1] == tictactoe_board[7]:
		return tictactoe_board[1]
	if tictactoe_board[2] == tictactoe_board[5] and tictactoe_board[2] == tictactoe_board[8]:
		return tictactoe_board[2]
	if tictactoe_board[0] == tictactoe_board[4] and tictactoe_board[0] == tictactoe_board[8]:
		return tictactoe_board[0]
	if tictactoe_board[2] == tictactoe_board[4] and tictactoe_board[2] == tictactoe_board[6]:
		return tictactoe_board[2]

	filled_count = 0
	for x in tictactoe_board:
		if x in ['x', 'o']:
			filled_count += 1

	if filled_count <= 8:
		return "continue"
	elif filled_count == 9:
		return "draw"
	else:
		return 'err'


def choose_spot(tictactoe_game_board, player_symbol):
	"""
	This function allows a player to choose a spot on the board. 
	We pass in the game board (which will be edited by the 
	function) and the player's symbol (so we know what to put
	on to the game board).

	Note that we don't have to return the game board because 
	we are performing the operation on an element that is passed
	into the function.
	"""
	invalid_selection_response = "\nSelection invalid"

	turn_successful = False
	while turn_successful == False:
		spot_chosen = input("\nSelect your spot: \n")
		if str(spot_chosen).isdigit() == True:
			spot_chosen = int(spot_chosen)
			if spot_chosen in range(1, 10) and str(tictactoe_game_board[spot_chosen-1]).isdigit():
				tictactoe_game_board[spot_chosen-1] = player_symbol
				turn_successful = True
			else:
				print(invalid_selection_response)
		else:
			print(invalid_selection_response)


def choose_starting_player():
	"""
	This choose a random integer: if that integer is 1, x 
	goes first, otherwise o goes first.
	"""
	starting_player = random.randint(1, 2)
	if starting_player == 1:
		player1_symbol = 'x'
		player2_symbol = 'o'
	else:
		player1_symbol = 'o'
		player2_symbol = 'x'

	"""
	Python can return multiple variables in an order specified.
	The call to the this function in your code would be:

	player1, player2 = choose_starting_player()

	player1 would be assigned x or o depending on whether the
	random integer was 1 or 2: player2 would be assigned the 
	other symbol. If the random integer was 1, the result:

	player1 = 'x'
	player2 = 'o'
	"""
	return player1_symbol, player2_symbol




# Now it's time to start the game
# First we need to make the game board. We'll assign it to the variable "playing_board"
playing_board = make_new_game_board()


# Now we need to show the game board. We'll use the show_game_board_using_format function



# Before we start the game, we want to choose who goes first
player1, player2 = choose_starting_player()


# Now we want to start the game, and we want to it keep going while the game doesn't have a win or draw
# I've used a while loop that uses the "check_for_endstate" function
while check_for_endstate(playing_board) == 'continue':
	for player in [player1, player2]:
		show_game_board_using_format(playing_board)
		print("{player}'s turn: ".format(player=player))
		choose_spot(playing_board, player)
		if check_for_endstate(playing_board) == 'draw':
			print("draw")

		if check_for_endstate(playing_board) == 'err':
			print("error")

		if check_for_endstate(playing_board) in ['x', 'o']:
			winning_player = check_for_endstate(playing_board)
			print("{winner} wins! ".format(winner=winning_player))









