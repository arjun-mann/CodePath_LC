class TicTacToe:
    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]
    
    def play(self) -> None:
        self.board = [[' '] * 3 for i in range(3)]
        p1turn = True
        for i in range(9):
            x = -1
            y = -1
            if p1turn:
                while True:
                    try:
                        turn = input("p1: Enter your move: ")
                        x, y = turn.split()
                        x = int(x)
                        y = int(y)
                        if x > 2 or x < 0 or y > 2 or y < 0: raise ValueError()
                        if self.board[x][y] != " ": raise ValueError()
                        break
                    except ValueError:
                        print("invalid input! Please try again")
                self.board[x][y] = 'X'
            else:
                while True:
                    try:
                        turn = input("p2: Enter your move: ")
                        x, y = turn.split()
                        x = int(x)
                        y = int(y)
                        if x > 2 or x < 0 or y > 2 or y < 0: raise ValueError()
                        if self.board[x][y] != " ": raise ValueError()
                        break
                    except ValueError:
                        print("invalid input! Please try again")
                self.board[x][y] = 'O'
            p1turn = not p1turn
            self.printboard()
            if self.winner('X', x, y):
                print('p1 wins!')
                break
            elif self.winner('O', x, y):
                print('p2 wins!')
                break
        else:
            print("Tie!")
            
    def printboard(self) -> None:
        for i in range(3):
            print('|', end = " ")
            for j in range(3):
                print(self.board[i][j], end=" ")
            print('|')
            
    def winner(self, ch, x, y) -> bool:
        for i in range(3):
            if self.board[x][i] != ch:
                break
        else:
            return True
        for i in range(3):
            if self.board[i][y] != ch:
                break
        else:
            return True
        for i in range(3):
            if self.board[i][i] != ch:
                break
        else:
            return True
        for i in range(3):
            if self.board[i][2-i] != ch:
                break
        else:
            return True
        return False
            
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
