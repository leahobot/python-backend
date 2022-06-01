import random


tic_tac_board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-", ]
player = "x"
game_playing = True
winner = None


print("Welcome to the tic-tac-toe game")


def board(tic_tac_board):
    print(tic_tac_board[0] + "|" + tic_tac_board[1] + "|" + tic_tac_board[2])
    print("------")
    print(tic_tac_board[3] + "|" + tic_tac_board[4] + "|" + tic_tac_board[5])
    print("------")
    print(tic_tac_board[6] + "|" + tic_tac_board[7] + "|" + tic_tac_board[8])


def player_input(tic_tac_board):
    user_input = int(input("Enter a number from 1-9:> "))
    if (user_input >= 1 and user_input <= 9 and tic_tac_board[user_input-1] == "-"):
        tic_tac_board[user_input - 1] = player
    else:
        print("This spot is occupied...")


def horizontal_board(tic_tac_board):
    global winner
    if(tic_tac_board[0] == tic_tac_board[1] == tic_tac_board[2] and tic_tac_board[0] != "-"):
        winner = tic_tac_board[0]
        return True
    elif(tic_tac_board[3] == tic_tac_board[4] == tic_tac_board[5] and tic_tac_board[3] != "-"):
        winner = tic_tac_board[3]
        return True
    elif(tic_tac_board[6] == tic_tac_board[7] == tic_tac_board[8] and tic_tac_board[6] != "-"):
        winner = tic_tac_board[6]
        return True


def vertical_board(tic_tac_board):
    global winner
    if(tic_tac_board[0] == tic_tac_board[3] == tic_tac_board[6] and tic_tac_board[0] != "-"):
        winner = tic_tac_board[0]
        return True
    elif(tic_tac_board[1] == tic_tac_board[4] == tic_tac_board[7] and tic_tac_board[1] != "-"):
        winner = tic_tac_board[1]
        return True
    elif(tic_tac_board[2] == tic_tac_board[5] == tic_tac_board[8] and tic_tac_board[2] != "-"):
        winner = tic_tac_board[2]
        return True


def diagonal_board(tic_tac_board):
    global winner
    if(tic_tac_board[0] == tic_tac_board[4] == tic_tac_board[8] and tic_tac_board[0] != "-"):
        winner = tic_tac_board[0]
        return True
    elif(tic_tac_board[2] == tic_tac_board[4] == tic_tac_board[6] and tic_tac_board[2] != "-"):
        winner = tic_tac_board[2]
        return True


def tie(tic_tac_board):
    global game_playing
    if ("-" not in tic_tac_board):
        board(tic_tac_board)
        print("Its a Tie!!")
        game_playing = False


def switch_player():
    global player
    if (player == "x"):
        player = "o"
    else:
        player = "x"


def win():
    if horizontal_board(tic_tac_board) or vertical_board(tic_tac_board) or diagonal_board(tic_tac_board):
        print(f"The winner is {winner}")


def com_player(tic_tac_board):
    while player == "o":
        position = random.randrange(8)
        if tic_tac_board[position] == "-":
            tic_tac_board[position] = "o"
            switch_player()


while game_playing:
    board(tic_tac_board)
    player_input(tic_tac_board)
    win()
    tie(tic_tac_board)
    switch_player()
    com_player(tic_tac_board)
    win()
    tie(tic_tac_board)
