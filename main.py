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
        print(self.check_column())
        print(self.check_row())

    def check_row(self):
        for i in range(self.length):
            x = self.board[i]
            counter_2 = 0
            for j in range(len(x) - 1):
                if x[j] == x[j + 1]:
                    counter_2 += 1

            if counter_2 == 4:
                return [
                    True,
                    x,
                    counter_2,
                ]  # add a method thing so that i can get the playes colours
        return "checks not found "
        # player1 /length = 4/6 then it wins

    def check_column(self):
        for i in range(self.length - 1):
            counter_1 = 0
            for j in range(self.length - 1):
                if self.board[i][j] == self.board[i + 1][j]:
                    symbol = self.board[i][j]
                    counter_1 += 1
            if counter_1 == 4:
                return [True, symbol, counter_1, i]
        return "No column wins"

    # some matrix down stuff
    # pass
    def insert(self, colours, x, y):
        self.board[x][y] = colours

    def play(self):
        pass

    def prop(self):
        pass


if __name__ == "__main__":
    con = coins()
    chicken = board(6)
    chicken.display()
    chicken.insert(con.player1, 1, 0)
    chicken.insert(con.player1, 1, 1)
    chicken.insert(con.player1, 1, 2)
    chicken.insert(con.player1, 1, 3)
    chicken.insert(con.player1, 0, 3)
    chicken.insert(con.player1, 1, 3)
    chicken.insert(con.player1, 2, 3)

    chicken.insert(con.player1, 2, 3)
    chicken.insert(con.player1, 3, 3)

    print(chicken.check_win_condition())
    chicken.display()
    print(chicken.board[0][0])
