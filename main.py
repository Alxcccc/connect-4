from modules.menu import Connect4Menu
from modules.punctuation import Connect4Punctuation
from modules.logging import Connecta4Logging
from modules.check_winner import CheckWinner
from modules.board import Connect4Board
from modules.exit_game import ExitGame
from modules.play_connect4 import PlayGame
from interfaces.context import Context

if __name__ == "__main__":
    logging = Connecta4Logging()
    board = Connect4Board(rows=6, columns=7, logging=logging)
    punctuation = Connect4Punctuation(logging)
    check = CheckWinner(board, punctuation, logging)
    context_play = Context(PlayGame(board, punctuation, check, logging))
    context_exit = Context(ExitGame())
    menu = Connect4Menu(context_play, context_exit, punctuation, board, check, logging)
    while True:
        menu.show_menu()