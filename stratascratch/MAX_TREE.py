def special_tree( values, k ) :
	####### DO NOT MODIFY THE CODE BELOW #######
	myTree = MySpecialTree(values)
	soln = []
	for val in range(k):
		soln.append(myTree.pop_max_value())

	return soln
	####### DO NOT MODIFY THE CODE ABOVE #######

class MySpecialTree():
		def __init__(self, values=None):
			self.data = values or []
			for x in range(len(values)//2, -1, -1):
				self.__max_treeify__(x)

		def parent(self, x):
			return x >> 1

		def left_child(self, x):
			return (x << 1) + 1

		def right_child(self, x):
			return (x << 1) + 2

		def __max_treeify__(self, x):
			pass

		def pop_max_value(self):
			pass

values = [1,8,3,0,4,2,9]
k =1
output is 9

val = [1,8,3,0,4,2,9] 
k =3
out = [9,8,4]