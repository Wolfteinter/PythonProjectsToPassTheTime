import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import copy
import math
from tkinter import messagebox 

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(width=500, height=500)
        self.root.title("Tic Tac Toe")
        self._initialState()
        self.root.mainloop()
    def _initialState(self):
        self.state = [[0,0,0],[0,0,0],[0,0,0]]
        helv36 = tkFont.Font(family='Helvetica', size=25, weight=tkFont.BOLD)
        f = tk.Frame(width=100,height=100)
        self.b1 = tk.Button(f, text ="", font=helv36,command=lambda:self._changePlayerState(1))
        f.rowconfigure(0, weight = 1)
        f.columnconfigure(0, weight = 1)
        f.grid_propagate(0)
        f.grid(row = 0, column = 0)
        self.b1.grid(sticky = "NWSE")

        f = tk.Frame(width=100,height=100)
        self.b2 = tk.Button(f, text ="", font=helv36, command=lambda:self._changePlayerState(2))
        f.rowconfigure(0, weight = 1)
        f.columnconfigure(0, weight = 1)
        f.grid_propagate(0)
        f.grid(row = 1, column = 0)
        self.b2.grid(sticky = "NWSE")

        f = tk.Frame(width=100,height=100)
        self.b3 = tk.Button(f, text ="", font=helv36, command=lambda:self._changePlayerState(3))
        f.rowconfigure(0, weight = 1)
        f.columnconfigure(0, weight = 1)
        f.grid_propagate(0)
        f.grid(row = 2, column = 0)
        self.b3.grid(sticky = "NWSE")

        f = tk.Frame(width=100,height=100)
        self.b4 = tk.Button(f, text ="", font=helv36, command=lambda:self._changePlayerState(4))
        f.rowconfigure(0, weight = 1)
        f.columnconfigure(0, weight = 1)
        f.grid_propagate(0)
        f.grid(row = 0, column = 1)
        self.b4.grid(sticky = "NWSE")

        f = tk.Frame(width=100,height=100)
        self.b5 = tk.Button(f, text ="", font=helv36, command=lambda:self._changePlayerState(5))
        f.rowconfigure(0, weight = 1)
        f.columnconfigure(0, weight = 1)
        f.grid_propagate(0)
        f.grid(row = 1, column = 1)
        self.b5.grid(sticky = "NWSE")

        f = tk.Frame(width=100,height=100)
        self.b6 = tk.Button(f, text ="", font=helv36, command=lambda:self._changePlayerState(6))
        f.rowconfigure(0, weight = 1)
        f.columnconfigure(0, weight = 1)
        f.grid_propagate(0)
        f.grid(row = 2, column = 1)
        self.b6.grid(sticky = "NWSE")

        f = tk.Frame(width=100,height=100)
        self.b7 = tk.Button(f, text ="", font=helv36, command=lambda:self._changePlayerState(7))
        f.rowconfigure(0, weight = 1)
        f.columnconfigure(0, weight = 1)
        f.grid_propagate(0)
        f.grid(row = 0, column = 2)
        self.b7.grid(sticky = "NWSE")

        f = tk.Frame(width=100,height=100)
        self.b8 = tk.Button(f, text ="", font=helv36, command=lambda:self._changePlayerState(8))
        f.rowconfigure(0, weight = 1)
        f.columnconfigure(0, weight = 1)
        f.grid_propagate(0)
        f.grid(row = 1, column = 2)
        self.b8.grid(sticky = "NWSE")

        f = tk.Frame(width=100,height=100)
        self.b9 = tk.Button(f, text ="", font=helv36, command=lambda:self._changePlayerState(9))
        f.rowconfigure(0, weight = 1)
        f.columnconfigure(0, weight = 1)
        f.grid_propagate(0)
        f.grid(row = 2, column = 2)
        self.b9.grid(sticky = "NWSE")
    def _changePlayerState(self, position):
        if position == 1:
            self.state[0][0] = 1
            self.b1.configure(text='X')
        elif position == 2:
            self.state[1][0] = 1
            self.b2.configure(text='X')
        elif position == 3:
            self.state[2][0] = 1
            self.b3.configure(text='X')
        elif position == 4:
            self.state[0][1] = 1
            self.b4.configure(text='X')
        elif position == 5:
            self.state[1][1] = 1
            self.b5.configure(text='X')
        elif position == 6:
            self.state[2][1] = 1
            self.b6.configure(text='X')
        elif position == 7:
            self.state[0][2] = 1
            self.b7.configure(text='X')
        elif position == 8:
            self.state[1][2] = 1
            self.b8.configure(text='X')
        elif position == 9:
            self.state[2][2] = 1
            self.b9.configure(text='X')
        if self._isComplete(self.state):
            messagebox.showinfo(message="TIE", title="RESULT")
        elif(self._evaluateAction(self.state) == 1):
            messagebox.showinfo(message="YOU WON", title="RESULT")
        #print(self._evaluateAction(self.state))
        else:
            self._actionFromComputer()
    def _evaluateAction(self, state):
        #Verticals and horizontals
        for i in range(3):
            if state[i][0] == 1 and state[i][1] == 1 and state[i][2] == 1:
                return 1
            if state[i][0] == -1 and state[i][1] == -1 and state[i][2] == -1:
                return -1   
        for i in range(3):
            if state[0][i] == 1 and state[1][i] == 1 and state[2][i] == 1:
                return 1
            if state[0][i] == -1 and state[1][i] == -1 and state[2][i] == -1:
                return -1
        #Diagonals
        if state[0][0] == 1 and state[1][1] == 1 and state[2][2] == 1:
            return 1
        if state[0][0] == -1 and state[1][1] == -1 and state[2][2] == -1:
            return -1
            
        if state[0][2] == 1 and state[1][1] == 1 and state[2][0] == 1:
            return 1
        if state[0][2] == -1 and state[1][1] == -1 and state[2][0] == -1:
            return -1
        #No one win
        return 0

    def _isComplete(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return False
        return True
    
    def _minmax(self, board, isMax):
        score = self._evaluateAction(board)
        if (score != 0):
            return score
        if self._isComplete(board):
            return 0
        if(isMax):
            best = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = 1
                        best = max(best, self._minmax(copy.deepcopy(board), False))
                        board[i][j] = 0
                        if best == 1:
                            return best
            return best
        else:
            best = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = -1
                        best = min(best, self._minmax(copy.deepcopy(board), True))
                        board[i][j] = 0
            return best

    def _findBestMove(self):
        bestVal = math.inf;
        bestMove = [-1, -1];
        board = copy.deepcopy(self.state)
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1;
                    moveVal = self._minmax(copy.deepcopy(board), True)
                    board[i][j] = 0
                    if moveVal < bestVal:
                        bestMove = [i, j]
                        bestVal = moveVal
        return bestMove
                

    def _actionFromComputer(self):
        y, x = self._findBestMove()
        self.state[y][x] = -1

        if y == 0:
            if x == 0:
                self.b1.configure(text='O')
            elif x == 1:
                self.b4.configure(text='O')
            elif x == 2:
                self.b7.configure(text='O')
        elif y == 1:
            if x == 0:
                self.b2.configure(text='O')
            elif x == 1:
                self.b5.configure(text='O')
            elif x == 2:
                self.b8.configure(text='O')
        elif y == 2:
            if x == 0:
                self.b3.configure(text='O')
            elif x == 1:
                self.b6.configure(text='O')
            elif x == 2:
                self.b9.configure(text='O')
        if self._isComplete(self.state):
            messagebox.showinfo(message="TIE", title="RESULT")
        elif(self._evaluateAction(self.state) == -1):
            messagebox.showinfo(message="YOU LOST", title="RESULT")

t = TicTacToe()