class Stack:
	def __init__(self):
		self.e = []
	def push(self, item):
		self.e.append(item)

	def peek(self):
		if (len(self.e) != 0):
			return self.e[-1]
		else:
			return "Error"
	def pop(self):
		self.e.pop()

	def is_empty(self):
		return len(self.e)== 0

	def __str__(self):
		arr = ""
		for i in range(len(self.e)-1,-1,-1):
			arr = arr + f"{self.e[i]}" + " "
		arr.strip()
		return arr
	def __len__(self):
		return len(self.e)
# s =Stack()
# s.push(5)
# s.push(4)
# s.push(6)
# s.pop()
# print(s)