import tkinter as tk
from tkinter import ttk
from tictactoe_logic import gameloop, reset_array, current_player

def make_gui():
    root = tk.Tk()
    root.geometry('300x300')
    root.title('TicTacToe')
    label = ttk.Label(root, text='Turn: X')
    label.configure(anchor="center")
    label.grid(sticky='NSEW', row=4, column= 1)
    buttons = make_buttongrid(root, label)
    reset_button = ttk.Button(root, text='Reset', command=lambda: reset_board(root, buttons, label))
    reset_button.grid(sticky='NSEW', row=4, column= 2)
    root.mainloop()

def make_buttongrid(root, label):
    buttons = []
    for row in range(3):
        buttons.append([])
        root.grid_rowconfigure(row, weight=1)
        for col in range(3):
            root.grid_columnconfigure(col, weight=1)
            make_button(root, row, col, buttons, label)
    return buttons
            
def make_button(root, row, col, buttons, label):
    button = ttk.Button(root)
    button.grid(row=row, column=col, sticky='NSEW')
    buttons[row].append(button)
    button.config(command=lambda r=row, c=col: on_button_click(r, c, buttons, label))

def on_button_click(row, col, buttons, label):
    if buttons[row][col]['text'] in ['X', 'O']:
        return
    gameloop(row, col, buttons, label)

def reset_board(root, buttons, label):
    for row in buttons:
        for btn in row:
            btn.destroy()
    make_buttongrid(root, label)
    reset_array()
    label['text'] = 'Turn: X'