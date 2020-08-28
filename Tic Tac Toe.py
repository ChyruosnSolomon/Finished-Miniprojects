def new_game(dic_row1,dic_row2,dic_row3,lst_row1,lst_row2,lst_row3,in_player,res_game):
	while not res_game:
		new_game_true = input("Do you want to start a new game? (yes or no)")
		while not new_game_true == "yes" or new_game_true == "no":
			print("Invalid input!")
			new_game_true = input("Do you want to start a new game? (Y or N)")
		if new_game_true == "yes":
			dic_row1 = {1:" ",2:" ",3:" "}
			dic_row2 = {4:" ",5:" ",6:" "}
			dic_row3 = {7:" ",8:" ",9:" "}
			lst_row1 = [dic_row1[1],dic_row1[2],dic_row1[3]]
			lst_row2 = [dic_row2[4],dic_row2[5],dic_row2[6]]
			lst_row3 = [dic_row3[7],dic_row3[8],dic_row3[9]]
			return True
			break
		elif new_game_true == "no":
			return False
			break

def display_current_board(lst_row1,lst_row2,lst_row3,dic_row1,dic_row2,dic_row3):
	lst_row1 = [dic_row1[1],dic_row1[2],dic_row1[3]]
	lst_row2 = [dic_row2[4],dic_row2[5],dic_row2[6]]
	lst_row3 = [dic_row3[7],dic_row3[8],dic_row3[9]]
	print(lst_row1)
	print(lst_row2)
	print(lst_row3)

def start_game(lst_player):
	print("Welcome to my first tic-tac-toe game.")

	player1_online = False
	player2_online = False

	while not player1_online or player2_online:
		lst_player[0] = input("Player 1, choose if you want to be X or O: ")

		if (lst_player[0] not in ["X","O"]):
			print("Invalid input!")
			lst_player[0] = input("Player 1, choose if you want to be X or O: ")
		elif (lst_player[0] == "X"):
			lst_player[1] = "O"
			player1_online = True
			player2_online = True
			player_first = "Player 2 will go first."
			break
		elif (lst_player[0] == "O"):
			lst_player[1] = "X"
			player1_online = True
			player2_online = True
			player_first = "Player 1 will go first."
			break

	print(player_first)

def select_positionO(lst_player,pos_num):

	if lst_player[0] == "X":
		player_input = lst_player[1]
		position_number = input("Player 2, select a number position to place your counter (1 - 9): ")

		while not position_number.isdigit():
			print("Invalid input!")
			position_number = input("Player 2, select a number position to place your counter (1 - 9): ")

		position_number = int(position_number)

		while not position_number in range(1,10):
			print("Invalid input!")
			position_number = input("Player 2, select a number position to place your counter (1 - 9): ")
			position_number = int(position_number)

		while position_number in pos_num:
			print("There is already an X or a O in that position. Select another position please.")
			position_number = input("Player 2, select a number position to place your counter (1 - 9): ")
			position_number = int(position_number)


	elif (lst_player[0] == "O"):
		player_input = lst_player[0]
		position_number = input("Player 1, select a number position to place your counter (1 - 9): ")

		while not position_number.isdigit():
			print("Invalid input!")
			position_number = input("Player 1, select a number position to place your counter (1 - 9): ")

		position_number = int(position_number)	

		while not position_number in range(1,10):
			print("Invalid input!")
			position_number = input("Player 1, select a number position to place your counter (1 - 9): ")
			position_number = int(position_number)

		while position_number in pos_num:
			print("There is already an X or a O in that position. Select another position please.")
			position_number = input("Player 1, select a number position to place your counter (1 - 9): ")
			position_number = int(position_number)

	pos_num.append(position_number)


def update_boardO(index_pos,pos_num,dic_row1,dic_row2,dic_row3):
	if pos_num[index_pos] in range(1,4):
		dic_row1[pos_num[index_pos]] = "O"
	elif pos_num[index_pos] in range(3,7):
		dic_row2[pos_num[index_pos]] = "O"
	elif pos_num[index_pos] in range(7,10):
		dic_row3[pos_num[index_pos]] = "O"
	

def select_positionX(lst_player,pos_num):

	if (lst_player[0] == "X"):
		player_input = lst_player[1]
		position_number = input("Player 1, select a number position to place your counter (1 - 9): ")

		while not position_number.isdigit():
			print("Invalid input!")
			position_number = input("Player 1, select a number position to place your counter (1 - 9): ")

		position_number = int(position_number)

		while not position_number in range(1,10):
			print("Invalid input!")
			position_number = input("Player 1, select a number position to place your counter (1 - 9): ")
			position_number = int(position_number)

		while position_number in pos_num:
			print("There is already an X or a O in that position. Select another position please.")
			position_number = input("Player 1, select a number position to place your counter (1 - 9): ")
			position_number = int(position_number)

	elif (lst_player[0] == "O"):
		player_input = lst_player[0]
		position_number = input("Player 2, select a number position to place your counter (1 - 9): ")

		while not position_number.isdigit():
			print("Invalid input!")
			position_number = input("Player 2, select a number position to place your counter (1 - 9): ")

		position_number = int(position_number)	

		while not position_number in range(1,10):
			print("Invalid input!")
			position_number = input("Player 2, select a number position to place your counter (1 - 9): ")
			position_number = int(position_number)

		while position_number in pos_num:
			print("There is already an X or a O in that position. Select another position please.")
			position_number = input("Player 2, select a number position to place your counter (1 - 9): ")
			position_number = int(position_number)

	pos_num.append(position_number)

