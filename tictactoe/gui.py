import tkinter as tk
from tkinter import ttk

def make_gui():
    # Create root window and configure
    root = tk.Tk()
    root.geometry('400x400')
    root.title('TicTacToe')

    make_buttongrid(root)
    
    root.mainloop()

def make_buttongrid(root):
    for row in range(3):
        # Configure layout
        root.grid_rowconfigure(row, weight=1)
        root.grid_columnconfigure(row, weight=1)
        for col in range(3):
            # Make button and set layout
            new_tile = ttk.Button(root, text=F'{row}_{col}')
            new_tile.grid(row=row, column=col, sticky='NSEW')