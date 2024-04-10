class Board:
    def __init__(self):
        self.cells = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.cells:
            print('|'.join(row))
            print('-' * 5)

    def update(self, row, col, symbol):
        if self.cells[row][col] == ' ':
            self.cells[row][col] = symbol
            return True
        else:
            print("This cell is already taken. Choose another one.")
            return False

    def is_winner(self, symbol):
        for row in self.cells:
            if all(cell == symbol for cell in row):
                return True
        for col in range(3):
            if all(self.cells[row][col] == symbol for row in range(3)):
                return True
        if all(self.cells[i][i] == symbol for i in range(3)):
            return True
        if all(self.cells[i][2 - i] == symbol for i in range(3)):
            return True
        return False


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                row = int(input("Enter row number (0, 1, or 2): "))
                col = int(input("Enter column number (0, 1, or 2): "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board.update(row, col, self.symbol):
                        break
                else:
                    print("Invalid input. Row and column must be between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")


def play_game():
    board = Board()
    player1 = Player('X')
    player2 = Player('O')
    current_player = player1

    while True:
        board.display()
        current_player.make_move(board)
        if board.is_winner(current_player.symbol):
            print(f"Player {current_player.symbol} wins!")
            break
        if all(cell != ' ' for row in board.cells for cell in row):
            print("It's a tie!")
            break
        current_player = player2 if current_player == player1 else player1


if __name__ == "__main__":
    play_game()
