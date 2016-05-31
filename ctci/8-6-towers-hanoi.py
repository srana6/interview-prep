"""
Towers of Hanoi, classic

Only one disk can be moved at a time
A disk is slid off the top of one tower onto another tower
A disk cannot be placed on top of a smaller disk

Write a program to move the disks from the first tower to the last using stacks.

Analysis:
	There are few possible types of moves, using building pattern:

	N = 1:
		N1 to T3
			Move d1 T1 - T3

	N = 2
		N2 to T3
			N1 to T2
				Move d1 T1 - T2
			Move d2 T1 - T3
			Move d1 T2 - T3

	N = 3   
		N3 to T3
			N2 to T2
				Move d1 T1 - T3
				Move d2 T1 - T2
				Move d1 T3 - T2
			Move d3 T1 - T3

			N2 to T3

	We alternate between buffer and destination on each call
"""


class Tower(object):
	def __init__(self, index):
		self.stack = []
		self.index = index

	# Add one disk to this tower
	def add(self, disk):
		if self.stack and self.stack[-1] < disk:
			return
		self.stack.append(disk)

	# Move top disk from current tower to another
	def move_top_to(self, tower):
		if self.stack:
			top = self.stack.pop()
			tower.add(top)

	# Move disks from a tower to another
	def move_disk(self, N, dest, buff):
		if N > 0:
			self.move_disk(N - 1, buff, dest)
			self.move_top_to(dest)
			buff.move_disk(N - 1, dest, self)

	def __repr__(self):
		return str(self.stack)

def hanoi_towers(N):
	if N <= 0: return
	towers = []

	# Helper variables
	first = 0
	buff = 1
	last = 2

	# Initialize 3 towers
	for index in range(3):
		towers.append(Tower(index))
	
	# Add N disks to first Tower
	for disk in reversed(range(1, N + 1)):		
		towers[first].add(disk)

	# Move elements from first to last using buff as auxiliar
	towers[first].move_disk(N, towers[last], towers[buff])

hanoi_towers(4)