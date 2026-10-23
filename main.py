class coins:
    def __init__(self, player1="boom", player2="clap"):
        self.player1 = player1
        self.player2 = player2


class board:
    def __init__(self, length: int):
        self.length = length
        self.board = [length * ["O"] for row in range(self.length)]
        self.coin = coins()

    def display(self):
        for row in range(self.length - 1, -1, -1):
            print(self.board[row])

    def check_win_condition(self):
        counter = 0
        for i in range(self.length):
            for j in range(self.length):
                if self.board[i][j] == self.board[i][j + 1]:
                    counter += 1
        for i in range(self.length):
            x = self.board[i]
            counter_2 = 0
            for j in range(len(x)):
                if x[j] == x[j + 1]:
                    counter_2 += 1

            if counter == 4:
                return True  # add a method thing so that i can get the playes colours

                # player1 /length = 4/6 then it wins

    # some matrix down stuff
    # pass
    def insert(self, colours, x, y):
        self.board[x][y] = colours

    def prop(self):
        pass


if __name__ == "__main__":
    con = coins()
    chicken = board(6)
    chicken.display()
    chicken.insert(con.player1, 1, 3)
    chicken.display()
