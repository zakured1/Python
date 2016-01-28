#!/usr/bin/python
class Queue(object):
	def __init__(self):
		self.queue=list()
	def pop(self):
		self.queue.pop(0)
	def push(self,value):
		self.queue.append(value)
	def isempty(self):
		return len(self.queue)==0
	def top(self):
		if self.isempty():
			return None
		return self.queue[0]

a=Queue()
print a.isempty()
a.push(1)
print a.isempty()
a.pop()
print a.isempty()
a.push(1)
a.push(2)
print a.top()

