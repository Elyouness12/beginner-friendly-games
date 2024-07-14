import tkinter as tk
from tkinter import ttk
from tictactoe_logic import game_loop

def make_gui():
    # Create root window and configure
    root = tk.Tk()
    root.geometry('310x300')
    root.title('TicTacToe')

    make_buttongrid(root)
    
    root.mainloop()

def make_buttongrid(root):
    for row in range(3):
        # Configure layout
        root.grid_rowconfigure(row, weight=1)
        for col in range(3):
            root.grid_columnconfigure(col, weight=1)
            # Make button and set layout
            make_button(root, row, col)
            

def make_button(root, row, col):
    button = ttk.Button(root)
    button.grid(row=row, column=col, sticky='NSEW')
    button.config(command=lambda r=row, c=col, b=button: on_button_click(r, c, b))
    return button

def on_button_click(row, col, b):
    turn = game_loop(3 * row + col + 1)
    symbol = 'O' if turn else 'X'
    b.config(text=symbol)