class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for each in tokens:
            if each=="+":
                stack.append(stack.pop()+stack.pop())
            elif each=="-":
                a,b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif each=="*":
                stack.append(stack.pop()* stack.pop())
            elif each=="/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(each))
        return stack[0]
        