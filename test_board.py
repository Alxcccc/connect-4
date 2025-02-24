from modules.board import Connect4Board
from modules.logging import Connecta4Logging

logging = Connecta4Logging()
board = Connect4Board(rows=6, columns=7, logging=logging)
while True:
    if board.put_token(user="Alxc"):
        board.show_matrix()