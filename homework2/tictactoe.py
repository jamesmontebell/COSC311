def print_board(board):
    print("   |   |   ")
    print(" "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+" ")
    print("   |   |   ")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_board(board)
    player = 'X'
    while True:
        print("It's " + player + "'s turn.")
        row = int(input("Enter a row (1-3): ")) - 1
        col = int(input("Enter a column (1-3): ")) - 1
        if board[row][col] == 'X' or board[row][col] == 'O':
            print("That space is already taken. Try again.")
            continue
        board[row][col] = player
        print_board(board)
        if check_win(board, player):
            print("Congratulations, " + player + " wins!")
            break
        if all([x != ' ' for row in board for x in row]):
            print("It's a tie!")
            break
        player = 'O' if player == 'X' else 'X'

tic_tac_toe()
