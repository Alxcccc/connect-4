from interfaces.board import Board
from modules.logging import Connecta4Logging

class Connect4Board(Board):
    
    def __init__(self, rows: int, columns: int, logging: Connecta4Logging):
        self._rows = rows
        self._columns = columns
        self._matrix = [[" " for _ in range(self._columns)] for _ in range(self._rows)]
        self.logging = logging
        
    def get_matrix(self):
        return self._matrix
        
    def show_matrix(self):
        print("+" + "   +" * self._columns)
        for row in self._matrix:
            print("|", end=" ")
            for element in row:
                print(f"{element} |", end=" ")
            print()
            print("+" + "   +" * self._columns)
    
    def reset_matrix(self):
        for i in range(self._rows):
            for j in range(self._columns):
                if self._matrix[i][j] != " ":
                    self._matrix[i][j] = " "
                else:
                    continue
                
    def put_token(self, user: str):
        try:
            position_token = int(input(f"{user} Enter the column where you want to put your token: ")) - 1
            
            if position_token > 6 or position_token < 0 :
                self.logging.info(f"Column's number that you picked is wrong, the board has {self._columns}.")
                self.put_token(user)
            
            elif self._matrix[0][position_token] != " ": 
                self.logging.info("There isn't space for another token in this column, try with other columns.")
                self.put_token(user)
            
            for rows in range(5,-1,-1): 
                if self._matrix[rows][position_token] != " ": 
                    pass
                else:
                    self._matrix[rows][position_token] = user[0]
                    return True
        except ValueError:
            self.logging.warning("You didn't write a number")
            self.put_token(user)