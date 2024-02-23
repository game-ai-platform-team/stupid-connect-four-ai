import random
import numpy as np

class ConnectFour:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((rows, columns), dtype=int)
        self.player = 1
        self.game_over = False

    def drop_piece(self, column):
        if not self.game_over:
            if (
                self.board[self.rows - 1][column] == 0
            ):  # Check if the bottom row of the column is empty
                for r in range(self.rows):
                    if self.board[r][column] == 0:
                        self.board[r][column] = self.player
                        if self.check_win(r, column):
                            self.game_over = True
                        self.player = 3 - self.player  # Switch player
                        return True
            else:
                return False
        else:
            return False

    def check_win(self, row, column) -> bool:
        # Check horizontal
        for c in range(self.columns - 3):
            if (
                self.board[row][c] == self.player
                and self.board[row][c + 1] == self.player
                and self.board[row][c + 2] == self.player
                and self.board[row][c + 3] == self.player
            ):
                return True

        # Check vertical
        for r in range(self.rows - 3):
            if (
                self.board[r][column] == self.player
                and self.board[r + 1][column] == self.player
                and self.board[r + 2][column] == self.player
                and self.board[r + 3][column] == self.player
            ):
                return True

        # Check positively sloped diagonals
        for r in range(self.rows - 3):
            for c in range(self.columns - 3):
                if (
                    self.board[r][c] == self.player
                    and self.board[r + 1][c + 1] == self.player
                    and self.board[r + 2][c + 2] == self.player
                    and self.board[r + 3][c + 3] == self.player
                ):
                    return True

        # Check negatively sloped diagonals
        for r in range(3, self.rows):
            for c in range(self.columns - 3):
                if (
                    self.board[r][c] == self.player
                    and self.board[r - 1][c + 1] == self.player
                    and self.board[r - 2][c + 2] == self.player
                    and self.board[r - 3][c + 3] == self.player
                ):
                    return True

        return False
    
    def get_board(self):
        return self.board

    def print_board(self):
        for row in reversed(range(self.rows)):
            print("|", end="")
            for col in range(self.columns):
                if self.board[row][col] == 0:
                    print(" ", end="|")
                elif self.board[row][col] == 1:
                    print("X", end="|")
                else:
                    print("O", end="|")
            print()
        print("-" * (self.columns * 2 + 1))
        print(" " + " ".join(str(i) for i in range(self.columns)))

    def is_valid_location(self, column):
        return self.board[self.rows - 1][column] == 0

    def get_valid_locations(self) -> list[int]:
        valid_locations = []
        for col in range(self.columns):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def is_board_full(self):
        return np.all(self.board != 0)



class ConnectFourEngine:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.game = ConnectFour(rows, columns)
    
    def make_move(self, move:str):
        self.game.drop_piece(int(move))
    
    def get_best_move(self) -> str:
        valid_moves =self.game.get_valid_locations()
                
        return str(random.choice(valid_moves))
    
    def get_game_state(self) -> list[list[int]]:
        return self.game.get_board
 
if __name__ == "__main__":
    game = ConnectFour()
    game.print_board()
    while not game.game_over:
        try:
            move = input()
            if move != "":
                col = int(move)
                game.drop_piece(col)
            legal_moves = game.get_valid_locations()

            choice = random.choice(legal_moves)
            game.drop_piece(choice)
            print("MOVE: " + str(choice))
            
        except ValueError:
            print("Invalid input. Please enter a valid column number.")