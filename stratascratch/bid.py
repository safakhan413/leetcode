def leftover_bidders( bids, number_of_items ) :
	######### DO NOT MODIFY BELOW ###########
	myQueue = MySpecialQueue()
	
	for bid in bids:
		myQueue.insert(bid)
	for sale in range(number_of_items):
		myQueue.dequeue()

	return myQueue.queue if myQueue.queue else [None]
	######### DO NOT MODIFY ABOVE ###########

class MySpecialQueue:
	# from collections import 
	import heapq
	def __init__(self):
	# Do not change the variable name of self.queue
		self.queue = []
	
	def insert(self, data):
		# print('data im', data)
		self.queue.append(data)
		# pass  
	
	def dequeue(self):
		print('sello',  self.queue)
		maxElem = max(self.queue)
		print(maxElem, 'im maxane')
		self.queue.pop(self.queue.index(maxElem))
		# pass

bids=[1,2,3,4,5,6,7,8,9,]
number_of_items=2
# Input([1,2,3,4,5,6,7,8,9,], int(2))
print(leftover_bidders( bids, number_of_items ))