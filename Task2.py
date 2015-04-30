from random import random
import threading

class TreeNode():
	def __init__(self, key):  #init node
		self.key = key
		self.left = None
		self.right = None

	def printn(self, depth):  #print key of node
		print '-'*depth+str(self.key)
		if self.left != None: self.left.printn(depth+1)
		if self.right != None: self.right.printn(depth+1)
		
	def sumn(self, s):  #summa keys of tree/recurrence relation
		s[0] += self.key
		if self.left != None: self.left.sumn(s)
		if self.right != None: self.right.sumn(s)
		
	def parsumn(self, proc, s, thr):  #parallel threads
		if proc == 1:	
			t = threading.Thread(target=self.sumn, args=(s,))	
			t.start()
			thr.append(t)
			return
				
		s[0] += self.key
		if (self.left == None and self.right == None): return
		if (self.left == None): 
			self.right.parsumn(proc, s, thr)
			return
		if (self.right == None):
			self.left.parsumn(proc, s, thr)
			return
		self.left.parsumn(proc/2, s, thr)
		self.right.parsumn(proc-proc/2, s, thr)
		
class BinaryTree():
	def __init__(self):	#initialization of the tree
		self.root = TreeNode(0)
		
	def add_node(self,key):	#add a node
		cur = self.root
		while True:
			if(random() < 0.5):
				if cur.left == None: 
					cur.left = TreeNode(key)
					return
				cur = cur.left
			else:
				if cur.right == None: 
					cur.right = TreeNode(key)
					return
				cur = cur.right

	def printt(self): #summa keys of tree 
		self.root.printn(0)
		
	def sumt(self): #summa keys of tree/ a simple count
		s = list()
		s.append(0)
		self.root.sumn(s)
		return s[0]

	def parsumt(self, proc):  #parallel threads
		s = list()
		s.append(0)
		thr = list()
		self.root.parsumn(proc, s, thr)
		for t in thr:
			t.join()
		return s[0]

a = BinaryTree()
for i in xrange(100):
	a.add_node(i)
#a.printt()
print a.sumt()  #a simple count
print a.parsumt(4)  #parallel threads
