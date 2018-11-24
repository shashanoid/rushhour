## Author -- Shashwat Singh
## Assignment 1 - CS380

import sys
from Board import Board

#Function that takes in command line args
def play_game(command, args=None):
	default_board_string = "  oaa |  o   |xxo   |ppp  q|     q|     q"
	if command == "print":
		if args:
			game_board = Board(args)
		else:
			game_board = Board(default_board_string)
		print game_board
	elif command == "done":
		if args:
			game_board = Board(args)
		else:
			game_board = Board(default_board_string)
		print game_board.done()
	elif command == "next":
		if args:
			game_board = Board(args)
		else:
			game_board = Board(default_board_string)
		game_board.vehicle_orientation()
		game_board.next()
	elif command == "random":
		if args:
			game_board = Board(args)
		else:
			game_board = Board(default_board_string)
			game_board.vehicle_orientation()
			game_board.random_walk()
	elif command == "bfs":
		if args:
			game_board = Board(args)
		else:
			game_board = Board(default_board_string)
			game_board.vehicle_orientation()
			game_board.bfs_random()




if __name__ == "__main__":
	arg_len = len(sys.argv)
	if arg_len == 3:
		play_game(sys.argv[1], sys.argv[2])
	else:
		play_game(sys.argv[1])