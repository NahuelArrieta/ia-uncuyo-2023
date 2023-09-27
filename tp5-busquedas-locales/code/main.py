from hill_climbing import *
from board import *

board = Board(8)
board.print_board()
hill_climbing = HillClimbing(board, 100)
hill_climbing.print_last_board()
print(hill_climbing.get_iterations())