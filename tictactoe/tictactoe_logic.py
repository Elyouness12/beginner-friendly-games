from tkinter import messagebox

# Players
Win = False

# Game Board
board =  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

player_x = True

# Display Game Board
def print_board(board):
    for row in board:
        print(row)

# Update Board based on user choice
def update_board(board, user_input, new_value):
  row = (user_input - 1) // 3
  col = (user_input - 1) % 3
  board[row][col] = new_value

# Check for wining
def win_check(board):
    # Horizontal check
    for row in range(3):
       if   board[row][0] == board[row][1] == board[row][2] != '0':
            return True

    # Vertical check
    for col in range(3):
       if   board[0][col] == board[1][col] == board[2][col] != '0':
            return True

    # X check
    if board[0][0] == board[1][1] == board[2][2] != '0':
        return True
    if board[2][0] == board[1][1] == board[0][2] != '0':
        return True

    return False

def player_role(board, index):
    user_choice = index
    if player_x == True:
        symbol = 'X'
    else:
        symbol = 'O'
    update_board(board, user_choice, symbol)
    print_board(board)

# Game Loop
def game_loop(index):
    global player_x
    player_role(board, index)
    if win_check(board):
        string = "Player", "1" if player_x else "2", "wins!"
        print(string)
        messagebox.showinfo(message=string)
    player_x = not player_x
    return player_x
 
print_board(board)