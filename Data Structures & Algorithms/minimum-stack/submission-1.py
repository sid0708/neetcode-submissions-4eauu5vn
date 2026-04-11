class MinStack:

    def __init__(self):
        self.lst = []
        self.minlist = []

        
    def push(self, val: int) -> None:
        self.lst.append(val)
        val = min(val, self.minlist[-1] if self.minlist else val)
        self.minlist.append(val)

        
    def pop(self) -> None:
        self.lst.pop()
        self.minlist.pop()

    def top(self) -> int:
        return self.lst[-1]
     

    def getMin(self) -> int:
        return self.minlist[-1]
    
        
