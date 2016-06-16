import collections
import sys
from utils import *
import re
import copy
#custom queue class for BFS
class Queue:
	def __init__(self):
		self.items = []
	def __contains__(self, item):
		if item in self.items:
			return True
		else:
			return False
	def isEmpty(self):
		return self.items == []
	def enqueue(self, item):
		if item not in self.items:
			self.items.insert(0,item)
			#print "inserted\/"
			#print item
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
q=Queue()


#return 0 for left, else 1 for right
def heur_search(current):
	#where the location of the room is located
	index = len(current)-1
	#farthest right room
	length = len(current)-2
	#the room the vacuum is currently in
	currentRoom = current[index] 

	existsLeft = False
	leftDistance = 0

	existsRight = False
	rightDistance = 0

	#DEFAULT MOVES
	#if the vacuum is in the farthest right room
	if current[index] == index:
		return 0
	#if the vacuum is in the farthest left room
	if current[index] == 0:
		return 1

	#checking the left side for dirty rooms
	for x in range(0, currentRoom):
		if current[x] == 1:
			existsLeft = True
			leftDistance = abs(currentRoom-x)
			break

	for x in range(currentRoom, index):
		if current[x] == 1:
			existsRight = True
			rightDistance = abs(currentRoom-x)

	if existsRight and existsLeft:
		if leftDistance <= rightDistance:
			return 0
		else:
			return 1
	elif existsLeft and not existsRight:
			return 0
	else:
		return 1

#return 0 for left, 1 up, 2 right, 3 down, 4 suck
def heur_search_meta(current):
	#where the location of the room is located
	index = len(current)-1
	#limit of ranges for x and y coord
	limit = len(current)-2
	xlimit = len(current[0])-1
	#the room the vacuum is currently in, is 2d so use it as currentRoom[][]
	currentRoom = current[index] 


	existsLeft = False
	leftDistance = 0

	existsRight = False
	rightDistance = 0

	#suck move
	if current[current[index][0]][current[index][1]] == 1:
		return 4

	#DEFAULT MOVE where there is a room dirty directly left, up, right, or down of the current
	#left
	if currentRoom[1] != 0:
		if current[currentRoom[0]][currentRoom[1]-1] == 1:
			return 0

	#up
	if currentRoom[0] != 0:
		if current[currentRoom[0]-1][currentRoom[1]] == 1:
			return 1

	#right
	if currentRoom[1] != xlimit:
		if current[currentRoom[0]][currentRoom[1]+1] == 1:
			return 2

	#down
	if currentRoom[0] != limit:
		if current[currentRoom[0]+1][currentRoom[1]] == 1:
			return 3

	#else, need to check ranges of the rooms that are diagonal of the current room
	#checking the left side for dirty rooms
	for x in range(currentRoom[1]):
		for y in range(currentRoom[0]):
			if current[y][x] == 1:
				existsLeft = True
				leftDistance = abs(currentRoom[0]-x) + abs(currentRoom[1]-y)
				break


	for x in range(currentRoom[1], xlimit+1):
			for y in range(currentRoom[0], index):
				if current[y][x] == 1:
					existsRight = True
					rightDistance = abs(currentRoom[0]-x) + abs(currentRoom[1]-y)

	if existsRight and existsLeft:
		#print leftDistance
		#print rightDistance
		if leftDistance <= rightDistance and currentRoom[1] != 0:
			return 0
		if currentRoom[0] != 0:
			return 1
	elif existsLeft:
		if currentRoom[1] != 0:
			return 0
		if currentRoom[0] != 0:
			return 1
	elif existsRight:
		if currentRoom[1] != xlimit:
			return 2
		if currentRoom[0] != limit:
			return 3


