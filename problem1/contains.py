from collections import deque
queue = deque([(0,0,1), (1,1,1), (0,1,2)])
queue.append((0,0,0))           # Terry arrives
queue.append((1,0,1))          # Graham arrives
if (0,0,1) in queue:
	print "yupyup"
print queue.popleft()                 # The first to arrive now leaves
print queue.popleft()                 # The second to arrive now leavesprint
print queue                           # Remaining queue in order of arrival
