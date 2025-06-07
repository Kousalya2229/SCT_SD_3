import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Solver")

        self.entries = [[None for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(master, width=2, font=("Arial", 18), justify="center")
                entry.grid(row=i, column=j, padx=(0 if j % 3 != 0 else 5), pady=(0 if i % 3 != 0 else 5))
                self.entries[i][j] = entry

        solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            board.append(row)
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    self.entries[i][j].insert(0, str(board[i][j]))

    def is_valid(self, board, num, pos):
        row, col = pos
        for i in range(9):
            if board[row][i] == num and i != col:
                return False
            if board[i][col] == num and i != row:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False
        return True

    def solve(self, board):
        empty = next(((i, j) for i in range(9) for j in range(9) if board[i][j] == 0), None)
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = 0
        return False

    def solve_sudoku(self):
        board = self.get_board()
        if self.solve(board):
            self.set_board(board)
            messagebox.showinfo("Success", "Sudoku solved successfully!")
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
