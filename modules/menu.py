from interfaces.menu import Menu
from interfaces.context import Context
from interfaces.punctuation import Punctuation
from modules.logging import Connecta4Logging
from modules.board import Connect4Board
from modules.check_winner import CheckWinner



class Connect4Menu(Menu):
    def __init__(self, context_play: Context, context_exit: Context, punctuation: Punctuation, board: Connect4Board, check_winner: CheckWinner, logging: Connecta4Logging):
        self.options = {1: "Play Connect 4", 2: "Reset Point", 3: "Exit"}
        self.logging = logging
        self.punctuation = punctuation
        self.board = board
        self.check_winner = check_winner
        self.context_play = context_play
        self.context_exit = context_exit
        
        
    def show_menu(self):
        self.show_options()
        op = self.catch_option()
        self.call_fuctions(op)
        
        
    def show_options(self):
        for num, description in self.options.items():
            print(f"{num}: {description}")
            
    def catch_option(self) -> int:
        try:
            option_choice = int(input("Write the option that you want to pick: "))
            if not option_choice in self.options:
                self.logging.info(f"The option that you choice is not valid: {option_choice}")
                return None
            return option_choice
        except ValueError:
            self.logging.warning("You should give me an option value")
            self.catch_option()
            
    def call_fuctions(self, option: int):
        if option == 1:
            self.context_play.execute_logic()
        if option == 2:
            self.punctuation.reset_point()
        if option == 3:
            self.context_exit.execute_logic()
        