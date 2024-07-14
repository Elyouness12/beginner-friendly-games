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
            

def make_button(root, row, col) -> ttk.Button:
    new_tile = ttk.Button(root, text=F'{3 * row + col + 1}')
    new_tile.grid(row=row, column=col, sticky='NSEW')
    new_tile.config(command=lambda b=new_tile: game_loop(int(b.cget('text'))))
    return new_tile