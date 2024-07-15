import tkinter as tk
from tkinter import ttk
from tictactoe_logic import gameloop

def make_gui():
    root = tk.Tk()
    root.geometry('300x300')
    root.title('TicTacToe')
    make_buttongrid(root)
    root.mainloop()

def make_buttongrid(root):
    buttons = []
    for row in range(3):
        buttons.append([])
        root.grid_rowconfigure(row, weight=1)
        for col in range(3):
            root.grid_columnconfigure(col, weight=1)
            make_button(root, row, col, buttons)
            
def make_button(root, row, col, buttons):
    button = ttk.Button(root)
    button.grid(row=row, column=col, sticky='NSEW')
    buttons[row].append(button)
    button.config(command=lambda r=row, c=col: on_button_click(r, c, buttons))

def on_button_click(row, col, buttons):
    gameloop(3 * row + col + 1, buttons)