#depth limited search v3.0
def DLS_alpha_pure(depth, stack, path, pathQ):
	if not stack:
		return None
	node = stack.pop()
	pathS = pathQ.pop()
	flag1 = True
	flag2 = True
	flag = 0
	if(depth >= 0):
		for x in range((len(node)-1)):
			for y in range((len(node)-1)):
				if node[x][y] != 0:
					flag1 = False
		if node[len(node)-1][0] < 0 or node[len(node)-1][0] > (len(node)-2):
			flag2 = False
		if node[len(node)-1][1] < 0 or node[len(node)-1][1] > (len(node)-2):
			flag2 = False
		#check to see if the dls is finished with the index value flag and the room values
		if flag1 and flag2:
			#print "Done cleaning after tries"
			#print pathS
			return pathS
			#print "Current state still needs cleaning ::"
		#print node
		path.append(node)
		#temp = copy.deepcopy(current)
		if LRS_alpha(4,node) not in path and LRS_alpha(4,node) != node:
			stack.append(LRS_alpha(4,node))
			pathQ.append(pathS + "S")
			flag += 1
		if LRS_alpha(3,node) not in path and LRS_alpha(3,node) != node:	
			stack.append(LRS_alpha(3,node))
			#pathtemp.append(LRS_alpha(3,node))
			pathQ.append(pathS + "D")
			flag += 1
			#print "moved down"
		if LRS_alpha(2,node) not in path and LRS_alpha(2,node) != node:
			stack.append(LRS_alpha(2,node))
			#pathtemp.append(LRS_alpha(2,node))
			pathQ.append(pathS + "R")
			flag += 1
			#print "moved right"
		if LRS_alpha(1,node) not in path and LRS_alpha(1,node) != node:
			stack.append(LRS_alpha(1,node))
			#pathtemp.append(LRS_alpha(1,node))
			pathQ.append(pathS + "U")
			flag += 1
			#print "moved up"
		if LRS_alpha(0,node) not in path and LRS_alpha(0,node) != node:
			stack.append(LRS_alpha(0,node))
			#pathtemp.append(LRS_alpha(0,node))
			pathQ.append(pathS + "L")
			flag += 1
			#print "moved left"
			#print "moved suck"
	if(flag == 0):
		return DLS_alpha_pure(depth+1, stack, path, pathQ)
	else:
		return DLS_alpha_pure(depth-1, stack, path, pathQ)

#depth limited search v3.0
def DLS_alpha(depth, stack, path, pathQ):
	if not stack:
		return None
	length = len(stack)
	#print length
	#print "path"
	#print path
	if(depth >= 0):
		for x in range(length-1, -1, -1):
			#print stack[x]
			#print pathQ[x]
			if check_clean_alpha(stack[x]):
				#print "Done cleaning after tries"
				#print pathQ[x]
				return pathQ[x]

		newstack = []
		newpathQ = []
		#print "range length"
		#print range(length)
		for i in range(length):
			node = stack.pop()
			pathS = pathQ.pop()
			path.append(node)
			if LRS_alpha(0,node) not in path and LRS_alpha(0,node) != node:
				newstack.insert(0,LRS_alpha(0,node))
				newpathQ.insert(0,pathS + "L")
				#print "moved left"
			if LRS_alpha(1,node) not in path and LRS_alpha(1,node) != node:
				newstack.insert(0,LRS_alpha(1,node))
				newpathQ.insert(0,pathS + "U")
				#print "moved up"
			if LRS_alpha(2,node) not in path and LRS_alpha(2,node) != node:
				newstack.insert(0,LRS_alpha(2,node))
				newpathQ.insert(0,pathS + "R")
				#print "moved right"
			if LRS_alpha(3,node) not in path and LRS_alpha(3,node) != node:	
				newstack.insert(0,LRS_alpha(3,node))
				newpathQ.insert(0,pathS + "D")
				#print "moved down"
			if LRS_alpha(4,node) not in path and LRS_alpha(4,node) != node:
				newstack.insert(0,LRS_alpha(4,node))
				newpathQ.insert(0,pathS + "S")
				#print "moved suck"
		return DLS_alpha(depth-1, newstack, path, newpathQ)	

#depth limited search v2.0
def DLS_beta(depth, stack, path, pathQ):
	if not stack:
		return None
	length = len(stack)
	#print stack
	#print pathQ
	if(depth >= 0):
		for x in range(length-1, -1, -1):
			#print stack[x]
			#print pathQ[x]
			if check_clean_beta(stack[x]):
				#print "Done cleaning after tries"
				#print pathQ[x]
				return pathQ[x]
		newstack = []
		newpathQ = []		
		for i in range(length):
			node = stack.pop()
			#print node
			pathS = pathQ.pop()
			#print pathS
			path.append(node)
			flag = 0
			if LRS_beta(0,node) not in path and LRS_beta(0,node) != node:
				stack.insert(0,LRS_beta(0,node))
				#pathtemp.append(LRS_beta(0,node))
				pathQ.insert(0,pathS + "L")
				#print "moved left"
				flag +=1 
			if LRS_beta(1,node) not in path and LRS_beta(1,node) != node:
				stack.insert(0,LRS_beta(1,node))
				#pathtemp.append(LRS_alpha(1,node))
				pathQ.insert(0,pathS + "R")
				#print "moved right"
				flag += 1
			if LRS_beta(2,node) not in path and LRS_beta(2,node) != node:
				stack.insert(0,LRS_beta(2,node))
				pathQ.insert(0,pathS + "S")
				#print "moved suck"
				flag +=1
		if(flag == 0):
			return DLS_beta(depth+1, stack, path, pathQ)
		else:
			return DLS_beta(depth-1, stack, path, pathQ)




