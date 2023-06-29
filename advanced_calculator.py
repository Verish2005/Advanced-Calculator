from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		self.history = Stack()
		
	def evaluate_expression(self, input_expression):
		tokens = self.tokenize(input_expression)
		ans =  self.evaluate_list_tokens(tokens)
		self.history.push((input_expression,ans))
		return ans
	def tokenize(self, input_expression):
		s = input_expression
		l = []
		i = 0
		while i < len(s):
			if s[i].isdigit():
				t = ""
				while s[i].isdigit():
					t += s[i]
					i += 1
					if i == len(s):
						break
				l.append(int(t))
			elif s[i]!=" ":
				l.append(s[i])
				i += 1
			else:
				i += 1
		return l
	def check_brackets(self, list_tokens):
		d = {"(":-1,"{":-2,")":1,"}":2}
		s= Stack()
		for i in list_tokens:
			if i in d:
				if s.is_empty():
					s.push(d[i])
				else:
					t = s.peek()
					if d[i] - t == -1:
						return False
					else:
						s.push(d[i])
		ans = 0
		# print(s,"a")
		while(s.is_empty() == False):
			t  = s.peek()
			ans += t
			s.pop()
		if ans == 0:
			return True
		else:
			return False
	def evaluate_list_tokens(self, list_tokens):
		"""
		Evaluate the expression passed as a list of tokens
		Return the final answer as a float, and "Error" in case of division by zero and other errors
		"""
		list_tokens = ["{"] + list_tokens + ["}"]
		# print(list_tokens)
		d = {"(":-1,"{":-2,")":1,"}":2}
		comb = {"(":-1,"{":-2,")":1,"}":2,"+":1,"-":1,"*":2,"/":2}
		precdence= {"+":1,"-":1,"*":2,"/":3}
		c1 = 0
		c2 = 0
		for i in list_tokens:
			if i in precdence:
				c2 += 1
			else:
				if type(i) == int:
					c1 += 1
		if c1-c2 != 1:
			return "Error"
		operand = Stack()
		opbrac = Stack()
		ans = None
		if self.check_brackets(list_tokens):
			for i in list_tokens:
				print(operand,opbrac)
				if type(i) == int:
					operand.push(i)
				else:
					if i in d:
						if d[i]>0:
							if opbrac.is_empty() == True:
								# print("b")
								return "Error"
							while comb[opbrac.peek()]>0:
								if operand.is_empty() == True:
									return "Error"
								a = operand.peek()
								operand.pop()
								if operand.is_empty() == True:
									return "Error"
								b = operand.peek()
								operand.pop()
								op = opbrac.peek()
								opbrac.pop()
								if op == "+":
									ans = a + b
								elif op == "-":
									if opbrac.peek() == "-":
										ans = b + a
									else:
										ans = b-a
								elif op == "*":
									ans = b*a
								elif op == "/":
									if a == 0:
										return "Error"
									ans = b/a
								else:
									return "Error"
								# print(ans,"c")
								# print(a,b,ans,operand,opbrac,"c")
								operand.push(ans)
								# print(opbrac)
							opbrac.pop()
							# print(opbrac)
						else:
							opbrac.push(i)
					else:
						if opbrac.is_empty()== False:
							op = opbrac.peek()
							while op in precdence:
								if precdence[i] < precdence[op]:
									opbrac.pop()
									if operand.is_empty() == True:
										return "Error"
									a = operand.peek()
									operand.pop()
									if operand.is_empty() == True:
										return "Error"
									b = operand.peek()
									operand.pop()
									if op == "+":
										ans = a + b
									elif op == "-":
										if opbrac.peek() == "-":
											ans = b + a
										else:
											ans= b-a
									elif op == "*":
										ans = b*a
									elif op == "/":
										if a == 0:
											return "Error"
										ans = b/a
									else:
										return "Error"
									# print(ans,"c")
									# print(a,b,ans)
									operand.push(ans)

									op = opbrac.peek()
								else:
									opbrac.push(i)
									break
							else:
								opbrac.push(i)
						else:
							opbrac.push(i)
			print(opbrac)
			if opbrac.is_empty() == False:
				# print("a")
				return "Error"
			return operand.peek()
		else:
			return "Error"

	def get_history(self):
		s = []
		while self.history.is_empty() == False:
			s.append(self.history.peek())
			self.history.pop()
		return s
calculator = AdvancedCalculator()
# tokens = calculator.tokenize("2+3+(5)*9*9/5")
# print(tokens)
# ans = calculator.evaluate_list_tokens(tokens)
# b= calculator.check_brackets(tokens)
# ans = calculator.evaluate_expression("2+3")
ans = calculator.evaluate_expression("30-(92)* 94 *88/35*62+{(55/((  76+11)-58) *7 -( 39   -74 *96 - 90-  72  )/97 -4  / 28)- 53   }  -92-24+ (((27)+(33/((59)))))")
history = calculator.get_history()
print(history)
# print(b)
print(ans)