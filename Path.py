# Board 1 -- "  oaa |  o   |  oxx |  pppq|     q|     q"
#Board 2 -- "  oaa |  o   |xxo   |ppp  q|     q|     q"

from Board import Board
import random

Board = Board("  oaa |  o   |xxo   |ppp  q|     q|     q")
Board.vehicle_orientation()
#Board.next()

# Board.next_trees(Board.boards[4])
#l = [[' ', ' ', 'o', 'a', 'a', ' '], [' ', ' ', 'o', ' ', ' ', ' '], ['x', 'x', 'o', ' ', ' ', ' '], ['p', 'p', 'p', ' ', ' ', 'q'], [' ', ' ', ' ', ' ', ' ', 'q'], [' ', ' ', ' ', ' ', ' ', 'q']]
# Board.next_trees(Board.board)
Board.random_walk()