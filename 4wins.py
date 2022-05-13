import numpy as np
import sys

nRows = 6
nCols = 7

board = np.zeros((nRows,nCols))
print(board)



def check4Win(board,playerId):
	if board[0][0] == playerId and board[0][1] == playerId and board[0][2] == playerId and board[0][3] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[0][1] == playerId and board[0][2] == playerId and board[0][3] == playerId and board[0][4] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[0][2] == playerId and board[0][3] == playerId and board[0][4] == playerId and board[0][5] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[0][3] == playerId and board[0][4] == playerId and board[0][5] == playerId and board[0][6] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][0] == playerId and board[1][1] == playerId and board[1][2] == playerId and board[1][3] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][1] == playerId and board[1][2] == playerId and board[1][3] == playerId and board[1][4] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][2] == playerId and board[1][3] == playerId and board[1][4] == playerId and board[1][5] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][3] == playerId and board[1][4] == playerId and board[1][5] == playerId and board[1][6] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][0] == playerId and board[2][1] == playerId and board[2][2] == playerId and board[2][3] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][1] == playerId and board[2][2] == playerId and board[2][3] == playerId and board[2][4] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][2] == playerId and board[2][3] == playerId and board[2][4] == playerId and board[2][5] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][3] == playerId and board[2][4] == playerId and board[2][5] == playerId and board[2][6] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[3][0] == playerId and board[3][1] == playerId and board[3][2] == playerId and board[3][3] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[3][1] == playerId and board[3][2] == playerId and board[3][3] == playerId and board[3][4] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[3][2] == playerId and board[3][3] == playerId and board[3][4] == playerId and board[3][5] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[3][3] == playerId and board[3][4] == playerId and board[3][5] == playerId and board[3][6] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[4][0] == playerId and board[4][1] == playerId and board[4][2] == playerId and board[4][3] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[4][1] == playerId and board[4][2] == playerId and board[4][3] == playerId and board[4][4] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[4][2] == playerId and board[4][3] == playerId and board[4][4] == playerId and board[4][5] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[4][3] == playerId and board[4][4] == playerId and board[4][5] == playerId and board[4][6] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[5][0] == playerId and board[5][1] == playerId and board[5][2] == playerId and board[5][3] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[5][1] == playerId and board[5][2] == playerId and board[5][3] == playerId and board[5][4] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[5][2] == playerId and board[5][3] == playerId and board[5][4] == playerId and board[5][5] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[5][3] == playerId and board[5][4] == playerId and board[5][5] == playerId and board[5][6] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")

	if board[0][0] == playerId and board[1][0] == playerId and board[2][0] == playerId and board[3][0] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][0] == playerId and board[2][0] == playerId and board[3][0] == playerId and board[4][0] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][0] == playerId and board[3][0] == playerId and board[4][0] == playerId and board[5][0] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[0][1] == playerId and board[1][1] == playerId and board[2][1] == playerId and board[3][1] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][1] == playerId and board[2][1] == playerId and board[3][1] == playerId and board[4][1] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][1] == playerId and board[3][1] == playerId and board[4][1] == playerId and board[5][1] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[0][2] == playerId and board[1][2] == playerId and board[2][2] == playerId and board[3][2] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][2] == playerId and board[2][2] == playerId and board[3][2] == playerId and board[4][2] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][2] == playerId and board[3][2] == playerId and board[4][2] == playerId and board[5][2] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[0][3] == playerId and board[1][3] == playerId and board[2][3] == playerId and board[3][3] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][3] == playerId and board[2][3] == playerId and board[3][3] == playerId and board[4][3] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][3] == playerId and board[3][3] == playerId and board[4][3] == playerId and board[5][3] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[0][4] == playerId and board[1][4] == playerId and board[2][4] == playerId and board[3][4] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][4] == playerId and board[2][4] == playerId and board[3][4] == playerId and board[4][4] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][4] == playerId and board[3][4] == playerId and board[4][4] == playerId and board[5][4] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[0][5] == playerId and board[1][5] == playerId and board[2][5] == playerId and board[3][5] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][5] == playerId and board[2][5] == playerId and board[3][5] == playerId and board[4][5] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][5] == playerId and board[3][5] == playerId and board[4][5] == playerId and board[5][5] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[0][6] == playerId and board[1][6] == playerId and board[2][6] == playerId and board[3][6] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[1][6] == playerId and board[2][6] == playerId and board[3][6] == playerId and board[4][6] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")
	if board[2][6] == playerId and board[3][6] == playerId and board[4][6] == playerId and board[5][6] == playerId:
		sys.exit("PlayerId "+str(playerId)+" won. Congratulations!\n")





	# for rowIndex in range(nRows):
	# 	for colIndex in range(nCols):
	# 		if board[rowIndex]


def startGame():
	for loop in range(21):
		print()
		movePlayer1 = 0
		try:
			while movePlayer1 <= 0 or movePlayer1 >= 8:
				movePlayer1 = int(input("Player 1 to move: "))
				print()
			colIndex = movePlayer1-1
		except:
			continue

		for i in range(5,-1,-1):
			if board[i][colIndex] == 0:
				rowIndex = i
				break
			if i == 0:
				print("This row is already full. Choose another one.")

		board[rowIndex][colIndex] = 1

		print()
		print(board)
		check4Win(board,1)


		print()
		movePlayer2 = 0
		try:
			while movePlayer2 <= 0 or movePlayer2 >= 8:
				movePlayer2 = int(input("Player 2 to move: "))
				print()
			colIndex = movePlayer2-1
		except:
			continue

		for i in range(5,-1,-1):
			if board[i][colIndex] == 0:
				rowIndex = i
				break
			if i == 0:
				print("This row is already full. Choose another one.")

		board[rowIndex][colIndex] = 2

		print()
		print(board)
		check4Win(board,2)

		if loop == 20:
			print("Game Over. It's a tie.")



startGame()