#depth limited search v3.0
def DLS_beta_pure(depth, stack, path, pathQ):
	if not stack:
		return -1
	node = stack.pop()
	pathS = pathQ.pop()
	flag1 = True
	flag2 = True
	if(depth >= 0):
		if check_clean_beta(node):
			#print node
			#print pathS
			return pathS

		#print "Current state still needs cleaning ::"
		#print node
		path.append(node)
		flag = 0
		if LRS_beta(2,node) not in path and LRS_beta(2,node) != node:
			stack.append(LRS_beta(2,node))
			pathQ.append(pathS + "S")
			flag += 1
			#print "moved suck"
		if LRS_beta(1,node) not in path and LRS_beta(1,node) != node:
			stack.append(LRS_beta(1,node))
			#pathtemp.append(LRS_alpha(1,node))
			pathQ.append(pathS + "R")
			flag += 1
			#print "moved right"
		if LRS_beta(0,node) not in path and LRS_beta(0,node) != node:
			stack.append(LRS_beta(0,node))
			#pathtemp.append(LRS_beta(0,node))
			pathQ.append(pathS + "L")
			flag += 1
			#print "moved left"
		if flag == 0:
			return DLS_beta_pure(depth+1, stack, path, pathQ)
		else:	
			return DLS_beta_pure(depth-1, stack, path, pathQ)
	

#depth limited search
def DLS(depth, stack, path, pathQ):
	if not stack:
		return None
	node = stack.pop()
	pathS = pathQ.pop()
	if(depth >= 0):
		if node == (0,0,0) or node == (0,0,1):
			#print "Done cleaning after tries"
			print pathS
			return True
		if LRS(2,node) not in path and LRS(2,node) != node:
			stack.append(LRS(2,node))
			path.append(LRS(2,node))
			pathQ.append(pathS + "S")
			#print "moved suck"
		if LRS(1,node) not in path and LRS(1,node) != node:	
			stack.append(LRS(1,node))
			path.append(LRS(1,node))
			pathQ.append(pathS + "R")
			#print "moved right"
		if LRS(0,node) not in path and LRS(0,node) != node:
			stack.append(LRS(0,node))
			path.append(LRS(0,node))
			pathQ.append(pathS + "L")
			#print "moved left"
		#print "Current depth: " + str(depth)
		DLS(depth-1, stack, path, pathQ)

#i dont think i ever used this
def IDDLS(depth, stack, path):
	if not stack:
		return None
	node = stack.pop()
	if depth == 0:
		if node == ('0','0','0') or node == ('0','0','1'):
			return node
	elif depth > 0:
		for x in range(2, -1, -1):
			if LRS(x,node) not in path and LRS(x,node) != node:
				stack.append(LRS(x,node))
				path.append(LRS(x,node))
				found = IDDLS(depth-1, stack, path)
				if found != None:
					return found
	return None





#cchecks if the current tuple is entirely clean
def check_clean_beta(current):
	roomrange = len(current)-1
	if int(current[roomrange]) < 0 or int(current[roomrange]) >= len(current):
		return False

	for x in range(roomrange):
		if(current[x] != 0):
			return False
	return True

#cchecks if the current tuple is entirely clean
def check_clean_alpha(current):
	roomrange = len(current)-1
	xlimit = len(current[0])-1
	ylimit = len(current)-2
	#print xlimit
	#print ylimit
	if int(current[roomrange][0]) < 0 or int(current[roomrange][0]) >= len(current):
		return False

	if int(current[roomrange][1]) < 0 or int(current[roomrange][1]) >= len(current):
		return False

	for x in range(xlimit+1):
		for y in range(ylimit+1):
			if(current[y][x] != 0):
				return False
	#print current
	return True

#cchecks if the current tuple is entirely clean
def check_clean(current):
	if(current == (0,0,1) or current == (0,0,0)):
		return True
	else:
		return False


""" calls a move on a current tuple and returns the modified tuple
	0 -> left
	1 -> right
	2 -> suck
	"""
def LRS(move, current):
	if current == None:
		return None
	if move == 0:
		temp = (current[0], current[1], 0)
		return temp
	if move == 1:
		temp = (current[0], current[1], 1)
		return temp
	if move == 2:
		if current[2] == 0:
			temp = (0, current[1], 0)
			return temp
		if current[2] == 1:
			temp = (current[0], 0, 1)
			return temp

