from modules.board import Connect4Board
from modules.logging import Connecta4Logging
from modules.punctuation import Connect4Punctuation


class CheckWinner():
    def __init__(self, board: Connect4Board, punctuation: Connect4Punctuation, logging: Connecta4Logging):
        self.board = board.get_matrix()
        self.board_rows = board._rows
        self.punctuation = punctuation
        self.logging = logging
        
    def check_win(self):
        if self.check_vertical() == "R" or self.check_horizontal() == "R" or self.check_diagonal_right() == "R" or self.check_diagonal_left() == "R":
            self.punctuation.increment_points(user="R")
            print("The winner is Red")
            return True
        elif self.check_vertical() == "B" or self.check_horizontal() == "B" or self.check_diagonal_right() == "B" or self.check_diagonal_left() == "B":
            self.punctuation.increment_points(user="B")
            print("The winner is Blue")
            return True
        else:
            return None
        
    def check_diagonal_right(self):
        for rows in range(self.board_rows-1,-1,-1):
            for columns in range(self.board_rows+1):
                count_r, count_b = 1, 1
                if self.board[rows][columns] != " ":
                    if columns + 3 > self.board_rows: 
                        return False
                    for i in range(1, 4):
                        if self.board[rows][columns] == "R":
                            if self.board[rows-i][columns+i] == "R":
                                count_r += 1
                                if count_r == 4:
                                    return "R"
                            else:
                                count_r = 0
                        elif self.board[rows][columns] == "B":
                            if self.board[rows-i][columns+i] == "B":
                                count_b +=1
                                if count_b == 4:
                                    return "B"
                            else:
                                count_b = 0

    def check_diagonal_left(self):
        for rows in range(self.board_rows-1,-1,-1):
            for columns in range(self.board_rows, -1, -1):
                count_r, count_b = 1, 1
                if self.board[rows][columns] != " ":
                    if columns-3 < 0: 
                        return False
                    for i in range(1, 4):
                        if self.board[rows][columns] == "R":
                            if self.board[rows-i][columns-i] == "R":
                                count_r += 1
                                if count_r == 4:
                                    return "R"
                            else:
                                count_r = 0
                        elif self.board[rows][columns] == "B":
                            if self.board[rows-i][columns-i] == "B":
                                count_b +=1
                                if count_b == 4:
                                    return "B"
                            else:
                                count_b = 0

    def check_vertical(self):
        for rows in range(self.board_rows+1):
            count_r, count_b = 0, 0
            for columns in range(5,-1,-1):
                if self.board[columns][rows] == "R":
                    count_b = 0
                    count_r += 1
                    if count_r == 4:
                        return "R"
                elif self.board[columns][rows] == "B":
                    count_r = 0
                    count_b += 1
                    if count_b == 4:
                        return "B"
                else:
                    count_r = 0
                    count_b = 0
        return None

    def check_horizontal(self):
        for columns in range(self.board_rows):
            count_r, count_b = 0, 0
            for rows in range(self.board_rows+1):
                if self.board[columns][rows] == "R":
                    count_b = 0
                    count_r += 1
                    if count_r == 4:
                        return "R"
                elif self.board[columns][rows] == "B":
                    count_r = 0
                    count_b += 1
                    if count_b == 4:
                        return "B"
                else:
                    count_r = 0
                    count_b = 0
        return None