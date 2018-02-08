global player_decider
player_decider = 0

board_array_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def get_user_names():
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
	user1_name = raw_input("What's your name? ")
	print "Awesome", user1_name + "," " you're Xs!" 
	print ""
	user2_name = raw_input("What's your buddy's name? ")
	print "Aight", user2_name + "," " you're Os!" 
	print ""
	print ""

	user_name_array = [user1_name, user2_name]
	return user_name_array

def draw_board(board_array_list):
	letter_array = ["A", "B", "C"]
	draw_loop_count = 0
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
	print "   1   2   3"
	for i in board_array_list:
		print letter_array[draw_loop_count], " " + i[0], "|", i[1], "|", i[2]
		draw_loop_count += 1
		if draw_loop_count < 3:
			print "  -----------"
	print""

def decide_player(turn_count):
	player_decider = turn_count%2
	return player_decider

def enter_move(names, player_decider, board_array_list):
	player_move = "?"
	new_move_row = "?"
	new_move_col = "?"
	move_can_be_entered = 0

	if player_decider == 0:
		player_move = "X"
	else:
		player_move = "O"

	while move_can_be_entered == 0:
		while new_move_row is not "A" and new_move_row is not "B" and new_move_row is not "C":
			new_move_row = raw_input("Your turn, " + names[player_decider] + ". \nPick a row: ")
		while new_move_col is not "1" and new_move_col is not "2" and new_move_col is not "3":
			new_move_col = raw_input("Pick a column: ")

		move_can_be_entered = 1

		if new_move_row == "A":
			row_i = 0
		elif new_move_row == "B":
			row_i = 1
		elif new_move_row == "C":
			row_i = 2

		if new_move_col == "1":
			col_i = 0
		elif new_move_col == "2":
			col_i = 1
		elif new_move_col == "3":
			col_i = 2

		# Prevents players overwriting moves
		if board_array_list[row_i][col_i] is "X" or board_array_list[row_i][col_i] is "O":
			print "\n\n\nSeat's taken!\n\n"

			move_can_be_entered = 0
			new_move_row = "?"
			new_move_col = "?"

	board_array_list[row_i][col_i] = player_move

	draw_board(board_array_list)

	return board_array_list

def winning(board, game_won):
	# Check for row wins
	for i in board:
		if i[0] is not " " and i[0] == i[1] and i[0] == i[2]:
			game_won = 1

	# Check for horizontal wins
	col_to_check = 0
	while col_to_check < 3:
		if board[0][col_to_check] is not " " and board[0][col_to_check] == board[1][col_to_check] and board[0][col_to_check] == board[2][col_to_check]:
			game_won = 1
		col_to_check += 1

	# Check for diagonal wins
	if board[0][0] is not " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
		game_won = 1
	elif board[0][2] is not " " and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
		game_won = 1

	tie = 0
	move_count = 0
	for i in board:
		for j in i:
			if j is not " ":
				move_count += 1

	if move_count == 9 and not game_won:
		tie = 1
		game_done = 1

	return (game_won, tie)

def main():
	turn_count = 0
	game_won = 0
	tie = 0
	names = get_user_names()
	draw_board(board_array_list)

	while not game_won and not tie:
		player_decider = decide_player(turn_count)
		board = enter_move(names, player_decider, board_array_list)
		how_it_ended = winning(board,game_won)
		game_won = how_it_ended[0]
		tie = how_it_ended[1]

		if game_won:
			print "YOU DA MAN, " + names[player_decider] + "!"

		if tie:
			print "\n\n\n\nY'ALLS MAD LAME!"

		turn_count += 1


main()
