class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set(["+", "/", "-", "*"])
        for each in tokens:
            if each not in operator:
                stack.append(int(each))
            else:
                b, a = stack.pop(), stack.pop() 
                if each == "*":
                    stack.append(a*b)
                if each =="/":
                    if b !=0:
                        stack.append(int(a/b))
                if each =="-":
                    stack.append(a-b)
                if each == "+":
                    stack.append(a+b)
        return stack[-1]
                    
