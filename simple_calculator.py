from stack import Stack

class SimpleCalculator():
    def __init__(self):
        self.a=None
        self.x=None
        self.y=None
        self.history=Stack()

    def evaluate_expression(self,input_expression):
        s=input_expression.replace(' ','')
        for i in range(len(s)):
            if (s[i]=='+') or (s[i]=='-') or (s[i]=='*') or (s[i]=='/'):
                self.a=s[i]
                x=s[:i]
                y=s[i+1:]
                # print(x,y,"vvv")
                if x.isdigit() and y.isdigit():
                    self.x=int(x)
                    self.y=int(y)
                    if self.a=='+':
                        ans=(float(self.x+self.y))
                    elif self.a=='-':
                        ans=(float(self.x-self.y))
                    elif self.a=='*':
                        ans=(float(self.x*self.y))
                    elif self.a=='/':
                        if self.y!=0:
                            ans=(float(self.x/self.y))
                        else:
                            ans='Error'
                    else:
                        ans='Error'
                else:
                    ans='Error'
            else:
                continue

        self.history.push((input_expression,ans))
        return(ans)
    
    def get_history(self):
        s=[]
        while not self.history.is_empty():
            s.append(self.history.peek())
            self.history.pop()
        return(s)
calculator = SimpleCalculator()
# answer = calculator.evaluate_expression("2    / 4") # answer should be 5.0
answer = calculator.evaluate_expression("2+   ") # answer should be "Error"
# history = calculator.get_history() # history should be [("2 +", "Error"), ("2 + 3", 5.0)]
print(answer)
# print(history)