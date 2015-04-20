#task 1: create dynamic array

class create_massiv ():
	def __init__(self):	#create array
		self.arr = []
	def __del__(self):	#delete array
		del self.arr
	def insert(self, n):	#insert elem to the array
		self.arr.append(n)
	def dump(self):		#dump array to the screen
		for i in range (len(self.arr)):
			print self.arr[i]



	
	
	
			


	
	
