import sys
input = sys.stdin.readline
class CircularQueue:
	def __init__(self, n = 10001):
		self.data = [None]  * (n)
		self.rear = 0
		self.front = 0
		self.size = n
	def isFull(self):
		return int((self.rear + 1)%self.size == self.front)
	def enqueue(self, n):
		if self.isFull():
			return -1
		self.rear = (self.rear + 1) % self.size
		self.data[self.rear] = n
	def isEmpty(self):
		return int(self.front == self.rear)
	def dequeue(self):
		if self.isEmpty():return -1
		self.front = (self.front + 1) % self.size
		return self.data[self.front]
	def getSize(self):
		return ((self.rear - self.front + self.size) if self.front >self.rear else (self.rear - self.front))% self.size
	def getFront(self):
		if self.isEmpty():return -1
		return self.data[(self.front + 1)%self.size]
	def getBack(self):
		if self.isEmpty():return -1
		return self.data[self.rear]

q = CircularQueue()
c = {"push":q.enqueue, "pop":q.dequeue, "size":q.getSize, "empty":q.isEmpty, "back":q.getBack, "front":q.getFront}
_case = int(input())
for _ in range(_case):
	got = input().strip().split()
	if len(got) == 2:
		ret = c[got[0]](int(got[1]))
		if ret != None:
			print(ret)
	else:
		print(c[got[0]]())