def LRS_beta(move, current):
	if current == None:
		return None
	locIndex = len(current)-1
	roomRange = locIndex
	if move == 0:
		if current[locIndex] == 0:
			temp = copy.deepcopy(current)
			return temp
		else:
			temp = ()
			for x in range(roomRange):
				temp = temp + (current[x],)
			temp = temp + ((current[locIndex]-1),)
			return temp
	if move == 1:
		if current[locIndex] == roomRange-1:
			temp = copy.deepcopy(current)
			return temp
		else:
			temp = ()
			for x in range(roomRange):
				temp = temp + (current[x],)
			temp = temp + ((current[locIndex]+1),)
			return temp
	if move == 2:
		temp = ()
		for x in range(len(current)):
			if x != current[locIndex]:
				temp = temp + (current[x],)
			else:
				temp = temp + (0,)
		return temp




def LRS_alpha(move, current):
	if current == None:
		return None
	locIndex = len(current)-1
	limit = locIndex-1
	xlimit = len(current[0])-1
	roomRange = locIndex
	coords = current[len(current)-1]
	if move == 0:#LEFT
		if current[locIndex][1] == 0:
			temp = copy.deepcopy(current)
			return temp
		else:
			temp = copy.deepcopy(current)
			temp[locIndex][1] = (current[locIndex][1])-1
			return temp
	if move == 1:#UP
		if current[locIndex][0] == 0:
			temp = copy.deepcopy(current)
			return temp
		else:
			temp = copy.deepcopy(current)
			temp[locIndex][0] = (current[locIndex][0])-1
			return temp
	if move == 2:#RIGHT
		if current[locIndex][1] == xlimit:
			temp = copy.deepcopy(current)
			return temp
		else:
			temp = copy.deepcopy(current)
			temp[locIndex][1] = (current[locIndex][1])+1
			return temp
	if move == 3:#DOWN
		if current[locIndex][0] == limit:
			temp = copy.deepcopy(current)
			return temp
		else:
			temp = copy.deepcopy(current)
			temp[locIndex][0] = (current[locIndex][0])+1
			return temp
	if move == 4:#SUCK
		temp = copy.deepcopy(current)
		temp[temp[locIndex][0]][current[locIndex][1]] = 0
		return temp




"""DLS ALPHA FAILURE!
			if LRS_alpha(4,node) not in path and LRS_alpha(4,node) != node:
				stacktemp = copy.deepcopy(stack)
				pathtemp = copy.deepcopy(path)
				pathQtemp = copy.deepcopy(pathQ)
				stacktemp.append(LRS_alpha(4,node))
				#pathtemp.append(LRS_alpha(4,node))
				pathQtemp.append(pathS + "S")
				#print "moved suck"
				DLS_alpha(depth-1, stacktemp, pathtemp, pathQtemp)
			if LRS_alpha(3,node) not in path and LRS_alpha(3,node) != node:	
				stacktemp = copy.deepcopy(stack)
				pathtemp = copy.deepcopy(path)
				pathQtemp = copy.deepcopy(pathQ)
				stacktemp.append(LRS_alpha(3,node))
				#pathtemp.append(LRS_alpha(3,node))
				pathQtemp.append(pathS + "D")
				#print "moved down"
				DLS_alpha(depth-1, stacktemp, pathtemp, pathQtemp)
			if LRS_alpha(2,node) not in path and LRS_alpha(2,node) != node:
				stacktemp = copy.deepcopy(stack)
				pathtemp = copy.deepcopy(path)
				pathQtemp = copy.deepcopy(pathQ)
				stacktemp.append(LRS_alpha(2,node))
				#pathtemp.append(LRS_alpha(2,node))
				pathQtemp.append(pathS + "R")
				#print "moved right"
				DLS_alpha(depth-1, stacktemp, pathtemp, pathQtemp)
			if LRS_alpha(1,node) not in path and LRS_alpha(1,node) != node:
				stacktemp = copy.deepcopy(stack)
				pathtemp = copy.deepcopy(path)
				pathQtemp = copy.deepcopy(pathQ)
				stacktemp.append(LRS_alpha(1,node))
				#pathtemp.append(LRS_alpha(1,node))
				pathQtemp.append(pathS + "U")
				#print "moved up"
				DLS_alpha(depth-1, stacktemp, pathtemp, pathQtemp)
			if LRS_alpha(0,node) not in path and LRS_alpha(0,node) != node:
				stacktemp = copy.deepcopy(stack)
				pathtemp = copy.deepcopy(path)
				pathQtemp = copy.deepcopy(pathQ)
				stacktemp.append(LRS_alpha(0,node))
				#pathtemp.append(LRS_alpha(0,node))
				pathQtemp.append(pathS + "L")
				print "moved left"
				DLS_alpha(depth-1, stacktemp, pathtemp, pathQtemp)
			#print "Current depth: " + str(depth)
			#DLS_alpha(depth-1, stack, path, pathQ)
"""

