from array import create_massiv
import random

class test():
	def test1(self):
		mas = create_massiv()
		for i in range (5):
			l = random.randint(0,100)
			mas.insert(l)
		mas.dump()
	def test2(self):
		mas = create_massiv()
		mas.insert(10)
		mas.insert(16)
		mas.dump()
		

	
test = test()
test.test1()
test.test2()
	
