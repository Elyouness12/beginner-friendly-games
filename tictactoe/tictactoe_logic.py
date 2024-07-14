# Players
Win = False

# Game Board
board =  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Display Game Board
def print_board(board):
    for row in board:
        print(row)

# Ask for user choice
def get_user_input(player):
  while True:
      user_input = int(input(player+" Enter a number from 1 to 9: "))
      if 1 <= user_input <= 9:
        return user_input
      else:
        print("Invalid input. Please enter a number between 1 and 9.")

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

# Player one Role
def player_one_role(board):
    user_choice = get_user_input("player 1 (X)")
    update_board(board, user_choice, 'X')
    print_board(board)

# Player two Role
def player_two_role(board):
    user_choice = get_user_input("player 2 (O)")
    update_board(board, user_choice, 'O')
    print_board(board)

# Game Loop
def game_loop():
    player1_turn = True
    while True:
        if player1_turn:
            player_one_role(board)
        else:
            player_two_role(board)

        if win_check(board):
            print("Player", "1" if player1_turn else "2", "wins!")
            break  # Exit the loop if there's a winner
        
        player1_turn = not player1_turn


   
print_board(board)
game_loop()
