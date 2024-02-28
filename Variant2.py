import tkinter as tk
import random


#выбирает из списка рандомное слово
def choose_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()
        return random.choice(words).strip().lower()
#print(choose_word('sonad2.txt'))




class QuadraticEquationSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Quadratic Equation Solver")
        self.create_labels()
        self.create_virtual_keyboard()

    def create_labels(self):
        self.labels = [[None]*6 for _ in range(6)]
        for i in range(6):
            for j in range(6):
                if (i, j) == (0, 0) or (i, j) == (0, 1) or (i, j) == (0, 2) or (i, j) == (0, 3) or (i, j) == (0, 4) or (i, j) == (0, 5):
                    self.labels[i][j] = tk.Label(self.master, text=" ", font=("Arial", 14))
                else:
                    self.labels[i][j] = tk.Label(self.master, text="1", font=("Arial", 14))
                self.labels[i][j].grid(row=i+1, column=j+1, padx=5, pady=5)

    def update_label(self, event):
        char = event.widget.cget("text")
        row = int(event.widget.grid_info()["row"]) - 1
        col = int(event.widget.grid_info()["column"]) - 1
        self.labels[row][col].config(text=char)

    def create_virtual_keyboard(self):
        buttons = [
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        ]

        for i, row in enumerate(buttons, start=8):
            for j, char in enumerate(row):
                button = tk.Button(self.master, text=char, width=4)
                button.grid(row=i, column=j, padx=5, pady=5)
                button.bind("<Button-1>", self.update_label)

def main():
    root = tk.Tk()
    app = QuadraticEquationSolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
