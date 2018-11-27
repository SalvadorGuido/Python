import numpy as np
from numpy import random
import matplotlib.pyplot as plot

class maze:
	def __init__(self):
		self.size = ()
		self.grid = np.asarray([])
		self.start = ()
		self.goal = ()
		self.c_pos = ()


	def c_grid(self,rows = 9,columns = 9):
		b = []
		c = []
		self.size = (rows,columns)
		for i in range(rows):
			for j in range(columns):
				if (i%2 == 0 or j%2 == 0):
					b.append(1)
				else:
					if(i == rows or j == columns):
						print(i,j)
						b.append(1)		
					else:
						b.append(0)
			c.append(b)
			b = []
		self.start_p()
		self.goal_p()
		self.c_position(self.start)
		self.grid = np.asarray(c)

	def start_p(self):
		self.start = (self.size[0]-2,1)

	def goal_p(self):
		self.goal = (1, self.size[1]-2)

	def c_position(self, pos):
		self.c_pos = pos

	def move_up(self):
		if(self.c_pos[0]- 2 >= 1):
			self.grid[self.c_pos[0]-1,self.c_pos[1]] = 0
			self.c_pos = (self.c_pos[0]-2,self.c_pos[1])

	def move_down(self):
		if(self.c_pos[0]+ 2 < self.size[0]):
			self.grid[self.c_pos[0]+1,self.c_pos[1]] = 0
			self.c_pos = (self.c_pos[0]+2,self.c_pos[1])

	def move_right(self):
		if(self.c_pos[1]+2 < self.size[1]):
			self.grid[self.c_pos[0],self.c_pos[1]+1] = 0
			self.c_pos = (self.c_pos[0],self.c_pos[1]+2)

	def move_left(self):
		if(self.c_pos[1]-2 >= 1):
			self.grid[self.c_pos[0],self.c_pos[1]-1] = 0
			self.c_pos = (self.c_pos[0],self.c_pos[1]-2)


	def solve(self):
		while(self.c_pos != self.goal):
			value = int(random.randint(100,size=1))
			if(value < 25):
				self.move_up()
			elif(value > 25 and value < 50):
				self.move_down()
			elif(value > 50 and value < 75):
				self.move_left()
			else:
				self.move_right()

class Node:
	
	def __init__(self, value = ()):
		self.value = value
		self.parent = None
		self.LChild = None
		self.RChild = None



class Tree:

	def __init__(self):
		self.root = None



print('-'*50)		
matrix = maze()
matrix.c_grid(55,55)
print('Current Position: 	{}'.format(matrix.c_pos))
print('Goal: 				{}'.format(matrix.goal))
print(matrix.grid)
print('-'*50)
matrix.solve()
print('Current Position: 	{}'.format(matrix.c_pos))
print('Goal: 				{}'.format(matrix.goal))
print(matrix.grid)
print('-'*50)
plot.imshow(matrix.grid,cmap='binary') 'dsffs' == s 
plot.show()