def update_boardX(index_pos,pos_num,dic_row1,dic_row2,dic_row3):
	if pos_num[index_pos] in range(1,4):
		dic_row1[pos_num[index_pos]] = "X"
	elif pos_num[index_pos] in range(3,7):
		dic_row2[pos_num[index_pos]] = "X"
	elif pos_num[index_pos] in range(7,10):
		dic_row3[pos_num[index_pos]] = "X"

def game_winO(dic_row1,dic_row2,dic_row3):
	#function not responding
	winner_o = ["O","O","O"]
	win_1 = [dic_row1[1],dic_row1[2],dic_row1[3]]
	win_2 = [dic_row2[4],dic_row2[5],dic_row2[6]]
	win_3 = [dic_row3[7],dic_row3[8],dic_row3[9]]
	win_4 = [dic_row1[1],dic_row2[4],dic_row3[7]]
	win_5 = [dic_row1[2],dic_row2[5],dic_row3[8]]
	win_6 = [dic_row1[3],dic_row2[6],dic_row3[9]]
	win_7 = [dic_row1[1],dic_row2[5],dic_row3[9]]
	win_8 = [dic_row1[3],dic_row2[5],dic_row3[7]]

	if win_1 == winner_o:
		return True
	elif win_2 == winner_o:
		return True
	elif win_3 == winner_o:
		return True
	elif win_4 == winner_o:
		return True
	elif win_5 == winner_o:
		return True
	elif win_6 == winner_o:
		return True
	elif win_7 == winner_o:
		return True
	elif win_8 == winner_o:
		return True	
	else:
		return False

def game_winX(dic_row1,dic_row2,dic_row3):
	#function not responding
	winner_x = ["X","X","X"]
	win_1 = [dic_row1[1],dic_row1[2],dic_row1[3]]
	win_2 = [dic_row2[4],dic_row2[5],dic_row2[6]]
	win_3 = [dic_row3[7],dic_row3[8],dic_row3[9]]
	win_4 = [dic_row1[1],dic_row2[4],dic_row3[7]]
	win_5 = [dic_row1[2],dic_row2[5],dic_row3[8]]
	win_6 = [dic_row1[3],dic_row2[6],dic_row3[9]]
	win_7 = [dic_row1[1],dic_row2[5],dic_row3[9]]
	win_8 = [dic_row1[3],dic_row2[5],dic_row3[7]]

	if win_1 == winner_x:
		return True
	elif win_2 == winner_x:
		return True
	elif win_3 == winner_x:
		return True
	elif win_4 == winner_x:
		return True
	elif win_5 == winner_x:
		return True
	elif win_6 == winner_x:
		return True
	elif win_7 == winner_x:
		return True
	elif win_8 == winner_x:
		return True	
	else:
		return False

def game_flow():
	win_X = False
	win_O = False
	restart_game = False
	game_round = 0
	drow_1 = {1:" ",2:" ",3:" "}
	drow_2 = {4:" ",5:" ",6:" "}
	drow_3 = {7:" ",8:" ",9:" "}

	row_1 = [drow_1[1],drow_1[2],drow_1[3]]
	row_2 = [drow_2[4],drow_2[5],drow_2[6]]
	row_3 = [drow_3[7],drow_3[8],drow_3[9]]

	player_inputs = ["",""]
	position_index = []

	start_game(player_inputs)
	display_current_board(row_1,row_2,row_3,drow_1,drow_2,drow_3)
	while (game_round < 9):
		select_positionO(player_inputs,position_index)
		update_boardO(game_round,position_index,drow_1,drow_2,drow_3)
		display_current_board(row_1,row_2,row_3,drow_1,drow_2,drow_3)
		win_O = game_winO(drow_1,drow_2,drow_3)
		if win_O:
			if player_inputs[0] == "O":
				print("Player 1 wins!")
				break

			elif player_inputs[0] == "X":
				print("Player 2 wins!")
				break
		game_round += 1
		
		if game_round == 9: 
			print("Tie!")
			break

		else:
			pass

		select_positionX(player_inputs,position_index)
		update_boardX(game_round,position_index,drow_1,drow_2,drow_3)
		display_current_board(row_1,row_2,row_3,drow_1,drow_2,drow_3)
		win_X = game_winX(drow_1,drow_2,drow_3)
		if win_X:
			if player_inputs[0] == "X":
				print("Player 1 wins!")
				break

			elif player_inputs[0] == "O":
				print("Player 2 wins!")
				break
		game_round += 1

		if game_round == 9: 
			print("Tie!")
			break

		else:
			pass

	print("Thank you for playing. :)")

game_flow()