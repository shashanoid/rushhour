import collections
import copy
from collections import OrderedDict
from sets import Set
import random

import Queue


#Initilizing the board
class Board:
	def __init__(self, board_string):
		self.string = board_string.split("|")
		self.original_board = [[x for x in x] for x in self.string]
		self.board = [[x for x in x] for x in self.string]
		self.orientation = {}
		self.boards = [self.original_board]
		self.init_board = copy.deepcopy(self.board)
		self.board_set = Set()
		self.random_walks = []
		
		self.tree_queues = Queue.Queue()
		self.tree_queues.enqueue(self.original_board)

	#resets the original board
	def reset(self):
		self.board = copy.deepcopy(self.init_board)

	def __eq__(self, other):
		return self.board == other.board

	#Prints the board from 2d array
	def __str__(self):
		s =  " " + "-" * 6 + "\n"

		for row in self.board:
			s = s + '|{0}|\n'.format(''.join(row))

		s = s + " " + "-" * 6 

		return s

	def print_board(self, board):
		s =  " " + "-" * 6 + "\n"

		for row in board:
			s = s + '|{0}|\n'.format(''.join(row))

		s = s + " " + "-" * 6

		return s

	
	#Checks if the solution state has been reached
	def done(self):
		solution_reached = False

		for row in self.board:
			if row[4] == "x" and row[5] == "x":
				solution_reached = True

		return solution_reached

	def done_board(self, board):
		solution_reached = False

		for row in board:
			if row[4] == "x" and row[5] == "x":
				solution_reached = True

		return solution_reached
			

	#Maps out different vehicle orientations	
	def vehicle_orientation(self):
		strings = self.string

		for string in strings:
			new_string = string.replace(' ', '')

			results = collections.Counter(new_string)

			for key,val in results.iteritems():
				if val >= 2:
					self.orientation.update({key:'h'})
				else:
					self.orientation.update({key:'v'})

	#Moves the vehicle in one step in whatever direction provided
	def next_in_direction(self, i, j, di, dj):
		car_char = self.board[i][j]
		if self.orientation[car_char] == 'h':
			lj = ''.join(self.board[i]).rindex(car_char)
			if dj > 0 and (lj + 1) < len(self.board[i]) and self.board[i][lj+1] == ' ':
				self.board[i][j] = ' '
				self.board[i][lj + 1] = car_char
			elif dj < 0 and (j - 1) >= 0 and self.board[i][j - 1] == ' ':
				self.board[i][lj] = ' '
				self.board[i][j - 1] = car_char
		else:
			li = ''.join([k[j] for k in self.board]).rindex(car_char)
			if di < 0 and (li + 1) < len(self.board) and self.board[li + 1][j] == ' ':
				self.board[i][j] = ' '
				self.board[li + 1][j] = car_char
			elif di > 0 and (i - 1) >= 0 and self.board[i - 1][j] == ' ':
				self.board[li][j] = ' '
				self.board[i - 1][j] = car_char



	def get_locations(self, board, letter, direction):
		location = ''.join([''.join(row) for row in board]).index(letter)
		row = location / len(board)
		start_location = location % len(board)

		return(row, start_location)
	

	#Generates all possible moves of a vehicle
	def next(self):
		boards = []
		temp_board = self
		new_state = None
		for letter, direction in self.orientation.iteritems():
			if direction == "h":
				for i in xrange(-6, 6):
					coord = self.get_locations(temp_board.board, letter, direction)
					new_state = self.next_in_direction(coord[0], coord[1], 0, i)

					if self.board not in self.boards and self.board != self.original_board:
						self.boards.append(copy.deepcopy(self.board))

				temp_board.reset()
			
		for letter, direction in self.orientation.iteritems():
			if direction == "v":
				for i in xrange(-6,6):
					coord = self.get_locations(temp_board.board, letter, direction)
					new_state = self.next_in_direction(coord[0], coord[1], i, 0)

					if self.board not in self.boards and self.board != self.original_board:
						self.boards.append(copy.deepcopy(self.board))

				temp_board.reset()

		for board in self.boards:
			print self.print_board(board)


	# Does a random walk 10 times and stops if it found a solution.
	def random_walk(self):
		temp_board = self
		counter = 0
		d = self.orientation
		keys = list(d.keys())

		while counter < 10:
			random.shuffle(keys)

			random_orientation = [(key, d[key]) for key in keys]

			if self.done() == True:
				break
			else:
				for letter, direction in random_orientation:
					if direction == "h":
						coord = self.get_locations(temp_board.board, letter, direction)
						self.next_in_direction(coord[0], coord[1], 0, random.randint(-1, 1))

						if self.board not in self.boards and self.board != self.original_board:
							self.boards.append(copy.deepcopy(self.board))
					else:
						coord = self.get_locations(temp_board.board, letter, direction)
						self.next_in_direction(coord[0], coord[1], random.randint(-1, 1), 0)

						if self.board not in self.boards and self.board != self.original_board:
							self.boards.append(copy.deepcopy(self.board))

			counter = counter + 1

		# Does a random walk 10 times and stops if it found a solution.
	def bfs_random(self):
		temp_board = self
		counter = 0
		d = self.orientation
		keys = list(d.keys())

		while self.done() != True:
			random.shuffle(keys)

			random_orientation = [(key, d[key]) for key in keys]

			if self.done() == True:
				break
			else:
				for letter, direction in random_orientation:
					if direction == "h":
						coord = self.get_locations(temp_board.board, letter, direction)
						self.next_in_direction(coord[0], coord[1], 0, random.randint(-1, 1))

						if self.board not in self.boards and self.board != self.original_board:
							self.boards.append(copy.deepcopy(self.board))
					else:
						coord = self.get_locations(temp_board.board, letter, direction)
						self.next_in_direction(coord[0], coord[1], random.randint(-1, 1), 0)

						if self.board not in self.boards and self.board != self.original_board:
							self.boards.append(copy.deepcopy(self.board))

			counter = counter + 1

		for board in self.boards:
			print self.print_board(board)

		print counter

	
	#Generates all possible moves of a vehicle
	def next_move(self, target):
		boards = []
		for letter, direction in self.orientation.iteritems():
			temp_board = copy.deepcopy(target)
			if direction == "h":
				for i in xrange(-1, 2,2):
					coord = temp_board.get_locations(temp_board.board, letter, direction)
					temp_board.next_in_direction(coord[0], coord[1], 0, i)
					if temp_board not in boards:
						boards.append(temp_board)
			if direction == "v":
				for i in xrange(-1,2,2):
					coord = temp_board.get_locations(temp_board.board, letter, direction)
					temp_board.next_in_direction(coord[0], coord[1], i, 0)
					if temp_board not in boards:
						boards.append(temp_board)
		return boards
	
	def BFS(self):
		visited = []
		paths = [[self]]
		while paths:
			cur_path = paths.pop(0)
			print len(paths)
			print '\n'.join([str(board) for board in cur_path])
			last_board = cur_path[-1]
			if last_board.done():
				return cur_path
			if last_board not in visited:
				visited.append(last_board)
			for move in last_board.next_move(last_board):
				if move not in visited:
					new_path = list(cur_path)
					new_path.append(move)
					paths.append(new_path)