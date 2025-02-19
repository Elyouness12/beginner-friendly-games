from tkinter import messagebox

win = False
current_player = True

board =  [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def print_board(board):
    for row in board:
        print(row)
    print()

def update_board(board, user_input, new_value, buttons):
  row = (user_input - 1) // 3
  col = (user_input - 1) % 3
  if (board[row][col] == 'X' or board[row][col] == 'O'):
    return False
  board[row][col] = new_value
  buttons[row][col]['text'] = new_value

def check_win(board):
    # Horizontal
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '0':
            return True, [(row, 0), (row, 1), (row, 2)]
    # Vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '0':
            return True, [(0, col), (1, col), (2, col)]
    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] != '0':
        return True, [(0, 0), (1, 1), (2, 2)]
    if board[2][0] == board[1][1] == board[0][2] != '0':
        return True, [(2, 0), (1, 1), (0, 2)]

    count = 9
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X' or board[row][col] == 'O':
                count -= 1
    if count < 1:
        return 'Tie', []

    return False, []

def make_turn(board, index, buttons):
    user_choice = index
    symbol = 'X' if current_player else 'O'
    update_board(board, user_choice, symbol, buttons)
    print_board(board)

def gameloop(r, c, buttons, label):
    global current_player
    index = 3 * r + c + 1
    make_turn(board, index, buttons)
    check, positions = check_win(board)
    if check == True:
        for pos in positions:
            if current_player:
                buttons[pos[0]][pos[1]].config(style='X.TButton')
            else:
                buttons[pos[0]][pos[1]].config(style='O.TButton')
        for row in buttons:
            for btn in row:
                btn.state(['disabled'])
        string = 'Player', 'X' if current_player else 'O', 'wins!'
        print(string, '\n')
        label['text'] = string
        messagebox.showinfo(message=string)
    elif check == 'Tie':
        for row in buttons:
            for btn in row:
                btn.state(['disabled'])
                btn.config(style='Tie.TButton')
        string = 'Game is tied!'
        print(string, '\n')
        label['text'] = string
        messagebox.showinfo(message=string)
    else:
        label['text'] = 'Turn: ' + ('O' if current_player else 'X')
        current_player = not current_player

print()
print_board(board)

def reset_array():
    global board
    global current_player
    current_player = True
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    print_board(board)