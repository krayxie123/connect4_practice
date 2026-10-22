class coins:
    pass


class board:
    def __init__(self, length: int):
        self.length = length
        self.board = [length * ["O"] for row in range(self.length)]

    def display(self):
        for row in range(self.length):
            print(self.board[row])


if __name__ == "__main__":
    chicken = board(6)
    print(chicken.display())
