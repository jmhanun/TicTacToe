class TicTacToe:
    def __init__(self, content):
        self.content = content.replace("_", " ")
        self.matrix = [list(self.content[i:i+3]) for i in range(0,len(self.content),3)]
        self.combs = self.get_all()
        self.player = "X"

    def get_row(self, row):
        return self.matrix[row]

    def get_col(self, col):
        return [row[col] for row in self.matrix]

    def get_diagonal(self, left_2_right=True):
        length = len(self.matrix[0])
        if left_2_right:
            return [self.matrix[i][i] for i in range(length)]
        return [self.matrix[length - 1 - i][i] for i in range(length - 1, -1, -1)]

    def __str__(self):
        return "-" * 9 + "\n" + "| " + " ".join(self.get_row(0)) + " |\n" + \
                "| " + " ".join(self.get_row(1)) + " |\n" + \
                "| " + " ".join(self.get_row(2)) + " |\n" + "-" * 9

    def content_2_matrix(self):
        self.matrix = [list(self.content[i:i+3]) for i in range(0,len(self.content),3)]
        self.combs = self.get_all()

    def matrix_2_content(self):
        self.content = ''.join(char for sub in self.matrix for char in sub)
        self.combs = self.get_all()

    def get_all(self):
        all_comb = []
        for i in range(3):
            all_comb.append(self.get_row(i))
            all_comb.append(self.get_col(i))
        all_comb.append(self.get_diagonal(True))
        all_comb.append(self.get_diagonal(False))
        return all_comb

    def x_wins(self):
        for comb in self.combs:
            if len(set(comb)) == 1 and comb[0] == "X":
                return True
        return False

    def o_wins(self):
        for comb in self.combs:
            if len(set(comb)) == 1 and comb[0] == "O":
                return True
        return False

    def complete(self):
        return self.content.count("X") + self.content.count("O") == 9

    def check(self):
        if self.x_wins() and self.o_wins():
            return "Impossible"
        if abs(self.content.count("X") - self.content.count("O")) >= 2:
            return "Impossible"
        if self.x_wins():
            return "X wins"
        if self.o_wins():
            return "O wins"
        if self.complete():
            return "Draw"
        return "Game not finished"

    def occupied(self, col, row):
        return self.matrix[3 - row][col - 1] != " "

    def set_cell(self, col, row, value):
        self.matrix[3 - row][col - 1] = value
        self.matrix_2_content()
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"


cells = " " * 9
game = TicTacToe(cells)
print(game)
ok = False
data = input("Enter the coordinates: ")
while not ok:
    x, y = "x", "x"
    if " " in data:
        x, y = data.split()
    if not x.isnumeric() or not y.isnumeric():
        print("You should enter numbers!")
        data = input("Enter the coordinates: ")
        continue
    x, y = int(x), int(y)
    if not (1 <= x <= 3) or not (1 <= y <= 3):
        print("Coordinates should be from 1 to 3!")
        data = input("Enter the coordinates: ")
        continue
    if game.occupied(x, y):
        print("This cell is occupied! Choose another one!")
        data = input("Enter the coordinates: ")
        continue
    game.set_cell(x, y, game.player)
    print(game)
    if game.check() in ["X wins", "O wins", "Draw"]:
        print(game.check())
        ok = True
    else:
        data = input("Enter the coordinates: ")
