from tkinter import messagebox

win = False
current_player = True

board =  [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def print_board(board):
    for row in board:
        print(row)

def update_board(board, user_input, new_value, buttons):
  row = (user_input - 1) // 3
  col = (user_input - 1) % 3
  if (board[row][col] == 'X' or board[row][col] == 'O'):
    return False
  board[row][col] = new_value
  buttons[row][col]['text'] = new_value

def check_win(board, buttons):
    # Horizontal
    for row in range(3):
       if board[row][0] == board[row][1] == board[row][2] != '0':
           return True
    # Vertical
    for col in range(3):
       if board[0][col] == board[1][col] == board[2][col] != '0': 
           return True
    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] != '0': 
        return True
    if board[2][0] == board[1][1] == board[0][2] != '0': 
        return True

    count = 9
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X' or board[row][col] == 'O': count -= 1
    if count < 1:
        return 'Tie'
    return False

def make_turn(board, index, buttons):
    user_choice = index
    symbol = 'X' if current_player else 'O'
    update_board(board, user_choice, symbol, buttons)
    print_board(board)

def gameloop(index, buttons, label):
    global current_player
    make_turn(board, index, buttons)
    check = check_win(board, buttons)
    if check == True:
        for row in buttons:
            for btn in row:
                btn.state(['disabled'])
        string = 'Player', 'X' if current_player else 'O', 'wins!'
        print(string)
        messagebox.showinfo(message=string)
        label['text'] = string
    elif check == 'Tie':
        for row in buttons:
            for btn in row:
                btn.state(['disabled'])
        string = 'Game is tied!'
        print(string)
        messagebox.showinfo(message=string)
        label['text'] = string
    else:
        if label['text'] == 'Turn: X':
            label['text'] = 'Turn: O'
        else:
            label['text'] = 'Turn: X'
        current_player = not current_player

print_board(board)

def reset_array():
    global board
    global current_player
    current_player = True
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    print_board(board)