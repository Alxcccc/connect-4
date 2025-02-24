from interfaces.strategy import Strategy
from modules.board import Connect4Board
from modules.punctuation import Connect4Punctuation
from modules.logging import Connecta4Logging
from modules.check_winner import CheckWinner

class PlayGame(Strategy):
    def __init__(self, board: Connect4Board, punctuation: Connect4Punctuation, win: CheckWinner, logging: Connecta4Logging):
        self.board = board
        self.punctuation = punctuation
        self.logging = logging
        self.win = win
        self.turn = "R"
    
    def do_algorithm(self):
        if self.options() == True:
            return None
        self.board.show_matrix()
        self.punctuation.show()
        if self.turn == "R":
            self.board.put_token(self.turn)
            if self.win.check_win() == None:
                self.turn = "B"
                self.do_algorithm()
                return None
            self.punctuation.show()
            input()
            self.board.reset_matrix()
            return None
            
        else: 
            self.board.put_token(self.turn)
            if self.win.check_win() == None:
                self.turn = "R"
                self.do_algorithm()
            self.punctuation.show()
            input()
            self.board.reset_matrix()
            return None
        
    def options(self):
        opcion = input("If you want to reset the match you should write 'r' or if you want to exit of match you should write 'e' and if just want to continue with the match press enter: ").strip()
        if opcion == "r":
            input("The match reset succesfully, please press enter")
            self.board.reset_matrix()
            self.turn = "R"
            self.do_algorithm()
        elif opcion == "e":
            self.board.reset_matrix()
            return True